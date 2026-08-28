import pytest
from app.adapters.amazon import AmazonAdapter
from app.adapters.boulanger import BoulangerAdapter
from app.models.retailer import RetailerTargetConfig


@pytest.fixture
def amazon_config():
    return RetailerTargetConfig(
        target_id="amazon-de",
        retailer="amazon",
        brand_name="Amazon",
        base_url="https://www.amazon.de",
        country="Germany",
        iso_country="DE",
        domain="amazon.de",
        locale="de-DE",
        currency="EUR",
        timezone="Europe/Berlin",
        discovery_methods=[],
        category_seeds=[],
        sitemap_urls=[],
        seed_urls=[],
        max_concurrency=1,
        rate_limit=1.0
    )


@pytest.fixture
def boulanger_config():
    return RetailerTargetConfig(
        target_id="boulanger-fr",
        retailer="boulanger",
        brand_name="Boulanger",
        base_url="https://www.boulanger.com",
        country="France",
        iso_country="FR",
        domain="boulanger.com",
        locale="fr-FR",
        currency="EUR",
        timezone="Europe/Paris",
        discovery_methods=[],
        category_seeds=[],
        sitemap_urls=[],
        seed_urls=[],
        max_concurrency=1,
        rate_limit=1.0
    )


# -------------------------------------------------------------
# Amazon Adapter Tests
# -------------------------------------------------------------

def test_amazon_adapter_valid_product(amazon_config):
    html = """
    <html>
      <head><title>Apple iPad 10.2 - Amazon.de</title></head>
      <body>
        <span id="productTitle">Apple iPad 10.2 Zoll (64GB) Space Grau</span>
        <div id="bylineInfo">Brand: Apple</div>
        <div id="corePrice_desktop">
          <span class="a-price"><span class="a-offscreen">349,00 €</span></span>
        </div>
        <div id="availability"><span class="a-color-base">Auf Lager.</span></div>
        <div id="productDescription"><p>Neues Apple iPad mit A13 Bionic Chip und Retina Display.</p></div>
        <div id="landingImage" data-old-hires="https://m.media-amazon.com/images/I/ipad.jpg"></div>
      </body>
    </html>
    """
    adapter = AmazonAdapter(amazon_config)
    res = adapter.extract_custom(html, "https://www.amazon.de/dp/B09G9FPHY6")
    assert res is not None
    assert res["sku"] == "B09G9FPHY6"
    assert "Apple iPad" in res["title"]
    assert res["brand"] == "Apple"
    assert res["price"] == 349.0
    assert res["currency"] == "EUR"
    assert res["availability"] == "InStock"
    assert "https://m.media-amazon.com/images/I/ipad.jpg" in res["image_urls"]


def test_amazon_adapter_missing_price_out_of_stock(amazon_config):
    html = """
    <html>
      <body>
        <h1 id="productTitle">Vintage Retro Radio</h1>
        <div id="bylineInfo">Brand: RetroSound</div>
        <div id="availability"><span class="primary-availability-message">Derzeit nicht verfügbar.</span></div>
      </body>
    </html>
    """
    adapter = AmazonAdapter(amazon_config)
    res = adapter.extract_custom(html, "https://www.amazon.de/dp/B000123456")
    assert res is not None
    assert res["sku"] == "B000123456"
    assert res.get("price") is None
    assert res["availability"] == "OutOfStock"


def test_amazon_adapter_invalid_price(amazon_config):
    html = """
    <html>
      <body>
        <span id="productTitle">Gadget XYZ</span>
        <div class="a-price"><span class="a-offscreen">Free / N/A</span></div>
      </body>
    </html>
    """
    adapter = AmazonAdapter(amazon_config)
    res = adapter.extract_custom(html, "https://www.amazon.de/dp/B000INVALID")
    assert res is not None
    assert res.get("price") is None  # Does not fabricate price from non-numeric string


def test_amazon_adapter_missing_optional_field(amazon_config):
    html = """
    <html>
      <body>
        <span id="productTitle">Generic HDMI Cable 2m</span>
        <span class="a-price"><span class="a-offscreen">9,99 €</span></span>
      </body>
    </html>
    """
    adapter = AmazonAdapter(amazon_config)
    res = adapter.extract_custom(html, "https://www.amazon.de/dp/B000CABLE1")
    assert res is not None
    assert res["price"] == 9.99
    assert "brand" not in res
    assert "description" not in res


def test_amazon_adapter_different_product_type(amazon_config):
    html = """
    <html>
      <body>
        <span id="productTitle">Sony WH-1000XM5 Wireless Noise Cancelling Headphones</span>
        <div id="bylineInfo">Visit the Sony Store</div>
        <span class="a-price"><span class="a-offscreen">379,99 €</span></span>
        <span id="acrCustomerReviewText">1.450 Sternebewertungen</span>
      </body>
    </html>
    """
    adapter = AmazonAdapter(amazon_config)
    res = adapter.extract_custom(html, "https://www.amazon.de/dp/B09XS7JWHH")
    assert res is not None
    assert res["sku"] == "B09XS7JWHH"
    assert res["brand"] == "Sony Store"
    assert res["price"] == 379.99
    assert res["review_count"] == 1450


# -------------------------------------------------------------
# Boulanger Adapter Tests
# -------------------------------------------------------------

def test_boulanger_adapter_valid_product(boulanger_config):
    html = """
    <html>
      <head><title>Machine à café DeLonghi - Boulanger</title></head>
      <body>
        <h1 class="product-title" itemprop="name">Expresso avec broyeur DeLonghi Magnifica S</h1>
        <span class="brand-name" itemprop="brand">DeLonghi</span>
        <div class="price__amount" itemprop="price">299,99 €</div>
        <div class="stock-status" itemprop="availability">En stock</div>
        <span itemprop="sku">1098234</span>
        <div class="product-image"><img itemprop="image" src="https://image.boulanger.com/delonghi.jpg" /></div>
        <div class="product-description" itemprop="description">Machine expresso compacte avec buse vapeur.</div>
      </body>
    </html>
    """
    adapter = BoulangerAdapter(boulanger_config)
    res = adapter.extract_custom(html, "https://www.boulanger.com/ref/1098234")
    assert res is not None
    assert res["sku"] == "1098234"
    assert "DeLonghi" in res["title"]
    assert res["brand"] == "DeLonghi"
    assert res["price"] == 299.99
    assert res["currency"] == "EUR"
    assert res["availability"] == "InStock"
    assert res["image_urls"] == ["https://image.boulanger.com/delonghi.jpg"]


def test_boulanger_adapter_missing_price_out_of_stock(boulanger_config):
    html = """
    <html>
      <body>
        <h1 class="product-title">Console PlayStation 5 Slim Edition</h1>
        <span class="brand-name">Sony</span>
        <div class="stock-status">Rupture de stock</div>
      </body>
    </html>
    """
    adapter = BoulangerAdapter(boulanger_config)
    res = adapter.extract_custom(html, "https://www.boulanger.com/ref/1199999")
    assert res is not None
    assert res.get("price") is None
    assert res["availability"] == "OutOfStock"


def test_boulanger_adapter_missing_optional_fields(boulanger_config):
    html = """
    <html>
      <body>
        <h1 class="product-title">Câble USB-C 1m</h1>
        <div class="price__amount">12,99 €</div>
      </body>
    </html>
    """
    adapter = BoulangerAdapter(boulanger_config)
    res = adapter.extract_custom(html, "https://www.boulanger.com/ref/8001001")
    assert res is not None
    assert res["price"] == 12.99
    assert "brand" not in res
    assert "description" not in res
    assert res["sku"] == "8001001"
