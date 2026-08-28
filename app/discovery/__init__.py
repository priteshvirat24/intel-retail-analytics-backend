from typing import List, Tuple, Dict, Any, Optional, Union
from collections import defaultdict
from app.models.registry import CanonicalTarget, SeedSku
from app.models.retailer import RetailerTargetConfig
from app.discovery.base import BaseDiscovery
from app.discovery.sitemap import SitemapDiscovery
from app.discovery.category import CategoryDiscovery
from app.discovery.search import SearchDiscovery
from app.discovery.deduplicator import ProductDeduplicator


class ProductDiscoveryEngine:
    """Unified Product Discovery Engine with category diversity balancing."""

    def __init__(self, target_config: Union[CanonicalTarget, RetailerTargetConfig]):
        self.target_config = target_config
        self.sitemap_discovery = SitemapDiscovery(target_config)
        self.category_discovery = CategoryDiscovery(target_config)
        self.search_discovery = SearchDiscovery(target_config)

    def _balance_category_diversity(self, candidate_seeds: List[Any], limit: int) -> List[Any]:
        """Round-robin interleaving across categories to ensure category diversity."""
        if not candidate_seeds:
            return []

        by_cat = defaultdict(list)
        for item in candidate_seeds:
            cat = "General"
            if isinstance(item, SeedSku):
                cat = item.category
            elif isinstance(item, dict):
                cat = item.get("category", "General")
            by_cat[cat].append(item)

        balanced: List[Any] = []
        categories = list(by_cat.keys())
        idx = 0
        while len(balanced) < limit and any(by_cat[c] for c in categories):
            cat = categories[idx % len(categories)]
            if by_cat[cat]:
                balanced.append(by_cat[cat].pop(0))
            idx += 1

        return balanced

    async def discover_products(self, limit: int = 20) -> Tuple[List[Dict[str, Any]], bool, str]:
        """
        Discovers product candidate records attempting multi-channel discovery and balancing categories.
        Returns (list_of_sku_dicts_with_category, is_discovery_limited, reason_summary).
        """
        candidate_records: List[Dict[str, Any]] = []

        # 1. Configured seeds (with category diversity)
        if hasattr(self.target_config, "seed_urls") and self.target_config.seed_urls:
            raw_seeds = self.target_config.seed_urls
            # Balance across categories
            balanced_seeds = self._balance_category_diversity(raw_seeds, limit)
            for s in balanced_seeds:
                if isinstance(s, SeedSku):
                    candidate_records.append({"url": s.url, "category": s.category, "sku_id": s.sku_id})
                elif isinstance(s, dict):
                    candidate_records.append({"url": s.get("url", ""), "category": s.get("category", "General"), "sku_id": s.get("sku_id", "")})
                elif isinstance(s, str):
                    candidate_records.append({"url": s, "category": "General", "sku_id": ""})

        # 2. Try Category Listing Pages if more needed
        if len(candidate_records) < limit:
            try:
                cat_urls = await self.category_discovery.discover_urls(limit=limit)
                for u in cat_urls:
                    candidate_records.append({"url": u, "category": "Category Crawl", "sku_id": ""})
            except Exception:
                pass

        # 3. Try Retailer Search if needed
        if len(candidate_records) < limit:
            try:
                search_urls = await self.search_discovery.discover_urls(limit=limit)
                for u in search_urls:
                    candidate_records.append({"url": u, "category": "Search Crawl", "sku_id": ""})
            except Exception:
                pass

        # 4. Try Sitemap / SitemapIndex if needed
        if len(candidate_records) < limit:
            try:
                sitemap_urls = await self.sitemap_discovery.discover_urls(limit=limit)
                for u in sitemap_urls:
                    candidate_records.append({"url": u, "category": "Sitemap Crawl", "sku_id": ""})
            except Exception:
                pass

        # Deduplicate URLs
        seen_urls = set()
        deduped_records = []
        for r in candidate_records:
            u = r["url"]
            if u and u not in seen_urls:
                seen_urls.add(u)
                deduped_records.append(r)
            if len(deduped_records) >= limit:
                break

        if len(deduped_records) >= limit:
            return deduped_records, False, f"Successfully discovered target {len(deduped_records)} SKUs across {len(set(r['category'] for r in deduped_records))} categories."
        elif len(deduped_records) >= 10:
            return deduped_records, False, f"Discovered minimum requirement {len(deduped_records)} SKUs across {len(set(r['category'] for r in deduped_records))} categories."
        elif len(deduped_records) > 0:
            return deduped_records, True, f"DISCOVERY_LIMITED: Discovered {len(deduped_records)} SKUs (below target {limit})."
        else:
            return [], True, "DISCOVERY_FAILURE: Could not discover any valid product URLs."


__all__ = [
    "BaseDiscovery",
    "ProductDeduplicator",
    "SitemapDiscovery",
    "CategoryDiscovery",
    "SearchDiscovery",
    "ProductDiscoveryEngine",
]
