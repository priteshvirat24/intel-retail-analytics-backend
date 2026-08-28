"""
Audit Flag & Brand Compliance Extractor for PC-Industry Intelligence.
Derives S1, S2, P1, P2, P3, P4, P5 flags from listing and PDP text/HTML.
"""
import re
from typing import Dict, Any, Tuple


class AuditFlagExtractor:
    """Extracts compliance flags and calculates SKU audit scores."""

    INTEL_KEYWORDS = [
        "intel", "intel core", "intel core ultra", "core ultra", "core i3", "core i5",
        "core i7", "core i9", "ultra 5", "ultra 7", "ultra 9", "intel vpro", "intel evo"
    ]
    
    COMPETITOR_KEYWORDS = [
        "amd", "ryzen", "ryzen 5", "ryzen 7", "ryzen 9", "radeon", "apple", "m2", "m3",
        "m4", "snapdragon", "snapdragon x", "qualcomm", "arm cortex"
    ]

    EVO_BADGE_PATTERNS = [
        r"intel\s*evo", r"evo\s*edition", r"evo\s*platform", r"powered\s*by\s*evo",
        r"badge[_-]?evo", r"intel-evo-badge"
    ]

    INTEL_BADGE_PATTERNS = [
        r"intel\s*inside", r"intel\s*core\s*ultra", r"intel\s*core", r"intel\s*vpro",
        r"intel_badge", r"badge-intel"
    ]

    INTEL_RICH_MEDIA_PATTERNS = [
        r"aplus-v2", r"intel-feature-module", r"intel_rich_media", r"intel-aplus",
        r"intel\s*npu\s*ai", r"intel\s*arc\s*graphics", r"intel\s*smart\s*cache",
        r"intel-brand-story", r"intel-hero-banner"
    ]

    OEM_RICH_MEDIA_PATTERNS = [
        r"vjs-tech", r"video-player", r"html5-video", r"360-view", r"interactive-viewer",
        r"thermal-design-module", r"oem-showcase", r"hp-rich-media", r"dell-module"
    ]

    @classmethod
    def evaluate_audit_flags(
        cls,
        listing_title: str,
        listing_html: str,
        pdp_title: str,
        pdp_html: str,
        specs: Dict[str, Any],
        is_intel_cpu: bool
    ) -> Dict[str, Any]:
        """
        Derives all 7 audit flags with pass/fail boolean, mention types, and diagnostic evidence.
        """
        listing_text = f"{listing_title} {listing_html}".lower()
        pdp_text = f"{pdp_title} {pdp_html}".lower()
        
        # -------------------------------------------------------------
        # S1: Listing page title mentions
        # -------------------------------------------------------------
        s1_mentions = []
        lt_lower = listing_title.lower()
        for kw in ["intel core ultra", "core ultra", "intel core", "intel", "core i9", "core i7", "core i5", "core i3"]:
            if kw in lt_lower and kw not in s1_mentions:
                s1_mentions.append(kw)
        
        s1_comp_mentions = []
        for kw in cls.COMPETITOR_KEYWORDS:
            if kw in lt_lower and kw not in s1_comp_mentions:
                s1_comp_mentions.append(kw)

        s1_pass = bool(s1_mentions) if is_intel_cpu else bool(s1_comp_mentions)

        # -------------------------------------------------------------
        # S2: Listing badge presence
        # -------------------------------------------------------------
        s2_badges = []
        for pat in cls.EVO_BADGE_PATTERNS + cls.INTEL_BADGE_PATTERNS:
            if re.search(pat, listing_text):
                s2_badges.append(pat.replace("\\s*", " ").replace("\\", ""))
        s2_pass = bool(s2_badges) if is_intel_cpu else False

        # -------------------------------------------------------------
        # P1: PDP product title mentions
        # -------------------------------------------------------------
        p1_mentions = []
        pt_lower = pdp_title.lower()
        for kw in ["intel core ultra", "core ultra", "intel core", "intel", "core i9", "core i7", "core i5"]:
            if kw in pt_lower and kw not in p1_mentions:
                p1_mentions.append(kw)
        p1_pass = bool(p1_mentions) if is_intel_cpu else True

        # -------------------------------------------------------------
        # P2: PDP badge presence
        # -------------------------------------------------------------
        p2_badges = []
        for pat in cls.EVO_BADGE_PATTERNS + cls.INTEL_BADGE_PATTERNS:
            if re.search(pat, pdp_text):
                p2_badges.append(pat.replace("\\s*", " ").replace("\\", ""))
        p2_pass = bool(p2_badges) if is_intel_cpu else False

        # -------------------------------------------------------------
        # P3: PDP spec mentions (Processor series, generation, clockspeed)
        # -------------------------------------------------------------
        cpu_spec = specs.get("cpu", "") or specs.get("processor", "")
        p3_pass = bool(cpu_spec and len(str(cpu_spec)) > 5)

        # -------------------------------------------------------------
        # P4: Intel rich media presence (A+ content, Intel modules)
        # -------------------------------------------------------------
        p4_modules = []
        for pat in cls.INTEL_RICH_MEDIA_PATTERNS:
            if re.search(pat, pdp_text):
                p4_modules.append(pat)
        p4_pass = bool(p4_modules) if is_intel_cpu else False

        # -------------------------------------------------------------
        # P5: OEM rich media presence (videos, 360 viewer, thermals)
        # -------------------------------------------------------------
        p5_modules = []
        for pat in cls.OEM_RICH_MEDIA_PATTERNS:
            if re.search(pat, pdp_text):
                p5_modules.append(pat)
        p5_pass = bool(p5_modules) or ("<video" in pdp_html.lower())

        # Calculate SKU-level compliance percentage (0 to 100)
        # For Intel SKUs, score all 7 flags; for competitors, standard baseline
        flags_bool = [s1_pass, s2_pass, p1_pass, p2_pass, p3_pass, p4_pass, p5_pass]
        sku_audit_score = round((sum(flags_bool) / len(flags_bool)) * 100, 1)

        return {
            "S1": {
                "pass": s1_pass,
                "label": "Listing Title Mention",
                "intel_mentions": s1_mentions,
                "competitor_mentions": s1_comp_mentions
            },
            "S2": {
                "pass": s2_pass,
                "label": "Listing Badge Presence",
                "detected_badges": list(set(s2_badges))
            },
            "P1": {
                "pass": p1_pass,
                "label": "PDP Title Mention",
                "intel_mentions": p1_mentions
            },
            "P2": {
                "pass": p2_pass,
                "label": "PDP Badge Presence",
                "detected_badges": list(set(p2_badges))
            },
            "P3": {
                "pass": p3_pass,
                "label": "PDP Spec Precision",
                "detected_cpu_spec": cpu_spec
            },
            "P4": {
                "pass": p4_pass,
                "label": "Intel Rich Media (A+ / Infographics)",
                "detected_modules": p4_modules
            },
            "P5": {
                "pass": p5_pass,
                "label": "OEM Rich Media (Videos / 360)",
                "detected_modules": p5_modules
            },
            "sku_audit_score": sku_audit_score,
            "all_flags_pass": all(flags_bool)
        }
