from fastapi import FastAPI, Response, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
import asyncio
from typing import Dict, Any

app = FastAPI(title="Mock Retailer Ecommerce Server")

# Simulated state for rate limiting tests
_request_counts: Dict[str, int] = {}


@app.get("/sitemap.xml")
async def get_sitemap():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for i in range(1, 21):
        xml_content += f"  <url><loc>http://127.0.0.1:8765/product/sku_{i:03d}</loc></url>\n"
    xml_content += "</urlset>"
    return Response(content=xml_content, media_type="application/xml")


@app.get("/category/laptops")
async def get_category():
    links_html = "".join([f'<li><a href="/product/sku_{i:03d}">Product SKU {i:03d}</a></li>' for i in range(1, 21)])
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Laptops Category</title></head>
    <body>
      <h1>Laptop Category Listing</h1>
      <ul>{links_html}</ul>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/product/{sku_id}")
async def get_product(sku_id: str, request: Request):
    idx_str = sku_id.replace("sku_", "")
    try:
        idx = int(idx_str)
    except ValueError:
        idx = 1

    # SKU 018: Simulate 404 Not Found
    if idx == 18:
        return HTMLResponse(content="<h1>404 Not Found</h1><p>Product does not exist.</p>", status_code=404)

    # SKU 019: Simulate CAPTCHA block
    if idx == 19:
        return HTMLResponse(content="""
        <html><head><title>Robot Check</title></head>
        <body>
          <h1>Please verify you are a human</h1>
          <div class="g-recaptcha" data-sitekey="xyz"></div>
          <p>Type the characters you see in this image to continue.</p>
        </body></html>
        """, status_code=403)

    # SKU 020: Simulate Rate Limiting (429) on first attempt, then success on retry
    if idx == 20:
        count = _request_counts.get(sku_id, 0)
        _request_counts[sku_id] = count + 1
        if count == 0:
            return HTMLResponse(content="<h1>429 Too Many Requests</h1><p>Rate limit exceeded.</p>", status_code=429)

    # SKU 001 - 005: Schema.org JSON-LD Products
    if idx <= 5:
        price = 899.99 + (idx * 50)
        json_ld = f"""{{
          "@context": "https://schema.org/",
          "@type": "Product",
          "name": "UltraBook Pro Laptop 15-inch - Model {idx}",
          "image": ["https://images.example.com/laptop-{idx}.jpg"],
          "description": "High performance laptop with 16GB RAM and 512GB SSD for professional computing.",
          "sku": "{sku_id}",
          "gtin13": "123456789012{idx % 10}",
          "brand": {{
            "@type": "Brand",
            "name": "TechCorp"
          }},
          "offers": {{
            "@type": "Offer",
            "price": "{price:.2f}",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "seller": {{
              "@type": "Organization",
              "name": "TechCorp Direct"
            }}
          }},
          "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.7",
            "reviewCount": "128"
          }}
        }}"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>UltraBook Pro Laptop 15-inch - Model {idx} | MockStore</title>
          <script type="application/ld+json">{json_ld}</script>
        </head>
        <body>
          <h1>UltraBook Pro Laptop 15-inch - Model {idx}</h1>
          <span class="price">${price:.2f}</span>
          <div class="stock">In Stock</div>
        </body>
        </html>
        """
        return HTMLResponse(content=html)

    # SKU 006 - 010: Next.js __NEXT_DATA__ Embedded State
    elif idx <= 10:
        price = 1199.00 + (idx * 30)
        next_data = f"""{{
          "props": {{
            "pageProps": {{
              "initialData": {{
                "product": {{
                  "id": "{sku_id}",
                  "name": "Gaming Monitor 27-inch 165Hz - Edition {idx}",
                  "brand": "AeroView",
                  "shortDescription": "IPS QHD Gaming Display with 1ms response time and G-Sync compatible.",
                  "priceInfo": {{
                    "currentPrice": {{
                      "price": {price:.2f},
                      "currency": "USD"
                    }}
                  }},
                  "inventoryStatus": "InStock",
                  "allImages": [{{"url": "https://images.example.com/mon-{idx}.jpg"}}]
                }}
              }}
            }}
          }}
        }}"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Gaming Monitor 27-inch 165Hz | MockStore</title>
          <script id="__NEXT_DATA__" type="application/json">{next_data}</script>
        </head>
        <body>
          <div id="__next"></div>
        </body>
        </html>
        """
        return HTMLResponse(content=html)

    # SKU 011 - 015: OpenGraph & DOM Products
    elif idx <= 15:
        price = 199.99 + (idx * 15)
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Wireless ANC Headphones HD-{idx} | MockStore</title>
          <meta property="og:title" content="Wireless ANC Headphones HD-{idx}" />
          <meta property="og:description" content="Active noise cancelling wireless headphones with 40-hour battery life." />
          <meta property="og:price:amount" content="{price:.2f}" />
          <meta property="og:price:currency" content="USD" />
          <meta property="og:availability" content="instock" />
          <meta property="product:brand" content="AudioMax" />
          <meta property="og:image" content="https://images.example.com/audio-{idx}.jpg" />
        </head>
        <body>
          <h1 class="product-title">Wireless ANC Headphones HD-{idx}</h1>
          <div class="product-price">${price:.2f}</div>
          <span class="stock-status">In Stock</span>
          <div class="product-description">Active noise cancelling wireless headphones with 40-hour battery life.</div>
        </body>
        </html>
        """
        return HTMLResponse(content=html)

    # SKU 016 - 017: Out of stock or missing fields
    else:
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Discontinued Accessory Kit {idx} | MockStore</title>
        </head>
        <body>
          <h1 id="productTitle">Discontinued Accessory Kit {idx}</h1>
          <span id="availability"><span>Currently Unavailable</span></span>
          <div id="productDescription">This product has been discontinued and is no longer for sale.</div>
        </body>
        </html>
        """
        return HTMLResponse(content=html)


def run_mock_server_in_thread():
    """Runs mock server in a background thread."""
    import threading
    config = uvicorn.Config(app, host="127.0.0.1", port=8765, log_level="error")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    return server
