"""
Share of Shelf (SOS) Analytics Engine.
Calculates % of Intel Core SKUs vs total SKUs per OEM per retailer, competitor share, and ranks.
"""
from typing import List, Dict, Any


class ShareOfShelfEngine:
    """Computes Share of Shelf (SOS) across retailers, OEMs, and processor families."""

    @classmethod
    def compute_share_of_shelf(cls, products: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Computes overall SOS, retailer SOS, OEM SOS, and competitive breakdown.
        """
        def is_intel(p: Dict[str, Any]) -> bool:
            if p.get("is_intel") is True or p.get("is_intel_cpu") is True:
                return True
            proc = str(p.get("processor") or p.get("processor_brand") or "").lower()
            return "intel" in proc

        def is_brand(p: Dict[str, Any], brand: str) -> bool:
            proc = str(p.get("processor") or p.get("processor_brand") or "").lower()
            return brand.lower() in proc

        total_skus = len(products)
        intel_skus = [p for p in products if is_intel(p)]
        amd_skus = [p for p in products if is_brand(p, "amd")]
        apple_skus = [p for p in products if is_brand(p, "apple")]
        qualcomm_skus = [p for p in products if is_brand(p, "qualcomm")]

        overall_sos = {
            "total_skus": total_skus,
            "intel_skus_count": len(intel_skus),
            "intel_sos_pct": round((len(intel_skus) / total_skus * 100), 1) if total_skus else 0.0,
            "amd_skus_count": len(amd_skus),
            "amd_sos_pct": round((len(amd_skus) / total_skus * 100), 1) if total_skus else 0.0,
            "apple_skus_count": len(apple_skus),
            "apple_sos_pct": round((len(apple_skus) / total_skus * 100), 1) if total_skus else 0.0,
            "qualcomm_skus_count": len(qualcomm_skus),
            "qualcomm_sos_pct": round((len(qualcomm_skus) / total_skus * 100), 1) if total_skus else 0.0,
        }

        # Retailer-level SOS
        retailers = sorted(list(set(p.get("retailer") or p.get("account") or "Unknown" for p in products)))
        retailer_sos = {}
        for ret in retailers:
            ret_items = [p for p in products if (p.get("retailer") or p.get("account")) == ret]
            r_total = len(ret_items)
            r_intel = sum(1 for p in ret_items if is_intel(p))
            r_amd = sum(1 for p in ret_items if is_brand(p, "amd"))
            r_apple = sum(1 for p in ret_items if is_brand(p, "apple"))
            r_qualcomm = sum(1 for p in ret_items if is_brand(p, "qualcomm"))

            retailer_sos[ret] = {
                "retailer": ret,
                "total_skus": r_total,
                "intel_count": r_intel,
                "intel_sos_pct": round((r_intel / r_total * 100), 1) if r_total else 0.0,
                "amd_count": r_amd,
                "amd_sos_pct": round((r_amd / r_total * 100), 1) if r_total else 0.0,
                "apple_count": r_apple,
                "apple_sos_pct": round((r_apple / r_total * 100), 1) if r_total else 0.0,
                "qualcomm_count": r_qualcomm,
                "qualcomm_sos_pct": round((r_qualcomm / r_total * 100), 1) if r_total else 0.0,
            }

        # OEM-level SOS & Ranking
        oems = sorted(list(set(p.get("oem") or p.get("brand") or "Unknown OEM" for p in products)))
        oem_sos_list = []
        for oem in oems:
            oem_items = [p for p in products if (p.get("oem") or p.get("brand")) == oem]
            o_total = len(oem_items)
            o_intel = sum(1 for p in oem_items if is_intel(p))
            o_amd = sum(1 for p in oem_items if is_brand(p, "amd"))
            o_apple = sum(1 for p in oem_items if is_brand(p, "apple"))
            o_qualcomm = sum(1 for p in oem_items if is_brand(p, "qualcomm"))

            oem_sos_list.append({
                "oem": oem,
                "total_skus": o_total,
                "intel_count": o_intel,
                "intel_sos_pct": round((o_intel / o_total * 100), 1) if o_total else 0.0,
                "amd_count": o_amd,
                "apple_count": o_apple,
                "qualcomm_count": o_qualcomm,
            })

        # Rank OEMs by Intel SKU Count
        oem_sos_list.sort(key=lambda x: (x["intel_count"], x["intel_sos_pct"]), reverse=True)
        for idx, o in enumerate(oem_sos_list, 1):
            o["rank"] = idx

        return {
            "overall_sos": overall_sos,
            "retailer_sos": retailer_sos,
            "oem_sos_ranks": oem_sos_list
        }
