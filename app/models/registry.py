"""
Canonical Target Registry models and programmatic loaders for config/targets.yaml.
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
import yaml
import hashlib


@dataclass
class SeedSku:
    url: str
    category: str
    sku_id: str


@dataclass
class CategorySeed:
    category: str
    url: str


@dataclass
class CanonicalTarget:
    target_id: str
    retailer: str
    country: str
    iso_country: str
    domain: str
    locale: str
    currency: str
    timezone: str
    discovery_methods: List[str]
    category_seeds: List[CategorySeed]
    sitemap_urls: List[str]
    max_concurrency: int
    rate_limit: float
    enabled: bool
    preferred_strategy: str = "auto"
    rate_limit_policy: str = "default"
    custom_adapter: Optional[str] = None
    custom_selectors: Dict[str, str] = field(default_factory=dict)
    seed_urls: List[SeedSku] = field(default_factory=list)

    @property
    def brand_name(self) -> str:
        return self.retailer.title()

    @property
    def base_url(self) -> str:
        proto = "https"
        dom = self.domain
        if dom.startswith("store.") or dom.startswith("articulo."):
            return f"{proto}://{dom}"
        return f"{proto}://www.{dom}"


class TargetRegistry:
    """Canonical registry that loads config/targets.yaml and computes aggregate counts programmatically."""
    
    def __init__(self, config_path: Optional[Path] = None):
        if config_path is None:
            config_path = Path("/Users/priteshhome/crawl/config/targets.yaml")
            if not config_path.exists():
                config_path = Path("config/targets.yaml")
        self.config_path = Path(config_path)
        self._raw_yaml: str = ""
        self._targets: Dict[str, CanonicalTarget] = {}
        self.load()

    def load(self) -> None:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Canonical targets registry not found at {self.config_path}")
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            self._raw_yaml = f.read()
            data = yaml.safe_load(self._raw_yaml)

        self._firecrawl_config = data.get("firecrawl", {})
        targets_dict = data.get("targets", {})
        self._targets = {}

        for tid, t_data in targets_dict.items():
            cat_seeds = [
                CategorySeed(category=cs.get("category", ""), url=cs.get("url", ""))
                for cs in t_data.get("category_seeds", [])
            ]
            seeds = []
            for s in t_data.get("seed_urls", []):
                if isinstance(s, dict):
                    seeds.append(SeedSku(
                        url=s.get("url", ""),
                        category=s.get("category", "General"),
                        sku_id=s.get("sku_id", "")
                    ))
                elif isinstance(s, str):
                    seeds.append(SeedSku(url=s, category="General", sku_id=""))

            target = CanonicalTarget(
                target_id=t_data.get("target_id", tid),
                retailer=t_data.get("retailer", ""),
                country=t_data.get("country", ""),
                iso_country=t_data.get("iso_country", ""),
                domain=t_data.get("domain", ""),
                locale=t_data.get("locale", "en-US"),
                currency=t_data.get("currency", "USD"),
                timezone=t_data.get("timezone", "UTC"),
                discovery_methods=t_data.get("discovery_methods", ["seed"]),
                category_seeds=cat_seeds,
                sitemap_urls=t_data.get("sitemap_urls", []),
                max_concurrency=t_data.get("max_concurrency", 2),
                rate_limit=float(t_data.get("rate_limit", 1.0)),
                enabled=bool(t_data.get("enabled", True)),
                preferred_strategy=t_data.get("preferred_strategy", "auto"),
                rate_limit_policy=t_data.get("rate_limit_policy", "default"),
                custom_adapter=t_data.get("custom_adapter", None),
                custom_selectors=t_data.get("custom_selectors", {}),
                seed_urls=seeds
            )
            self._targets[tid] = target

    @property
    def raw_yaml(self) -> str:
        return self._raw_yaml

    @property
    def firecrawl_config(self) -> Dict[str, Any]:
        return getattr(self, "_firecrawl_config", {})

    @property
    def configuration_hash(self) -> str:
        """Computes SHA-256 hash of targets.yaml for the test run manifest."""
        return hashlib.sha256(self._raw_yaml.encode("utf-8")).hexdigest()

    def get(self, target_id: str) -> Optional[CanonicalTarget]:
        return self._targets.get(target_id)

    def all_targets(self, enabled_only: bool = True) -> List[CanonicalTarget]:
        if enabled_only:
            return [t for t in self._targets.values() if t.enabled]
        return list(self._targets.values())

    @property
    def unique_retailers(self) -> int:
        """Programmatically counts distinct retailer brand identities."""
        return len({t.retailer.lower() for t in self._targets.values() if t.enabled})

    @property
    def unique_retailers_list(self) -> List[str]:
        return sorted(list({t.retailer.lower() for t in self._targets.values() if t.enabled}))

    @property
    def retailer_country_targets(self) -> int:
        """Programmatically counts active target configurations."""
        return len([t for t in self._targets.values() if t.enabled])

    @property
    def countries(self) -> int:
        """Programmatically counts distinct ISO country codes."""
        return len({t.iso_country.upper() for t in self._targets.values() if t.enabled})

    @property
    def countries_list(self) -> List[str]:
        return sorted(list({t.iso_country.upper() for t in self._targets.values() if t.enabled}))
