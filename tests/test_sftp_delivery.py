"""
Integration & Unit Tests for Automated sFTP Data Feed Delivery Subsystem.
Runs an actual local Paramiko SFTP server on localhost to verify:
1. Schema completeness against SOW §1.5 Product Data Attributes.
2. End-to-end socket connection, authentication, file transfer, and SHA-256 verification.
3. Atomic staging and rename verification (zero partial-file risk).
4. Exponential backoff retry logic (3 attempts) on simulated connection failures.
5. Contractual [CRITICAL_DELIVERY_FAILURE] alerting and audit log generation.
"""
import os
import sys
import json
import time
import socket
import threading
import tempfile
import hashlib
from pathlib import Path
import pytest
import paramiko
from paramiko import (
    AUTH_SUCCESSFUL,
    AUTH_FAILED,
    OPEN_SUCCEEDED,
    OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED,
    SFTP_OK,
    SFTP_NO_SUCH_FILE,
    SFTP_FAILURE,
    SFTPHandle,
    SFTPAttributes,
    SFTPServerInterface,
    SFTPServer,
)

from app.delivery.feed_exporter import DailyFeedExporter, FEED_HEADERS
from app.delivery.sftp_publisher import SftpPublisher, SftpConfig, SftpDeliveryResult
from app.delivery.daily_feed_job import DailyFeedJob


class RealAuth(paramiko.ServerInterface):
    """SSH authentication server interface for testing."""
    def __init__(self, expected_user="intel_feed_user", expected_pass="secret_pass_123"):
        self.expected_user = expected_user
        self.expected_pass = expected_pass

    def check_auth_password(self, username, password):
        if username == self.expected_user and password == self.expected_pass:
            return AUTH_SUCCESSFUL
        return AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return OPEN_SUCCEEDED
        return OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED


class RealSFTP(SFTPServerInterface):
    """Filesystem-backed SFTP Server Interface for live testbed uploads."""
    def __init__(self, server, *args, **kwargs):
        super().__init__(server, *args, **kwargs)
        self.root = server.root_dir

    def _p(self, path):
        clean_path = path.lstrip("/")
        return os.path.join(self.root, clean_path)

    def stat(self, path):
        rp = self._p(path)
        if os.path.exists(rp):
            return SFTPAttributes.from_stat(os.stat(rp))
        return SFTP_NO_SUCH_FILE

    def lstat(self, path):
        return self.stat(path)

    def open(self, path, flags, attr):
        rp = self._p(path)
        os.makedirs(os.path.dirname(rp), exist_ok=True)
        try:
            if (flags & os.O_CREAT) and (flags & os.O_WRONLY):
                mode = "wb+" if (flags & os.O_TRUNC) else "ab+"
            elif flags & os.O_WRONLY:
                mode = "wb"
            elif flags & os.O_RDWR:
                mode = "rb+"
            else:
                mode = "rb"
            f = open(rp, mode)
            h = SFTPHandle(flags)
            h.read = lambda offset, length: (f.seek(offset), f.read(length))[1]
            h.write = lambda offset, data: (f.seek(offset), f.write(data), SFTP_OK)[2]
            h.close = lambda: (f.close(), SFTP_OK)[1]
            h.stat = lambda: SFTPAttributes.from_stat(os.fstat(f.fileno()))
            return h
        except IOError:
            return SFTP_FAILURE

    def remove(self, path):
        try:
            os.remove(self._p(path))
            return SFTP_OK
        except Exception:
            return SFTP_NO_SUCH_FILE

    def rename(self, oldpath, newpath):
        try:
            ro = self._p(oldpath)
            rn = self._p(newpath)
            os.makedirs(os.path.dirname(rn), exist_ok=True)
            if os.path.exists(rn):
                os.remove(rn)
            os.rename(ro, rn)
            return SFTP_OK
        except Exception:
            return SFTP_FAILURE

    def mkdir(self, path, attr):
        try:
            os.makedirs(self._p(path), exist_ok=True)
            return SFTP_OK
        except Exception:
            return SFTP_FAILURE


