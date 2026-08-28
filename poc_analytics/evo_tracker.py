"""
Intel EVO Badge Tracking Analytics.
Calculates count and % of SKUs with EVO badge/mention, categorized by retailer.
"""
from typing import List, Dict, Any
import statistics


class EvoTracker:
    """Computes Intel EVO badge adoption, retailer compliance, and price premium metrics."""

    @classmethod
    def compute_evo_metrics(cls, products: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculates EVO badge counts, percentages by retailer, and EVO vs non-EVO pricing.
        """
        laptops = [p for p in products if p["form_factor"] == "Laptop"]
        intel_laptops = [p for p in laptops if p["is_intel_cpu"]]
        
        evo_skus = [p for p in intel_laptops if p.get("is_evo")]
        non_evo_intel_laptops = [p for p in intel_laptops if not p.get("is_evo")]

        total_evo_count = len(evo_skus)
        total_intel_laptop_count = len(intel_laptops)
        evo_penetration_pct = round((total_evo_count / total_intel_laptop_count * 100), 1) if total_intel_laptop_count > 0 else 0.0

        retailers = sorted(list(set(p["retailer"] for p in products)))
        retailer_evo_breakdown = {}

        for ret in retailers:
            ret_intel_laptops = [p for p in intel_laptops if p["retailer"] == ret]
            ret_evo = [p for p in ret_intel_laptops if p.get("is_evo")]
            
            retailer_evo_breakdown[ret] = {
                "retailer": ret,
                "total_intel_laptops": len(ret_intel_laptops),
                "evo_badged_count": len(ret_evo),
                "evo_badge_pct": round((len(ret_evo) / len(ret_intel_laptops) * 100), 1) if ret_intel_laptops else 0.0,
                "evo_skus": [s["model_series"] for s in ret_evo]
            }

        # Pricing comparison: EVO vs Non-EVO Intel Laptops
        evo_prices = [p["current_price"] for p in evo_skus]
        non_evo_prices = [p["current_price"] for p in non_evo_intel_laptops]

        avg_evo_price = round(statistics.mean(evo_prices), 2) if evo_prices else 0.0
        avg_non_evo_price = round(statistics.mean(non_evo_prices), 2) if non_evo_prices else 0.0
        evo_premium_pct = round(((avg_evo_price - avg_non_evo_price) / avg_non_evo_price) * 100, 1) if avg_non_evo_price > 0 else 0.0

        return {
            "total_intel_laptops": total_intel_laptop_count,
            "total_evo_badged_skus": total_evo_count,
            "overall_evo_penetration_pct": evo_penetration_pct,
            "avg_evo_price_usd": avg_evo_price,
            "avg_non_evo_price_usd": avg_non_evo_price,
            "evo_price_premium_pct": evo_premium_pct,
            "retailer_evo_breakdown": retailer_evo_breakdown,
            "evo_sku_list": evo_skus
        }
