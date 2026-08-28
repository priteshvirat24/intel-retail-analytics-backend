"""
Daily Feed Orchestrator Job.
Combines export of SOW §1.5 Price & Promotion dataset with automated sFTP delivery.
"""
import sys
import logging
from pathlib import Path
from typing import Optional, Dict, Any

from app.delivery.feed_exporter import DailyFeedExporter
from app.delivery.sftp_publisher import SftpPublisher, SftpConfig, SftpDeliveryResult

logger = logging.getLogger("daily_feed_job")


class DailyFeedJob:
    """Executes daily Price & Promotion feed generation and automated sFTP push."""

    @classmethod
    def run_daily_delivery(
        cls,
        products: Optional[list] = None,
        output_dir: Optional[Path] = None,
        sftp_config: Optional[SftpConfig] = None,
        audit_log_path: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """
        1. Generates timestamped daily CSV feed.
        2. Uploads via sFTP using atomic staging and retry backoff.
        3. Returns execution summary dictionary.
        """
        # Step 1: Export Feed
        feed_path, sha256, record_count = DailyFeedExporter.generate_daily_feed(
            products=products, output_dir=output_dir
        )
        logger.info(
            f"📄 Daily feed generated: {feed_path.name} ({record_count} records, SHA-256: {sha256[:12]}...)"
        )

        # Step 2: Push via sFTP
        publisher = SftpPublisher(config=sftp_config, audit_log_path=audit_log_path)
        delivery_res = publisher.upload_file(local_path=feed_path)

        return {
            "feed_file": str(feed_path),
            "feed_filename": feed_path.name,
            "record_count": record_count,
            "file_sha256": sha256,
            "sftp_result": delivery_res,
            "success": delivery_res.success,
        }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    res = DailyFeedJob.run_daily_delivery()
    print("\n--- Daily Feed Delivery Summary ---")
    print(f"File: {res['feed_filename']}")
    print(f"Records: {res['record_count']}")
    print(f"Status: {res['sftp_result'].status}")
    if not res["success"]:
        sys.exit(1)
