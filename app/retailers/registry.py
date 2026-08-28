from typing import Dict, Type, Optional
from app.retailers.base_adapter import BaseRetailerAdapter
from app.retailers.amazon import AmazonAdapter
from app.retailers.flipkart import FlipkartAdapter
from app.retailers.walmart import WalmartAdapter
from app.retailers.bestbuy import BestBuyAdapter
from app.retailers.mercadolibre import MercadoLibreAdapter
from app.retailers.mediamarkt import MediaMarktAdapter
from app.retailers.custom_generic import CustomGenericAdapter
from app.retailers.boulanger import BoulangerAdapter
from app.retailers.agres import AgresAdapter
from app.models.retailer import RetailerTargetConfig


class RetailerAdapterRegistry:
    """Registry mapping retailer targets to specialized adapters."""

    _ADAPTERS: Dict[str, Type[BaseRetailerAdapter]] = {
        "amazon": AmazonAdapter,
        "flipkart": FlipkartAdapter,
        "walmart": WalmartAdapter,
        "bestbuy": BestBuyAdapter,
        "mercadolibre": MercadoLibreAdapter,
        "mercadolivre": MercadoLibreAdapter,
        "mediamarkt": MediaMarktAdapter,
        "boulanger": BoulangerAdapter,
        "agres": AgresAdapter,
    }

    @classmethod
    def get_adapter(cls, target_config: RetailerTargetConfig) -> Optional[BaseRetailerAdapter]:
        retailer_key = target_config.retailer.lower()
        adapter_cls = cls._ADAPTERS.get(retailer_key)
        if adapter_cls:
            return adapter_cls(target_config)
        return CustomGenericAdapter(target_config)


__all__ = [
    "BaseRetailerAdapter",
    "AmazonAdapter",
    "FlipkartAdapter",
    "WalmartAdapter",
    "BestBuyAdapter",
    "MercadoLibreAdapter",
    "MediaMarktAdapter",
    "BoulangerAdapter",
    "AgresAdapter",
    "CustomGenericAdapter",
    "RetailerAdapterRegistry",
]
