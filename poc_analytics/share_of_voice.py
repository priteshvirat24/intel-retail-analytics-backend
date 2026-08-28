"""
Share of Voice (Search) (SOV) Analytics Engine.
Analyzes 10 sample search keywords, organic & sponsored visibility, and top-2-page audit compliance.
"""
from typing import List, Dict, Any
import statistics


class ShareOfVoiceEngine:
    """Computes Share of Voice (SOV) metrics across sample search keywords and search audit compliance."""

    @classmethod
    def compute_share_of_voice(cls, sov_searches: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Processes keyword-level search metrics, rankings, and audit compliance for top 2 search pages.
        """
        # Sort keywords highest to lowest Intel Share
        ranked_keywords = sorted(sov_searches, key=lambda x: x["intel_share_pct"], reverse=True)
        
        for idx, k in enumerate(ranked_keywords, 1):
            k["intel_rank"] = idx

        overall_intel_share_avg = round(statistics.mean([k["intel_share_pct"] for k in ranked_keywords]), 1)
        overall_sponsored_share_avg = round(statistics.mean([k["sponsored_intel_share_pct"] for k in ranked_keywords]), 1)
        top2_audit_scores_avg = round(statistics.mean([k["top2_page_audit"]["score"] for k in ranked_keywords]), 1)

        return {
            "total_keywords_analyzed": len(ranked_keywords),
            "average_intel_sov_pct": overall_intel_share_avg,
            "average_sponsored_sov_pct": overall_sponsored_share_avg,
            "average_top2_search_audit_score": top2_audit_scores_avg,
            "ranked_keywords": ranked_keywords
        }
