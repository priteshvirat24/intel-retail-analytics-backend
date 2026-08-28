"""
Retailer Audit & Brand Benchmarking Scoring Engine.
Computes S1, S2, P1, P2, P3, P4, P5 scores per SKU and retailer.
Rolls up into overall Brand Compliance Score weighted 85% Laptop / 15% Desktop.
"""
from typing import List, Dict, Any
import statistics


class RetailerAuditScorer:
    """Calculates audit compliance scores, failure flags, and 85/15 weighted rollups."""

    @classmethod
    def compute_retailer_audit_scores(cls, products: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Computes SKU-level, Flag-level, and Retailer-level Brand Compliance Scores.
        Formula: Brand Compliance = (0.85 * Laptop_Score) + (0.15 * Desktop_Score)
        """
        retailers = sorted(list(set(p["retailer"] for p in products)))
        retailer_scorecards = {}

        sku_audit_records = []
        for p in products:
            flags = p.get("audit_flags", {})
            sku_rec = {
                "sku_id": p["sku_id"],
                "oem": p["oem"],
                "model_series": p["model_series"],
                "retailer": p["retailer"],
                "form_factor": p["form_factor"],
                "is_intel_cpu": p["is_intel_cpu"],
                "processor_model": p["processor_model"],
                "S1_pass": flags.get("S1", {}).get("pass", False),
                "S2_pass": flags.get("S2", {}).get("pass", False),
                "P1_pass": flags.get("P1", {}).get("pass", False),
                "P2_pass": flags.get("P2", {}).get("pass", False),
                "P3_pass": flags.get("P3", {}).get("pass", False),
                "P4_pass": flags.get("P4", {}).get("pass", False),
                "P5_pass": flags.get("P5", {}).get("pass", False),
                "sku_score": flags.get("sku_audit_score", 0.0),
                "product_url": p.get("product_url"),
                "screenshot_pdp_path": p.get("screenshot_pdp_path")
            }
            sku_audit_records.append(sku_rec)

        # Flag-level compliance rates
        flag_keys = ["S1", "S2", "P1", "P2", "P3", "P4", "P5"]
        flag_pass_rates = {}
        for f in flag_keys:
            passes = sum(1 for s in sku_audit_records if s[f"{f}_pass"])
            flag_pass_rates[f] = {
                "flag": f,
                "passed_skus": passes,
                "total_skus": len(sku_audit_records),
                "compliance_pct": round((passes / len(sku_audit_records)) * 100, 1)
            }

        # Retailer-level rollup with 85% Laptop / 15% Desktop weighting
        for ret in retailers:
            ret_skus = [s for s in sku_audit_records if s["retailer"] == ret]
            laptop_skus = [s for s in ret_skus if s["form_factor"] == "Laptop"]
            desktop_skus = [s for s in ret_skus if s["form_factor"] == "Desktop"]

            laptop_avg = statistics.mean([s["sku_score"] for s in laptop_skus]) if laptop_skus else 100.0
            desktop_avg = statistics.mean([s["sku_score"] for s in desktop_skus]) if desktop_skus else 100.0

            # 85% Laptop / 15% Desktop Weighted Rollup
            brand_compliance_score = round((0.85 * laptop_avg) + (0.15 * desktop_avg), 1)

            # Grade assignment
            if brand_compliance_score >= 85.0:
                grade = "A (Exemplary)"
            elif brand_compliance_score >= 70.0:
                grade = "B (Compliant)"
            elif brand_compliance_score >= 50.0:
                grade = "C (Needs Remediation)"
            else:
                grade = "D (Critical Violation)"

            retailer_scorecards[ret] = {
                "retailer": ret,
                "total_skus": len(ret_skus),
                "laptop_skus_count": len(laptop_skus),
                "desktop_skus_count": len(desktop_skus),
                "laptop_compliance_score": round(laptop_avg, 1),
                "desktop_compliance_score": round(desktop_avg, 1),
                "brand_compliance_score": brand_compliance_score,
                "compliance_grade": grade,
                "weighting_formula": "85% Laptop + 15% Desktop",
                "skus": ret_skus
            }

        # Overall Program Benchmark Rollup
        all_laptop_scores = [s["sku_score"] for s in sku_audit_records if s["form_factor"] == "Laptop"]
        all_desktop_scores = [s["sku_score"] for s in sku_audit_records if s["form_factor"] == "Desktop"]
        prog_laptop_avg = statistics.mean(all_laptop_scores) if all_laptop_scores else 0.0
        prog_desktop_avg = statistics.mean(all_desktop_scores) if all_desktop_scores else 0.0
        program_compliance_score = round((0.85 * prog_laptop_avg) + (0.15 * prog_desktop_avg), 1)

        return {
            "program_compliance_score": program_compliance_score,
            "laptop_average_score": round(prog_laptop_avg, 1),
            "desktop_average_score": round(prog_desktop_avg, 1),
            "flag_pass_rates": flag_pass_rates,
            "retailer_scorecards": retailer_scorecards,
            "sku_audit_records": sku_audit_records
        }
