"""
Banner Tracking & Visual Placement Analytics Engine.
Calculates banner brand counts, destination link validity, and flag breakdowns (EVO/Gaming/Premier).
"""
from typing import List, Dict, Any


class BannerAnalyticsEngine:
    """Computes homepage and category banner presence, promo depth, and link fidelity."""

    @classmethod
    def compute_banner_analytics(cls, banners: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Computes brand share of banners, destination link validity, and promo flags.
        """
        total_banners = len(banners)
        intel_banners = [b for b in banners if "Intel" in b.get("brand", "")]
        has_dest_link_count = sum(1 for b in banners if b.get("has_destination_link"))

        evo_flag_count = sum(1 for b in banners if b.get("flags", {}).get("evo_flag"))
        gaming_flag_count = sum(1 for b in banners if b.get("flags", {}).get("gaming_flag"))
        premier_sku_count = sum(1 for b in banners if b.get("flags", {}).get("premier_sku_flag"))
        ai_pc_flag_count = sum(1 for b in banners if b.get("flags", {}).get("ai_pc_flag"))

        brand_breakdown = {}
        for b in banners:
            br = b.get("brand", "Other")
            brand_breakdown[br] = brand_breakdown.get(br, 0) + 1

        return {
            "total_banners": total_banners,
            "intel_banners_count": len(intel_banners),
            "intel_banner_share_pct": round((len(intel_banners) / total_banners * 100), 1) if total_banners else 0.0,
            "destination_link_compliance_pct": round((has_dest_link_count / total_banners * 100), 1) if total_banners else 0.0,
            "flag_breakdown": {
                "evo_banners": evo_flag_count,
                "evo_banners_pct": round((evo_flag_count / total_banners * 100), 1) if total_banners else 0.0,
                "gaming_banners": gaming_flag_count,
                "gaming_banners_pct": round((gaming_flag_count / total_banners * 100), 1) if total_banners else 0.0,
                "premier_sku_banners": premier_sku_count,
                "premier_sku_banners_pct": round((premier_sku_count / total_banners * 100), 1) if total_banners else 0.0,
                "ai_pc_banners": ai_pc_flag_count,
                "ai_pc_banners_pct": round((ai_pc_flag_count / total_banners * 100), 1) if total_banners else 0.0,
            },
            "brand_breakdown": brand_breakdown,
            "banner_records": banners
        }