class LocalSftpTestServer:
    """Spawns an actual Paramiko SFTP test server listening on an ephemeral localhost port."""

    def __init__(self, root_dir: Path, username="intel_feed_user", password="secret_pass_123"):
        self.root_dir = str(root_dir)
        self.username = username
        self.password = password
        self.host_key = paramiko.RSAKey.generate(2048)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(5)
        self.port = self.sock.getsockname()[1]
        self.running = True
        self.thread = threading.Thread(target=self._run_server, daemon=True)
        self.thread.start()

    def _run_server(self):
        while self.running:
            try:
                self.sock.settimeout(0.5)
                client_sock, _ = self.sock.accept()
            except socket.timeout:
                continue
            except Exception:
                break

            t = paramiko.Transport(client_sock)
            t.add_server_key(self.host_key)
            t.set_subsystem_handler("sftp", SFTPServer, sftp_si=RealSFTP)
            server = RealAuth(self.username, self.password)
            server.root_dir = self.root_dir
            try:
                t.start_server(server=server)
                chan = t.accept(10)
                while t.is_active():
                    time.sleep(0.02)
            except Exception:
                pass
            finally:
                try:
                    t.close()
                except Exception:
                    pass

    def stop(self):
        self.running = False
        try:
            self.sock.close()
        except Exception:
            pass


@pytest.fixture
def local_sftp_server():
    with tempfile.TemporaryDirectory() as tmpdir:
        srv_root = Path(tmpdir)
        (srv_root / "uploads" / "daily_feeds").mkdir(parents=True, exist_ok=True)
        server = LocalSftpTestServer(root_dir=srv_root)
        time.sleep(0.1)
        yield server, srv_root
        server.stop()


# --------------------------------------------------------------------------
# Test 1: SOW §1.5 Feed Schema Completeness
# --------------------------------------------------------------------------
def test_feed_exporter_schema_completeness(tmp_path):
    feed_file, sha256, count = DailyFeedExporter.generate_daily_feed(output_dir=tmp_path)
    assert feed_file.exists()
    assert count > 0

    with open(feed_file, "r", encoding="utf-8") as f:
        header_line = f.readline().strip().split(",")

    assert header_line == FEED_HEADERS
    for req_col in [
        "retailer", "country", "product_id", "product_title", "product_description",
        "oem", "model_and_series", "processor_brand", "processor_series",
        "processor_number", "processor_generation", "graphics_card", "form_factor",
        "screen_size", "screen_type", "ram_gb", "storage_gb", "storage_type",
        "operating_system", "original_price_local", "selling_price_local",
        "usd_original_price", "usd_selling_price", "discount_amount_local",
        "discount_pct", "currency", "price_history", "availability", "product_url"
    ]:
        assert req_col in header_line


