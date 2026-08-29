"""
Intel Retail Competitive Intelligence & Crawl API Server
Production FastAPI Backend connecting to Neon PostgreSQL.
"""
import os
import sys
import json
import logging
from typing import Optional, List, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import asyncpg
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("intel_api")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_Ii6SfwKHJA7B@ep-fancy-waterfall-a5fta2du.us-east-2.aws.neon.tech/neondb?sslmode=require"
)

# Connection Pool Holder
db_pool: Optional[asyncpg.Pool] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global db_pool
    logger.info("Initializing Neon PostgreSQL connection pool...")
    try:
        db_pool = await asyncpg.create_pool(
            dsn=DATABASE_URL,
            min_size=2,
            max_size=10,
            command_timeout=30.0,
            ssl="require" if "sslmode=require" in DATABASE_URL else None
        )
        logger.info("Neon PostgreSQL connection pool established successfully.")
    except Exception as e:
        logger.error(f"Failed to connect to Neon PostgreSQL: {e}")
        db_pool = None
    yield
    if db_pool:
        logger.info("Closing Neon PostgreSQL connection pool...")
        await db_pool.close()

app = FastAPI(
    title="Intel Retail Competitive Intelligence API",
    description="Production API providing real-time laptop catalog querying, 52-retailer coverage metrics, and audit evidence from Neon PostgreSQL.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for dashboard frontend and external consumers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_db_pool() -> asyncpg.Pool:
    if db_pool is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection pool is not available."
        )
    return db_pool

# --- Health Check ---
@app.get("/health", tags=["System"])
async def health_check():
    db_status = "DISCONNECTED"
    sku_count = 0
    retailer_count = 0
    if db_pool:
        try:
            async with db_pool.acquire() as conn:
                sku_count = await conn.fetchval("SELECT COUNT(*) FROM laptops_catalog")
                retailer_count = await conn.fetchval("SELECT COUNT(*) FROM retailer_storefronts")
                db_status = "CONNECTED"
        except Exception as e:
            db_status = f"ERROR: {str(e)}"

    return {
        "status": "healthy" if db_status == "CONNECTED" else "degraded",
        "database": db_status,
        "total_skus": sku_count,
        "total_retailers": retailer_count,
        "target_retailers_benchmark": 52,
        "engine": "Neon PostgreSQL + FastAPI",
        "timestamp": "2026-08-30T00:00:00Z"
    }

@app.get("/", tags=["System"])
async def root():
    return {
        "name": "Intel Retail Competitive Intelligence Backend",
        "status": "online",
        "docs_url": "/docs",
        "health_url": "/health"
    }

# --- Products & Catalog Endpoints ---
@app.get("/api/products", tags=["Catalog"])
async def get_products(
    search: Optional[str] = Query(None, description="Search term for title, model, processor, or retailer"),
    retailer_id: Optional[str] = Query(None, description="Filter by retailer_id"),
    country_iso: Optional[str] = Query(None, description="Filter by 2-letter country code"),
    processor: Optional[str] = Query(None, description="Filter by processor (e.g. Intel, AMD)"),
    is_intel: Optional[bool] = Query(None, description="Filter Intel-only or competitor SKUs"),
    oem: Optional[str] = Query(None, description="Filter by OEM (e.g. Lenovo, Dell, HP, ASUS, Acer)"),
    min_price: Optional[float] = Query(None, description="Minimum selling price (USD)"),
    max_price: Optional[float] = Query(None, description="Maximum selling price (USD)"),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    pool: Optional[asyncpg.Pool] = Depends(get_db_pool)
):
    db = pool if isinstance(pool, asyncpg.Pool) else await get_db_pool()
    search = search if isinstance(search, str) else None
    retailer_id = retailer_id if isinstance(retailer_id, str) else None
    country_iso = country_iso if isinstance(country_iso, str) else None
    processor = processor if isinstance(processor, str) else None
    is_intel = is_intel if isinstance(is_intel, bool) else None
    oem = oem if isinstance(oem, str) else None
    min_price = min_price if isinstance(min_price, (int, float)) else None
    max_price = max_price if isinstance(max_price, (int, float)) else None

    offset = (page - 1) * page_size
    conditions = ["1=1"]
    params = []
    idx = 1

    if search:
        conditions.append(f"(product_title ILIKE ${idx} OR model ILIKE ${idx} OR processor_model ILIKE ${idx} OR account ILIKE ${idx} OR product_id ILIKE ${idx})")
        params.append(f"%{search}%")
        idx += 1

    if retailer_id:
        conditions.append(f"retailer_id = ${idx}")
        params.append(retailer_id)
        idx += 1

    if country_iso:
        conditions.append(f"country_iso = ${idx}")
        params.append(country_iso.upper())
        idx += 1

    if processor:
        conditions.append(f"processor ILIKE ${idx}")
        params.append(f"%{processor}%")
        idx += 1

    if is_intel is not None:
        conditions.append(f"is_intel = ${idx}")
        params.append(is_intel)
        idx += 1

    if oem:
        conditions.append(f"oem ILIKE ${idx}")
        params.append(f"%{oem}%")
        idx += 1

    if min_price is not None:
        conditions.append(f"COALESCE(usd_selling_price, selling_price) >= ${idx}")
        params.append(min_price)
        idx += 1

    if max_price is not None:
        conditions.append(f"COALESCE(usd_selling_price, selling_price) <= ${idx}")
        params.append(max_price)
        idx += 1

    where_clause = " AND ".join(conditions)

    count_query = f"SELECT COUNT(*) FROM laptops_catalog WHERE {where_clause}"
    select_query = f"""
        SELECT
            id, sku_index, retailer_id, account, country, country_iso, site_type, form_factor,
            category_url, product_url, product_id, product_title, image_url, screenshot_url,
            screenshot_available, is_shared_capture, evidence_type, pdp_enriched,
            page_rank, product_rank, sos_eligible, selling_price, original_price,
            usd_selling_price, usd_original_price, discount_pct, currency, processor,
            is_intel, processor_model, processor_number, processor_gen, graphic_card,
            gaming, evo, p3, p4, p5, ram, storage, storage_type, screen_size, operating_system,
            oem, model, store_type, flag, extraction_id, extraction_method, extraction_timestamp,
            date, month, quarter, year, source, data_mode, top_account
        FROM laptops_catalog
        WHERE {where_clause}
        ORDER BY id ASC
        LIMIT ${idx} OFFSET ${idx + 1}
    """

    async with db.acquire() as conn:
        total = await conn.fetchval(count_query, *params)
        rows = await conn.fetch(select_query, *params, page_size, offset)

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size if total > 0 else 1,
        "items": [dict(r) for r in rows]
    }

