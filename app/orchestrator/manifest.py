"""
Test-Run Manifest Generator.
Creates immutable run manifests at reports/runs/<run_id>/manifest.json.
"""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field


class TestRunManifest(BaseModel):
    run_id: str
    timestamp: str
    git_commit: str
    crawler_version: str = "2.0.0"
    target_count: int
    sku_limit: int
    targets: List[str]
    strategies_enabled: List[str]
    configuration_hash: str
    firecrawl_enabled: bool = True
    firecrawl_base_url: str = "http://localhost:3002"
    firecrawl_version: str = "2.11.0"
    firecrawl_commit: str = "ca0be9b7d91eb9b48d3430f5678211f0d47e1d90"
    firecrawl_modes: List[str] = Field(default_factory=lambda: ["scrape", "map", "crawl", "batch_scrape"])
    firecrawl_concurrency: int = 5
    firecrawl_timeout: int = 30
    proxy_configuration: str = "DISABLED"
    browser_configuration: str = "Chromium / Headless"


class ManifestManager:
    @staticmethod
    def get_git_commit() -> str:
        try:
            res = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=False
            )
            if res.returncode == 0 and res.stdout.strip():
                return res.stdout.strip()
        except Exception:
            pass
        return "unversioned"

    @classmethod
    def create_manifest(
        cls,
        run_id: str,
        target_ids: List[str],
        sku_limit: int,
        configuration_hash: str,
        strategies_enabled: Optional[List[str]] = None,
        base_dir: Optional[Path] = None
    ) -> Path:
        if base_dir is None:
            base_dir = Path("reports/runs") / run_id
        else:
            base_dir = Path(base_dir) / "runs" / run_id

        base_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = base_dir / "manifest.json"

        manifest = TestRunManifest(
            run_id=run_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            git_commit=cls.get_git_commit(),
            crawler_version="1.2.0",
            target_count=len(target_ids),
            sku_limit=sku_limit,
            targets=target_ids,
            strategies_enabled=strategies_enabled or ["HTTP", "PLAYWRIGHT", "ADAPTER"],
            configuration_hash=configuration_hash
        )

        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest.model_dump(), f, indent=2)

        return manifest_path
