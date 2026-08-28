import pytest
from app.extraction.jsonld import JsonLdExtractor
from app.extraction.embedded_json import EmbeddedJsonExtractor
from app.extraction.opengraph import OpenGraphExtractor
from app.extraction.dom import DomExtractor
from app.extraction.engine import ProductExtractionEngine
from app.models.retailer import RetailerTargetConfig


@pytest.fixture
def target_config():
    return RetailerTargetConfig(
        target_id="test-retailer",
        retailer="teststore",
        brand_name="Test Store",
        country="US",
        domain="teststore.com",
        base_url="https://teststore.com",
        locale="en-US",
        currency="USD"
    )


def test_jsonld_extraction(target_config):
    html = """
    <html>
      <head>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org/",
          "@type": "Product",
          "name": "Dell XPS 15 9530 Laptop",
          "image": ["https://example.com/img1.jpg"],
          "description": "Premium 15-inch laptop with OLED 3.5K display.",
          "sku": "XPS15-9530",
          "gtin13": "1234567890123",
          "brand": { "@type": "Brand", "name": "Dell" },
          "offers": {
            "@type": "Offer",
            "price": "1999.99",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock"
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "reviewCount": "240"
          }
        }
        </script>
      </head>
      <body></body>
    </html>
    """
    extractor = JsonLdExtractor(target_config)
    res = extractor.extract(html, "https://teststore.com/product/xps15")
    assert res is not None
    assert res["title"] == "Dell XPS 15 9530 Laptop"
    assert res["price"] == 1999.99
    assert res["currency"] == "USD"
    assert res["brand"] == "Dell"
    assert res["sku"] == "XPS15-9530"
    assert res["availability"] == "InStock"
    assert res["rating"] == 4.8
    assert res["review_count"] == 240


def test_jsonld_graph_extraction(target_config):
    html = """
    <html>
      <head>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@graph": [
            { "@type": "WebSite", "name": "Store" },
            {
              "@type": "Product",
              "name": "Sony WH-1000XM5 Headphones",
              "sku": "SONY-XM5",
              "offers": { "@type": "Offer", "price": "399.00", "priceCurrency": "USD" }
            }
          ]
        }
        </script>
      </head>
    </html>
    """
    extractor = JsonLdExtractor(target_config)
    res = extractor.extract(html, "https://teststore.com/p/sony-xm5")
    assert res is not None
    assert res["title"] == "Sony WH-1000XM5 Headphones"
    assert res["price"] == 399.0
    assert res["sku"] == "SONY-XM5"


def test_embedded_next_data_extraction(target_config):
    html = """
    <html>
      <head>
        <script id="__NEXT_DATA__" type="application/json">
        {
          "props": {
            "pageProps": {
              "initialData": {
                "product": {
                  "id": "ASUS-ROG-4090",
                  "name": "ASUS ROG Zephyrus G16",
                  "brand": "ASUS",
                  "shortDescription": "Intel Core Ultra 9 with RTX 4090",
                  "priceInfo": { "currentPrice": { "price": 2899.99, "currency": "USD" } },
                  "inventoryStatus": "InStock"
                }
              }
            }
          }
        }
        </script>
      </head>
    </html>
    """
    extractor = EmbeddedJsonExtractor(target_config)
    res = extractor.extract(html, "https://teststore.com/asus-g16")
    assert res is not None
    assert res["title"] == "ASUS ROG Zephyrus G16"
    assert res["price"] == 2899.99
    assert res["brand"] == "ASUS"
    assert res["sku"] == "ASUS-ROG-4090"


def test_opengraph_extraction(target_config):
    html = """
    <html>
      <head>
        <meta property="og:title" content="Samsung Galaxy Tab S9 Ultra" />
        <meta property="og:description" content="14.6-inch Dynamic AMOLED 2X tablet." />
        <meta property="og:price:amount" content="1199.99" />
        <meta property="og:price:currency" content="USD" />
        <meta property="og:availability" content="instock" />
        <meta property="og:image" content="https://example.com/tab-s9.jpg" />
        <meta property="product:brand" content="Samsung" />
      </head>
    </html>
    """
    extractor = OpenGraphExtractor(target_config)
    res = extractor.extract(html, "https://teststore.com/tab-s9")
    assert res is not None
    assert res["title"] == "Samsung Galaxy Tab S9 Ultra"
    assert res["price"] == 1199.99
    assert res["currency"] == "USD"
    assert res["brand"] == "Samsung"
    assert res["availability"] == "InStock"


def test_product_extraction_engine_coordination(target_config):
    html = """
    <html>
      <head>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org/",
          "@type": "Product",
          "name": "Apple Watch Ultra 2",
          "sku": "WATCH-U2",
          "offers": { "@type": "Offer", "price": "799.00", "priceCurrency": "USD", "availability": "https://schema.org/InStock" }
        }
        </script>
      </head>
      <body>
        <h1 class="product-title">Apple Watch Ultra 2 GPS + Cellular</h1>
      </body>
    </html>
    """
    engine = ProductExtractionEngine(target_config)
    product, err = engine.extract_product(html, "https://teststore.com/watch-u2", crawler_strategy="HTTP")
    assert err is None
    assert product is not None
    assert product.title == "Apple Watch Ultra 2"
    assert product.price == 799.0
    assert product.validation.is_valid_sku is True
    assert product.validation.field_completeness >= 0.5
    assert product.validation.field_validity == 1.0