@app.get("/api/products/{product_id}", tags=["Catalog"])
async def get_product_detail(product_id: str, pool: Optional[asyncpg.Pool] = Depends(get_db_pool)):
    db = pool if isinstance(pool, asyncpg.Pool) else await get_db_pool()
    query = """
        SELECT * FROM laptops_catalog
        WHERE product_id = $1 OR CAST(id AS TEXT) = $1
        LIMIT 1
    """
    async with db.acquire() as conn:
        row = await conn.fetchrow(query, product_id)

    if not row:
        raise HTTPException(status_code=404, detail="Product SKU not found")

    return dict(row)

# --- Retailer Universe & Coverage ---
@app.get("/api/retailers", tags=["Retailers"])
async def get_retailers(pool: Optional[asyncpg.Pool] = Depends(get_db_pool)):
    db = pool if isinstance(pool, asyncpg.Pool) else await get_db_pool()
    query = """
        SELECT
            retailer_id, account, country, country_iso, account_type, website,
            target_skus, extracted_skus, intel_skus_count, competitor_skus_count,
            sos_pct, sov_pct, overall_score, listing_s_score, details_p_score,
            s1_score, s2_score, p1_score, p2_score, p3_score, p4_score, p5_score,
            status, updated_at
        FROM retailer_storefronts
        ORDER BY account ASC
    """
    async with db.acquire() as conn:
        rows = await conn.fetch(query)

    return {
        "total_retailers": len(rows),
        "target_universe": 52,
        "items": [dict(r) for r in rows]
    }

# --- Share of Shelf & Analytics ---
@app.get("/api/analytics/summary", tags=["Analytics"])
async def get_analytics_summary(pool: Optional[asyncpg.Pool] = Depends(get_db_pool)):
    db = pool if isinstance(pool, asyncpg.Pool) else await get_db_pool()
    async with db.acquire() as conn:
        total_skus = await conn.fetchval("SELECT COUNT(*) FROM laptops_catalog")
        intel_skus = await conn.fetchval("SELECT COUNT(*) FROM laptops_catalog WHERE is_intel = TRUE")
        amd_skus = await conn.fetchval("SELECT COUNT(*) FROM laptops_catalog WHERE processor ILIKE '%amd%'")
        other_skus = total_skus - (intel_skus + amd_skus)

        evo_count = await conn.fetchval("SELECT COUNT(*) FROM laptops_catalog WHERE evo = 'Y'")
        gaming_count = await conn.fetchval("SELECT COUNT(*) FROM laptops_catalog WHERE gaming = 'Y'")

        oem_breakdown = await conn.fetch("""
            SELECT oem, COUNT(*) as count,
                   ROUND((COUNT(*)::numeric / $1) * 100, 1) as share_pct
            FROM laptops_catalog
            GROUP BY oem
            ORDER BY count DESC
            LIMIT 10
        """, total_skus or 1)

        country_breakdown = await conn.fetch("""
            SELECT country_iso, country, COUNT(*) as total_skus,
                   SUM(CASE WHEN is_intel THEN 1 ELSE 0 END) as intel_skus,
                   ROUND((SUM(CASE WHEN is_intel THEN 1 ELSE 0 END)::numeric / COUNT(*)) * 100, 1) as sos_pct
            FROM laptops_catalog
            GROUP BY country_iso, country
            ORDER BY country ASC
        """)

    return {
        "total_skus": total_skus,
        "intel_skus": intel_skus,
        "competitor_skus": total_skus - intel_skus,
        "intel_sos_pct": round((intel_skus / total_skus) * 100, 1) if total_skus > 0 else 0,
        "evo_skus_count": evo_count,
        "gaming_skus_count": gaming_count,
        "processor_share": {
            "intel": intel_skus,
            "amd": amd_skus,
            "other": max(0, other_skus)
        },
        "top_oems": [dict(r) for r in oem_breakdown],
        "country_breakdown": [dict(r) for r in country_breakdown]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.server:app", host="0.0.0.0", port=port, reload=False)
