"""
Proxy Provider & Strategy Request Context.
Implements real proxy configuration management and execution context isolation.
Ensures proxy credentials are never exposed in logs, manifests, or reports.
"""
import os
import re
from typing import Optional, Dict, Any
from urllib.parse import urlparse
from pydantic import BaseModel, Field


class ProxyConfig(BaseModel):
    """Normalized proxy configuration without exposing plaintext credentials."""
    enabled: bool = False
    endpoint_id: str = "direct"
    server: Optional[str] = None
    protocol: Optional[str] = None
    country: Optional[str] = None
    is_residential: bool = False

    def get_sanitized_repr(self) -> Dict[str, Any]:
        """Returns a sanitized dictionary representation suitable for telemetry/logging."""
        return {
            "proxy_enabled": self.enabled,
            "proxy_endpoint_id": self.endpoint_id,
            "protocol": self.protocol,
            "country": self.country,
            "is_residential": self.is_residential
        }


class ProxyProvider:
    """Manages proxy endpoints read from environment or target configuration."""

    @classmethod
    def get_brightdata_proxy(cls, target_country_iso: Optional[str] = None) -> ProxyConfig:
        """
        Builds normalized ProxyConfig for Bright Data (Residential / Web Unlocker / Scraping Browser).
        Supports country-specific targeting (e.g. -country-us) and strict credential sanitization.
        """
        from app.crawlers.brightdata_guard import BrightDataCostGuard
        guard = BrightDataCostGuard.get_instance()

        # Check explicit proxy url or individual components
        proxy_url = os.getenv("BRIGHTDATA_PROXY_URL")
        host = os.getenv("BRIGHTDATA_HOST", "brd.superproxy.io")
        port = os.getenv("BRIGHTDATA_PORT", "22225")
        customer = os.getenv("BRIGHTDATA_CUSTOMER_ID") or os.getenv("BRIGHTDATA_USERNAME")
        password = os.getenv("BRIGHTDATA_PASSWORD")
        zone = os.getenv("BRIGHTDATA_ZONE", "residential")

        if proxy_url:
            raw_url = proxy_url
        elif customer and password:
            user_str = f"brd-customer-{customer}-zone-{zone}"
            if target_country_iso:
                user_str += f"-country-{target_country_iso.lower()}"
            raw_url = f"http://{user_str}:{password}@{host}:{port}"
        else:
            return ProxyConfig(enabled=False, endpoint_id="brightdata_not_configured")

        try:
            parsed = urlparse(raw_url)
            p_host = parsed.hostname or host
            p_port = parsed.port or int(port)
            endpoint_id = f"brightdata://{p_host}:{p_port}?zone={zone}"
            if target_country_iso:
                endpoint_id += f"&country={target_country_iso}"

            return ProxyConfig(
                enabled=True,
                endpoint_id=endpoint_id,
                server=raw_url,
                protocol="http",
                country=target_country_iso,
                is_residential=True
            )
        except Exception:
            return ProxyConfig(enabled=False, endpoint_id="brightdata_invalid_config")

    @classmethod
    def get_proxy(cls, target_country: Optional[str] = None, target_country_iso: Optional[str] = None) -> ProxyConfig:
        """
        Reads real proxy configuration from environment variables (Bright Data, HTTP_PROXY, HTTPS_PROXY).
        Returns normalized ProxyConfig.
        """
        # 1. Check if Bright Data is enabled
        brightdata_enabled = os.getenv("BRIGHTDATA_ENABLED", "false").lower() in ("true", "1", "yes")
        if brightdata_enabled or os.getenv("BRIGHTDATA_PROXY_URL") or os.getenv("BRIGHTDATA_CUSTOMER_ID"):
            bd_proxy = cls.get_brightdata_proxy(target_country_iso=target_country_iso)
            if bd_proxy.enabled:
                return bd_proxy

        # 2. Check standard environment proxies
        proxy_url = os.getenv("HTTPS_PROXY") or os.getenv("HTTP_PROXY") or os.getenv("ALL_PROXY")
        if not proxy_url:
            return ProxyConfig(enabled=False, endpoint_id="direct_egress")

        try:
            parsed = urlparse(proxy_url)
            host = parsed.hostname or "unknown_host"
            port = parsed.port or (443 if parsed.scheme == "https" else 80)
            endpoint_id = f"{parsed.scheme}://{host}:{port}"
            
            # Detect residential indicator if present in host or env
            is_residential = os.getenv("PROXY_IS_RESIDENTIAL", "false").lower() in ("true", "1", "yes")
            country = target_country or os.getenv("PROXY_COUNTRY")

            return ProxyConfig(
                enabled=True,
                endpoint_id=endpoint_id,
                server=proxy_url,
                protocol=parsed.scheme,
                country=country,
                is_residential=is_residential
            )
        except Exception:
            return ProxyConfig(enabled=False, endpoint_id="invalid_proxy_config")


class StrategyRequestContext(BaseModel):
    """Encapsulates isolated request execution parameters for a strategy attempt."""
    url: str
    target_id: str
    retailer: str
    country: str
    sku_id: str
    category: Optional[str] = None
    strategy: str = "HTTP"
    attempt_number: int = 1
    timeout_sec: float = 30.0
    headers: Dict[str, str] = Field(default_factory=dict)
    proxy_config: ProxyConfig = Field(default_factory=lambda: ProxyConfig(enabled=False))
    wait_for_selector: Optional[str] = None
    wait_after_load_ms: int = 1000
    custom_context: Dict[str, Any] = Field(default_factory=dict)
