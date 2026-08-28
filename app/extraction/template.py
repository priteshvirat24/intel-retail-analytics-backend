"""
Deterministic Structural Product Template Identifier.
Computes a stable template ID and signature from DOM structural layout rather than URL strings.
"""
import hashlib
from typing import Optional, Dict, Any, List
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field


class TemplateProfile(BaseModel):
    """Detailed structural template analysis profile."""
    template_id: str
    template_signature: str
    framework_detected: Optional[str] = None
    schema_types: List[str] = Field(default_factory=list)
    extraction_sources: List[str] = Field(default_factory=list)
    has_jsonld: bool = False
    has_microdata: bool = False
    has_opengraph: bool = False
    has_cart_form: bool = False


class ProductTemplateIdentifier:
    """Derives a deterministic product template ID and signature from HTML structural characteristics."""

    @classmethod
    def analyze_template(cls, html: str) -> TemplateProfile:
        if not html or len(html.strip()) < 50:
            return TemplateProfile(
                template_id="tmpl_empty_shell",
                template_signature="empty_shell",
                framework_detected="none"
            )

        try:
            soup = BeautifulSoup(html, "html.parser")
        except Exception:
            return TemplateProfile(
                template_id="tmpl_unparseable_html",
                template_signature="unparseable",
                framework_detected="unknown"
            )

        structural_features: List[str] = []
        schema_types: List[str] = []
        extraction_sources: List[str] = []
        framework_detected = "vanilla_html"

        # 1. Structured data types present
        json_lds = soup.find_all("script", type="application/ld+json")
        has_jsonld = bool(json_lds)
        if json_lds:
            structural_features.append(f"jsonld_count:{len(json_lds)}")
            extraction_sources.append("JSON_LD")
            for j in json_lds[:3]:
                txt = j.string or ""
                if '"@type"' in txt:
                    for t in ["Product", "Offer", "AggregateOffer", "Brand", "BreadcrumbList", "ItemPage"]:
                        if f'"{t}"' in txt and t not in schema_types:
                            schema_types.append(t)

        if soup.find("script", id="__NEXT_DATA__"):
            structural_features.append("has_next_data")
            framework_detected = "nextjs"
            extraction_sources.append("EMBEDDED_NEXT_DATA")
        elif soup.find("script", id="__NUXT_DATA__") or soup.find("script", id="__NUXT__"):
            structural_features.append("has_nuxt_data")
            framework_detected = "nuxtjs"
            extraction_sources.append("EMBEDDED_NUXT_DATA")
        elif soup.find("div", id="root") or soup.find("div", id="app"):
            framework_detected = "spa_shell"

        has_microdata = bool(soup.find(attrs={"itemscope": True, "itemtype": True}))
        if has_microdata:
            structural_features.append("has_microdata")
            extraction_sources.append("MICRODATA")

        # 2. Key structural container hierarchy
        main_tags = []
        for tag in ["main", "article", "section", "div"]:
            containers = soup.find_all(tag, limit=10)
            for c in containers:
                c_id = c.get("id", "")
                c_class = ".".join(c.get("class", [])) if c.get("class") else ""
                if any(kw in (c_id + c_class).lower() for kw in ["product", "item", "pdp", "detail", "catalog", "sku"]):
                    main_tags.append(f"{tag}#{c_id}.{c_class}")

        if main_tags:
            structural_features.append("containers:" + ",".join(sorted(main_tags[:5])))

        # 3. Meta OpenGraph tags presence
        og_tags = sorted([
            m.get("property", "") for m in soup.find_all("meta", property=True)
            if m.get("property", "").startswith("og:") or m.get("property", "").startswith("product:")
        ])
        has_og = bool(og_tags)
        if og_tags:
            structural_features.append("og:" + ",".join(og_tags[:6]))
            extraction_sources.append("OPENGRAPH")

        # 4. Form / cart elements
        has_cart = False
        forms = soup.find_all("form")
        for f in forms:
            f_action = f.get("action", "")
            if any(kw in f_action.lower() for kw in ["cart", "basket", "buy", "checkout"]):
                structural_features.append(f"cart_form:{f_action[:30]}")
                has_cart = True
                break

        if not structural_features:
            tag_counts = f"div:{len(soup.find_all('div'))}_p:{len(soup.find_all('p'))}_span:{len(soup.find_all('span'))}"
            structural_features.append(tag_counts)

        signature = "|".join(structural_features)
        sig_hash = hashlib.sha256(signature.encode("utf-8")).hexdigest()[:12]

        prefix = "tmpl_generic"
        if framework_detected == "nextjs":
            prefix = "tmpl_nextjs"
        elif framework_detected == "nuxtjs":
            prefix = "tmpl_nuxtjs"
        elif has_jsonld:
            prefix = "tmpl_jsonld"
        elif has_microdata:
            prefix = "tmpl_microdata"
        elif has_og:
            prefix = "tmpl_opengraph"

        template_id = f"{prefix}_{sig_hash}"

        return TemplateProfile(
            template_id=template_id,
            template_signature=signature,
            framework_detected=framework_detected,
            schema_types=schema_types,
            extraction_sources=extraction_sources,
            has_jsonld=has_jsonld,
            has_microdata=has_microdata,
            has_opengraph=has_og,
            has_cart_form=has_cart
        )

    @classmethod
    def identify_template(cls, html: str) -> str:
        """Backward-compatible helper returning string template ID."""
        profile = cls.analyze_template(html)
        return profile.template_id
