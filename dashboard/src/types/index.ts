export type NavTabId =
  | 'overview'
  | 'live-extraction'
  | 'retailer-coverage'
  | 'scorecards'
  | 'sos'
  | 'sov'
  | 'products'
  | 'pricing'
  | 'audit'
  | 'banners'
  | 'evo'
  | 'retailers'
  | 'countries'
  | 'oems'
  | 'evidence'
  | 'data-quality'
  | 'scrape-center'
  | 'cost-center'
  | 'reports'
  | 'program-history';

export type RetailerType = '1P Retailer' | '3P Marketplace' | 'OEM';
export type ScrapeMethod = 'Bright Data' | 'Cached' | 'Existing Dataset' | 'Manual' | 'SERP Discovery' | 'SDK';
export type ScrapeStatus = 'SUCCESS' | 'PARTIAL' | 'FAILED' | 'CACHED' | 'SKIPPED';
export type FailureCategory =
  | 'Blocked'
  | 'CAPTCHA'
  | 'Timeout'
  | 'Invalid URL'
  | 'Parser failure'
  | 'Missing product data'
  | 'Unsupported structure'
  | 'HTTP error'
  | 'None';

export interface AuditFlag {
  pass: boolean;
  score?: number;
  label?: string;
  expected?: string;
  detected?: string;
  sourceUrl?: string;
  evidenceText?: string;
  screenshotPath?: string;
}

export interface ProductSKU {
  sku_id: string;
  product_id: string;
  oem: string;
  model_series: string;
  product_title: string;
  retailer: string;
  retailer_type: RetailerType;
  country: string;
  currency: string;
  current_price: number;
  original_price: number;
  price_usd: number;
  discount_amount: number;
  discount_pct: number;
  processor_brand: 'Intel' | 'AMD' | 'Apple' | 'Qualcomm';
  processor_series: string;
  processor_gen: string;
  processor_model: string;
  is_intel_cpu: boolean;
  graphics_card: string;
  ram_size: string;
  ram_type: string;
  storage_size: string;
  storage_type: string;
  screen_size: string;
  screen_type: string;
  form_factor: 'Laptop' | 'Desktop' | 'Workstation' | 'Tablet';
  segment: 'AI PC' | 'Premium' | 'Gaming' | 'Mainstream' | 'Entry';
  operating_system: string;
  is_evo: boolean;
  is_vpro: boolean;
  is_gaming: boolean;
  availability: 'In Stock' | 'Limited Stock' | 'Out of Stock';
  compliance_score: number;
  audit_flags: {
    S1?: AuditFlag;
    S2?: AuditFlag;
    P1?: AuditFlag;
    P2?: AuditFlag;
    P3?: AuditFlag;
    P4?: AuditFlag;
    P5?: AuditFlag;
    sku_audit_score?: number;
    [key: string]: any;
  };
  product_url: string;
  screenshot_pdp_path?: string;
  sourceUrl: string;
  sourceType: string;
  scrapedAt: string;
  cachedAt: string;
  scrapeMethod: ScrapeMethod;
  status: ScrapeStatus;
  confidence: number;
  price_history: Array<{
    date: string;
    price: number;
    price_usd: number;
    retailer: string;
  }>;
}

export interface Retailer {
  id: string;
  name: string;
  domain: string;
  country: string;
  type: RetailerType;
  products_count: number;
  intel_skus_count: number;
  competitor_skus_count: number;
  brand_compliance_score: number;
  laptop_compliance_score: number;
  desktop_compliance_score: number;
  compliance_grade: string;
  last_successful_crawl: string;
  data_freshness: string;
  extraction_success_rate: number;
  cached_pages_count: number;
  live_requests_count: number;
  brightdata_requests_count: number;
  status: 'ACTIVE_POC' | 'CACHED' | 'NOT_YET_SCRAPED';
  data_source_mode: 'Real Scraped Data' | 'Cached Data' | 'Sampled Data';
}

export interface Banner {
  banner_id: string;
  retailer: string;
  brand: string;
  position: string;
  headline: string;
  subheadline: string;
  discount_text: string;
  has_destination_link: boolean;
  destination_link: string;
  landing_page_url?: string;
  flags: {
    evo_flag: boolean;
    gaming_flag: boolean;
    premier_sku_flag: boolean;
    ai_pc_flag: boolean;
    [key: string]: any;
  };
  first_seen?: string;
  last_seen?: string;
  screenshot_file: string;
  screenshot_svg_path?: string;
  confidence?: number;
  [key: string]: any;
}

export interface KeywordSOV {
  keyword: string;
  intel_share_pct: number;
  sponsored_intel_share_pct: number;
  intel_count: number;
  amd_count: number;
  apple_count: number;
  qualcomm_count: number;
  total_results_sampled: number;
  intel_rank: number;
  top_ranked_sku: string;
  top2_page_audit: {
    score?: number;
    s1_pass?: boolean;
    s2_pass?: boolean;
    p1_pass?: boolean;
    p2_pass?: boolean;
    [key: string]: any;
  };
  retailer_breakdown?: Record<string, number>;
  [key: string]: any;
}

export interface ScrapeJob {
  id: string;
  url: string;
  retailer: string;
  country: string;
  reason: string;
  method: ScrapeMethod;
  cache_status: 'HIT' | 'MISS';
  priority: 'HIGH' | 'NORMAL' | 'LOW';
  status: ScrapeStatus;
  failure_reason?: FailureCategory;
  brightdata_request_count: number;
  duration_ms: number;
  fields_extracted: number;
  timestamp: string;
}

export interface CostMetrics {
  total_budget_requests: number;
  used_requests: number;
  cached_requests: number;
  blocked_duplicate_requests: number;
  cache_hit_rate_pct: number;
  estimated_cost_usd: number;
}

export interface CostGuardrails {
  session_limit: number;
  retailer_limit: number;
  url_limit: number;
  cache_ttl_days: number;
  rate_limit_rpm?: number;
  duplicate_url_protection: boolean;
  global_budget_limit: number;
}
