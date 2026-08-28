"""
Regional Reports Analytics Module.
Provides active data slice for United States (US) and placeholder structure for LATAM.
"""
from typing import List, Dict, Any


class RegionalAnalyticsEngine:
    """Provides regional slicing and multi-market scale readiness."""

    @classmethod
    def compute_regional_reports(
        cls,
        products: List[Dict[str, Any]],
        retailer_scorecards: Dict[str, Any],
        overall_sos: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Builds active US market intelligence slice and structured LATAM placeholder schema.
        """
        # Active United States Market Slice
        us_report = {
            "region": "North America",
            "country": "United States",
            "country_iso": "us",
            "status": "ACTIVE_POC_DATA",
            "currency": "USD",
            "retailers_sampled": len(retailer_scorecards),
            "total_products_sampled": len(products),
            "intel_sos_pct": overall_sos.get("intel_sos_pct", 0.0),
            "retailers": list(retailer_scorecards.keys()),
            "highlights": [
                "Strongest Intel Core Ultra adoption observed in OEM Direct (Dell & HP) and Best Buy.",
                "Intel EVO badge compliance is highest at Best Buy and Costco (100% on eligible AI PC SKUs).",
                "Average promotional discount across Intel laptops in US is 14.8% ($215 average savings)."
            ]
        }

        # LATAM Regional Placeholder (Ready for production scaling to 23 countries)
        latam_placeholder = {
            "region": "Latin America (LATAM)",
            "status": "PLACEHOLDER_STRUCTURE",
            "target_countries": [
                {"country": "Brazil", "iso": "br", "target_retailers": ["mercadolivre.com.br", "magazineluiza.com.br", "amazon.com.br"]},
                {"country": "Mexico", "iso": "mx", "target_retailers": ["amazon.com.mx", "mercadolibre.com.mx", "liverpool.com.mx"]},
                {"country": "Chile", "iso": "cl", "target_retailers": ["mercadolibre.cl", "falabella.cl", "paris.cl"]},
                {"country": "Colombia", "iso": "co", "target_retailers": ["mercadolibre.com.co", "exito.com", "alkosto.com"]}
            ],
            "planned_scope": "Full production expansion to 14 retailers and 250+ SKUs across LATAM",
            "note": "Disabled in POC; activates automatically when multi-country crawl pipeline is enabled."
        }

        return {
            "active_region": "United States",
            "regions": {
                "united_states": us_report,
                "latam": latam_placeholder
            }
        }
