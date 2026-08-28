"""
Automated sFTP Publisher Subsystem.
Provides enterprise-grade, atomic sFTP uploads with exponential backoff retry logic,
cryptographic SHA-256 validation, and loud contractual failure alerting.
"""
import os
import sys
import time
import uuid
import hashlib
import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any, Tuple

import paramiko

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_AUDIT_LOG = PROJECT_ROOT / "reports" / "delivery_audit.log"

logger = logging.getLogger("sftp_publisher")


@dataclass
class SftpConfig:
    host: str = ""
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    private_key_path: Optional[str] = None
    remote_path: str = "/uploads/daily_feeds/"
    max_retries: int = 3
    retry_backoff_sec: float = 2.0
    connect_timeout: float = 15.0
    enabled: bool = False

    @classmethod
    def from_env(cls) -> "SftpConfig":
        return cls(
            host=os.getenv("SFTP_HOST", "localhost"),
            port=int(os.getenv("SFTP_PORT", "22")),
            username=os.getenv("SFTP_USERNAME", ""),
            password=os.getenv("SFTP_PASSWORD") or None,
            private_key_path=os.getenv("SFTP_PRIVATE_KEY_PATH") or None,
            remote_path=os.getenv("SFTP_REMOTE_PATH", "/uploads/daily_feeds/"),
            max_retries=int(os.getenv("SFTP_MAX_RETRIES", "3")),
            retry_backoff_sec=float(os.getenv("SFTP_RETRY_BACKOFF_SEC", "2.0")),
            connect_timeout=float(os.getenv("SFTP_CONNECT_TIMEOUT", "15.0")),
            enabled=os.getenv("SFTP_ENABLED", "false").lower() in ("true", "1", "yes"),
        )


@dataclass
class SftpDeliveryResult:
    success: bool
    status: str  # "SUCCESS" | "FAILED" | "DISABLED"
    local_file: str
    remote_file: Optional[str]
    file_sha256: str
    bytes_transferred: int
    attempts: int
    duration_sec: float
    error_message: Optional[str] = None
    timestamp: str = ""