# --------------------------------------------------------------------------
# Test 2: Real Local SFTP End-to-End Delivery & Atomic Rename Verification
# --------------------------------------------------------------------------
def test_real_local_sftp_delivery_end_to_end(local_sftp_server, tmp_path):
    server, srv_root = local_sftp_server
    audit_log = tmp_path / "test_delivery_audit.log"

    # Generate feed
    feed_path, local_sha256, count = DailyFeedExporter.generate_daily_feed(output_dir=tmp_path)
    local_bytes = feed_path.read_bytes()

    config = SftpConfig(
        host="127.0.0.1",
        port=server.port,
        username="intel_feed_user",
        password="secret_pass_123",
        remote_path="/uploads/daily_feeds/",
        max_retries=3,
        retry_backoff_sec=0.1,
        enabled=True,
    )

    publisher = SftpPublisher(config=config, audit_log_path=audit_log)
    result = publisher.upload_file(local_path=feed_path)

    # 1. Assert result status
    assert result.success is True
    assert result.status == "SUCCESS"
    assert result.attempts == 1
    assert result.file_sha256 == local_sha256
    assert result.bytes_transferred == len(local_bytes)

    # 2. Verify file arrived on the actual test server filesystem
    remote_uploaded_file = srv_root / "uploads" / "daily_feeds" / feed_path.name
    assert remote_uploaded_file.exists(), f"Expected {remote_uploaded_file} to exist on remote filesystem"

    # 3. Verify SHA-256 byte-for-byte integrity
    remote_bytes = remote_uploaded_file.read_bytes()
    remote_sha256 = hashlib.sha256(remote_bytes).hexdigest()
    assert remote_sha256 == local_sha256
    assert len(remote_bytes) == len(local_bytes)

    # 4. Verify no staging/temp files left on remote server (atomic rename cleanup)
    all_remote_files = list((srv_root / "uploads" / "daily_feeds").iterdir())
    assert len(all_remote_files) == 1
    assert all_remote_files[0].name == feed_path.name

    # 5. Verify audit log entry
    assert audit_log.exists()
    with open(audit_log, "r", encoding="utf-8") as f:
        log_entry = json.loads(f.readline().strip())
    assert log_entry["status"] == "SUCCESS"
    assert log_entry["file_sha256"] == local_sha256
    assert log_entry["bytes_sent"] == len(local_bytes)


# --------------------------------------------------------------------------
# Test 3: Simulated Failure, 3-Attempt Backoff Retry, & Critical Alerting
# --------------------------------------------------------------------------
def test_sftp_retry_backoff_and_critical_failure_alert(tmp_path, capsys):
    audit_log = tmp_path / "test_failure_audit.log"
    feed_path, local_sha256, _ = DailyFeedExporter.generate_daily_feed(output_dir=tmp_path)

    # Use a non-listening port to force connection failure
    unused_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    unused_sock.bind(("127.0.0.1", 0))
    dead_port = unused_sock.getsockname()[1]
    unused_sock.close()

    config = SftpConfig(
        host="127.0.0.1",
        port=dead_port,
        username="intel_feed_user",
        password="secret_pass_123",
        remote_path="/uploads/daily_feeds/",
        max_retries=3,
        retry_backoff_sec=0.05,
        connect_timeout=1.0,
        enabled=True,
    )

    publisher = SftpPublisher(config=config, audit_log_path=audit_log)
    result = publisher.upload_file(local_path=feed_path)

    # 1. Assert failure status & 3 retry attempts
    assert result.success is False
    assert result.status == "FAILED"
    assert result.attempts == 3
    assert result.bytes_transferred == 0
    assert result.error_message is not None

    # 2. Verify loud alert banner surfaced in stderr
    captured = capsys.readouterr()
    assert "[CRITICAL_DELIVERY_FAILURE]" in captured.err
    assert "CONTRACTUAL DAILY sFTP PUSH FAILED" in captured.err

    # 3. Verify failure audit log entry
    assert audit_log.exists()
    with open(audit_log, "r", encoding="utf-8") as f:
        log_entry = json.loads(f.readline().strip())
    assert log_entry["status"] == "FAILED"
    assert log_entry["attempts"] == 3


# --------------------------------------------------------------------------
# Test 4: Graceful Handling When SFTP_ENABLED=false
# --------------------------------------------------------------------------
def test_sftp_disabled_mode_returns_gracefully(tmp_path):
    audit_log = tmp_path / "test_disabled_audit.log"
    feed_path, local_sha256, _ = DailyFeedExporter.generate_daily_feed(output_dir=tmp_path)

    config = SftpConfig(
        host="example.com",
        port=22,
        username="intel_feed_user",
        enabled=False,
    )

    publisher = SftpPublisher(config=config, audit_log_path=audit_log)
    result = publisher.upload_file(local_path=feed_path)

    assert result.success is True
    assert result.status == "DISABLED"
    assert result.attempts == 0
