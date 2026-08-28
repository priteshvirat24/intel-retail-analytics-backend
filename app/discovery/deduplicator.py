import re
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode
from typing import List, Set, Optional


class ProductDeduplicator:
    """Canonicalizes and deduplicates product URLs across diverse categories."""

    TRACKING_PARAMS = {
        "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
        "ref", "ref_", "tag", "qid", "sr", "spm", "scm", "pf_rd_r", "pf_rd_p",
        "pd_rd_r", "pd_rd_w", "pd_rd_wg", "_encoding", "psc", "smid", "th",
        "gclid", "fbclid", "_trkparms", "click_id", "session_id", "source"
    }

    # Product ID extraction regexes for common retailer families
    PRODUCT_ID_PATTERNS = [
        re.compile(r"/dp/([A-Z0-9]{10})"),                     # Amazon ASIN
        re.compile(r"/gp/product/([A-Z0-9]{10})"),            # Amazon ASIN
        re.compile(r"/site/[^/]+/([0-9]+)\.p"),               # Best Buy US SKU
        re.compile(r"/product/[^/]+/([0-9]+)"),               # Best Buy CA / Elkjop SKU
        re.compile(r"/ip/[^/]+/([0-9]+)"),                    # Walmart item ID
        re.compile(r"/ip/([0-9]+)"),                          # Walmart item ID
        re.compile(r"/p/([a-zA-Z0-9]+)"),                     # Flipkart PID / Newegg
        re.compile(r"/ref/([0-9]+)"),                         # Boulanger ref
        re.compile(r"/products/([0-9]+)"),                    # Coupang product ID
        re.compile(r"/Item\?goodscode=([0-9]+)"),             # Gmarket item ID
        re.compile(r"/(ML[A-Z]-[0-9]+)"),                     # Mercado Libre ID
        re.compile(r"/product/([0-9]+)/"),                    # Yodobashi product ID
    ]

    @classmethod
    def clean_url(cls, url: str) -> str:
        """Strip tracking parameters and clean trailing junk."""
        if not url:
            return ""
        parsed = urlparse(url)
        # Filter query params
        query_pairs = parse_qsl(parsed.query, keep_blank_values=False)
        cleaned_query = [
            (k, v) for k, v in query_pairs
            if k.lower() not in cls.TRACKING_PARAMS and not k.startswith("utm_")
        ]
        # Rebuild query
        new_query = urlencode(cleaned_query)
        # Strip fragment
        return urlunparse((
            parsed.scheme,
            parsed.netloc.lower(),
            parsed.path,
            parsed.params,
            new_query,
            ""
        ))

    @classmethod
    def extract_product_key(cls, url: str, target_config: Optional[Any] = None) -> str:
        """Extract unique product identity key from URL if identifiable, or return cleaned URL."""
        cleaned = cls.clean_url(url)
        for pattern in cls.PRODUCT_ID_PATTERNS:
            match = pattern.search(cleaned)
            if match:
                return match.group(1)
        return cleaned

    @classmethod
    def deduplicate(cls, urls: List[str], max_count: int = 20) -> List[str]:
        """Deduplicate a list of product URLs while preserving order and diversity."""
        seen_keys: Set[str] = set()
        deduped: List[str] = []

        for url in urls:
            if not url or not url.startswith("http"):
                continue
            cleaned = cls.clean_url(url)
            key = cls.extract_product_key(cleaned)
            if key not in seen_keys:
                seen_keys.add(key)
                deduped.append(cleaned)
                if len(deduped) >= max_count:
                    break

        return deduped