class SftpPublisher:
    """Manages secure, atomic sFTP data feed delivery with retry backoff and audit logging."""

    def __init__(self, config: Optional[SftpConfig] = None, audit_log_path: Optional[Path] = None):
        self.config = config or SftpConfig.from_env()
        self.audit_log_path = audit_log_path or DEFAULT_AUDIT_LOG

    def upload_file(
        self,
        local_path: Path,
        remote_filename: Optional[str] = None,
        config_override: Optional[SftpConfig] = None,
    ) -> SftpDeliveryResult:
        """
        Uploads a local file to the configured sFTP destination using atomic staging and rename.
        Retries up to config.max_retries with exponential backoff on failure.
        """
        cfg = config_override or self.config
        local_file = Path(local_path)
        if not local_file.exists():
            raise FileNotFoundError(f"Local file does not exist: {local_file}")

        file_bytes = local_file.read_bytes()
        file_size = len(file_bytes)
        file_sha256 = hashlib.sha256(file_bytes).hexdigest()
        target_filename = remote_filename or local_file.name

        start_time = time.time()
        now_iso = datetime.now(timezone.utc).isoformat()

        # Check if sFTP is disabled by configuration
        if not cfg.enabled and not config_override:
            msg = "sFTP push is currently disabled via SFTP_ENABLED=false"
            logger.info(msg)
            self._log_audit(
                status="SKIPPED_DISABLED",
                local_file=str(local_file),
                remote_file=f"{cfg.remote_path.rstrip('/')}/{target_filename}",
                file_sha256=file_sha256,
                bytes_sent=0,
                attempts=0,
                duration=round(time.time() - start_time, 3),
                error=msg,
            )
            return SftpDeliveryResult(
                success=True,
                status="DISABLED",
                local_file=str(local_file),
                remote_file=None,
                file_sha256=file_sha256,
                bytes_transferred=0,
                attempts=0,
                duration_sec=round(time.time() - start_time, 3),
                error_message=msg,
                timestamp=now_iso,
            )

        # Validate host configuration
        if not cfg.host or not cfg.username:
            err = f"Incomplete sFTP configuration: host='{cfg.host}', username='{cfg.username}'"
            self._emit_critical_alert(target_filename, cfg, err, attempts=0)
            self._log_audit(
                status="FAILED_CONFIG",
                local_file=str(local_file),
                remote_file=f"{cfg.remote_path.rstrip('/')}/{target_filename}",
                file_sha256=file_sha256,
                bytes_sent=0,
                attempts=0,
                duration=round(time.time() - start_time, 3),
                error=err,
            )
            return SftpDeliveryResult(
                success=False,
                status="FAILED",
                local_file=str(local_file),
                remote_file=None,
                file_sha256=file_sha256,
                bytes_transferred=0,
                attempts=0,
                duration_sec=round(time.time() - start_time, 3),
                error_message=err,
                timestamp=now_iso,
            )

        # Build remote paths
        remote_dir = cfg.remote_path.rstrip("/")
        final_remote_path = f"{remote_dir}/{target_filename}"
        staging_filename = f".{target_filename}.tmp.{uuid.uuid4().hex[:8]}"
        staging_remote_path = f"{remote_dir}/{staging_filename}"

        last_error = None
        attempt = 0

        while attempt < cfg.max_retries:
            attempt += 1
            attempt_start = time.time()
            transport = None
            sftp = None

            try:
                logger.info(
                    f"📤 [Attempt {attempt}/{cfg.max_retries}] Connecting to sFTP server {cfg.host}:{cfg.port} as user '{cfg.username}'..."
                )

                # Initialize socket transport
                transport = paramiko.Transport((cfg.host, cfg.port))
                transport.banner_timeout = cfg.connect_timeout

                # Authenticate
                if cfg.private_key_path and os.path.exists(cfg.private_key_path):
                    pkey = self._load_private_key(cfg.private_key_path, cfg.password)
                    transport.connect(username=cfg.username, pkey=pkey)
                elif cfg.password is not None:
                    transport.connect(username=cfg.username, password=cfg.password)
                else:
                    transport.connect(username=cfg.username)

                sftp = paramiko.SFTPClient.from_transport(transport)

                # Ensure remote directory exists
                self._ensure_remote_dir(sftp, remote_dir)

                # Step 1: Upload to atomic staging filename
                logger.info(f"⏳ Uploading {file_size:,} bytes to staging path: {staging_remote_path}")
                sftp.put(str(local_file), staging_remote_path)

                # Step 2: Verify uploaded file size matches local file size
                remote_stat = sftp.stat(staging_remote_path)
                if remote_stat.st_size != file_size:
                    raise IOError(
                        f"Staging file size mismatch: local is {file_size} bytes, remote staging is {remote_stat.st_size} bytes"
                    )

                # Step 3: Atomic rename from staging to final destination
                logger.info(f"🔄 Performing atomic rename to final path: {final_remote_path}")
                # Remove existing remote file if server does not support atomic overwrite
                try:
                    sftp.remove(final_remote_path)
                except IOError:
                    pass  # File didn't exist, ignore

                sftp.rename(staging_remote_path, final_remote_path)

                total_duration = round(time.time() - start_time, 3)
                logger.info(f"✅ sFTP Delivery Successful: {final_remote_path} ({file_size:,} bytes in {total_duration}s)")

                self._log_audit(
                    status="SUCCESS",
                    local_file=str(local_file),
                    remote_file=final_remote_path,
                    file_sha256=file_sha256,
                    bytes_sent=file_size,
                    attempts=attempt,
                    duration=total_duration,
                    error=None,
                )

                return SftpDeliveryResult(
                    success=True,
                    status="SUCCESS",
                    local_file=str(local_file),
                    remote_file=final_remote_path,
                    file_sha256=file_sha256,
                    bytes_transferred=file_size,
                    attempts=attempt,
                    duration_sec=total_duration,
                    error_message=None,
                    timestamp=now_iso,
                )

            except Exception as e:
                last_error = f"{type(e).__name__}: {str(e)}"
                logger.warning(
                    f"⚠️ [Attempt {attempt}/{cfg.max_retries}] sFTP transfer failed for {target_filename}: {last_error}"
                )

                # Clean up staging file on failure if possible
                if sftp:
                    try:
                        sftp.remove(staging_remote_path)
                    except Exception:
                        pass

                # Exponential backoff sleep before next attempt
                if attempt < cfg.max_retries:
                    backoff = cfg.retry_backoff_sec * (2 ** (attempt - 1))
                    logger.info(f"⏳ Sleeping {backoff:.1f}s before retry attempt {attempt + 1}...")
                    time.sleep(backoff)

            finally:
                if sftp:
                    try:
                        sftp.close()
                    except Exception:
                        pass
                if transport:
                    try:
                        transport.close()
                    except Exception:
                        pass

        # If loop finishes without returning, all attempts failed
        total_duration = round(time.time() - start_time, 3)
        self._emit_critical_alert(target_filename, cfg, last_error or "Unknown error", attempts=attempt)
        self._log_audit(
            status="FAILED",
            local_file=str(local_file),
            remote_file=final_remote_path,
            file_sha256=file_sha256,
            bytes_sent=0,
            attempts=attempt,
            duration=total_duration,
            error=last_error,
        )

        return SftpDeliveryResult(
            success=False,
            status="FAILED",
            local_file=str(local_file),
            remote_file=final_remote_path,
            file_sha256=file_sha256,
            bytes_transferred=0,
            attempts=attempt,
            duration_sec=total_duration,
            error_message=last_error,
            timestamp=now_iso,
        )

    def _ensure_remote_dir(self, sftp: paramiko.SFTPClient, remote_dir: str) -> None:
        """Recursively creates remote directories if they do not exist."""
        if not remote_dir or remote_dir == "/":
            return
        parts = [p for p in remote_dir.split("/") if p]
        curr = "" if not remote_dir.startswith("/") else "/"
        for part in parts:
            curr = f"{curr.rstrip('/')}/{part}"
            try:
                sftp.stat(curr)
            except IOError:
                try:
                    sftp.mkdir(curr)
                except IOError:
                    pass

    def _load_private_key(self, key_path: str, password: Optional[str] = None) -> paramiko.PKey:
        """Attempts loading private key as RSA, Ed25519, or ECDSA."""
        for key_class in (paramiko.RSAKey, paramiko.Ed25519Key, paramiko.ECDSAKey, paramiko.DSSKey):
            try:
                return key_class.from_private_key_file(key_path, password=password)
            except Exception:
                continue
        raise ValueError(f"Unable to load SSH private key from: {key_path}")

    def _log_audit(
        self,
        status: str,
        local_file: str,
        remote_file: Optional[str],
        file_sha256: str,
        bytes_sent: int,
        attempts: int,
        duration: float,
        error: Optional[str],
    ) -> None:
        """Appends structured audit record to reports/delivery_audit.log."""
        try:
            self.audit_log_path.parent.mkdir(parents=True, exist_ok=True)
            entry = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "status": status,
                "local_file": local_file,
                "remote_file": remote_file,
                "file_sha256": file_sha256,
                "bytes_sent": bytes_sent,
                "attempts": attempts,
                "duration_sec": duration,
                "error": error,
            }
            with open(self.audit_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            logger.error(f"Failed to write delivery audit log: {e}")

    def _emit_critical_alert(
        self, filename: str, cfg: SftpConfig, error_msg: str, attempts: int
    ) -> None:
        """Emits an unmissable terminal alert banner when contractual daily delivery fails."""
        alert = f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║ 🚨 [CRITICAL_DELIVERY_FAILURE] CONTRACTUAL DAILY sFTP PUSH FAILED                             ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║ Feed File   : {filename:<78} ║
║ Destination : {cfg.username}@{cfg.host}:{cfg.port}{cfg.remote_path:<48} ║
║ Attempts    : {attempts} / {cfg.max_retries:<73} ║
║ Error       : {error_msg[:78]:<78} ║
║ Action Req  : Check sFTP credentials, network firewall, or remote host availability.         ║
║ Timestamp   : {datetime.now(timezone.utc).isoformat():<78} ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝
"""
        sys.stderr.write(alert + "\n")
        sys.stderr.flush()
