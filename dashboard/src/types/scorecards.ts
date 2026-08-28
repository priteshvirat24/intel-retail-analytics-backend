export type MainNavId =
  | 'overview'
  | 'live-extraction'
  | 'retailer-coverage'
  | 'scorecards'
  | 'sos'
  | 'sov'
  | 'products'
  | 'retailers'
  | 'banners'
  | 'evo'
  | 'evidence'
  | 'data-quality'
  | 'scrape-center'
  | 'cost-center'
  | 'reports'
  | 'program-history';

export type LiveExtractionSubTab = 'live-controller' | 'live-logs' | 'job-history' | 'bd-budget-guard';
export type RetailerCoverageSubTab = 'coverage-table' | 'coverage-heatmap' | 'data-completeness' | 'extraction-efficiency';
export type ScorecardsSubTab = 'account-scorecards' | 'product-scorecards' | 'score-distribution' | 'score-trends';
export type SosSubTab = 'sos-overview' | 'sos-retailer' | 'sos-country' | 'sos-oem' | 'sos-product' | 'sos-trend' | 'category-urls';
export type SovSubTab = 'sov-overview' | 'sov-keywords' | 'sov-retailer' | 'sov-country' | 'sov-product' | 'sov-search-results' | 'sov-trend' | 'sov-matrix-full';
export type ProductsSubTab = 'product-explorer' | 'product-detail' | 'product-comparison' | 'price-intelligence';
export type RetailersSubTab = 'account-explorer' | 'account-detail' | 'account-performance' | 'account-history';
export type BannersSubTab = 'banner-overview' | 'banner-explorer' | 'banner-evidence';
export type EvoSubTab = 'evo-overview' | 'evo-products' | 'evo-retailer' | 'evo-oem';
export type EvidenceSubTab = 'screenshots' | 'source-pages' | 'audit-evidence';

export type AccountType = '1P Retailer' | '3P Marketplace' | 'OEM';
export type SourceType = 'Website' | 'Mobile Application';
export type ScrapeMethod = 'Bright Data' | 'SDK' | 'SERP' | 'Cached' | 'Existing Dataset' | 'Manual';
export type ScrapeStatus = 'SUCCESS' | 'PARTIAL' | 'FAILED' | 'CACHED' | 'SKIPPED';
export type DataCategory = 'LIVE' | 'CACHED' | 'SAMPLED' | 'HISTORICAL' | 'NOT AVAILABLE';

export interface ScorecardSKU {
  // Common Time Dimensions
  date: string; // Format: d/m/yyyy 00:00 e.g. 1/8/2024 00:00
  month: number; // 1-12 e.g. 8
  quarter: number; // 1-4 e.g. 3
  year: number; // e.g. 2024, 2025, 2026

  // Source & Account Dimensions
  source: SourceType; // Website or Mobile Application
  top_account: boolean; // TRUE or FALSE
  country: string; // Full country name (e.g. United States, United Kingdom, Canada, France)
  account: string; // Format: Best Buy - US, Amazon - US, Dell, HP, etc.
  form_factor: 'Laptop' | 'Desktop';

  // SOS-Specific Columns
  sos_eligible: boolean; // TRUE if from first 2 category pages
  category_url?: string;
  category_screenshot?: string;
  page_rank: number; // 1 or 2
  product_rank: number; // Position on page

  // SOV-Specific Columns
  Intel_keyword?: string;
  keyword_rank?: number;
  search_volume?: number;
  sov_harvested?: boolean; // TRUE for all collected search results
  sov_score_eligible?: boolean; // TRUE if page_rank 1-2 AND keyword_rank 1-20

  // Product Identification & Evidence
  product_url: string;
  product_id: string;
  product_screenshot: string;
  product_title: string;
  image_url: string;

  // Pricing
  original_price: number;
  selling_price: number;
  usd_original_price: number;
  usd_selling_price: number;
  discount_amount: number;
  discount_pct: number;
  currency: string;

  // Product Specifications
  processor: 'Intel' | 'AMD' | 'Qualcomm' | 'Apple';
  graphic_card: string; // Integrated / Discrete GPU model
  Gaming: 'Y' | 'N';
  Evo: 'Y' | 'N';
  Vpro: 'Y' | 'N';
  Premium: 'Y' | 'N';

  // Scoring Breakdown (0-100 Integer, No Decimals)
  Overall: number; // Average of listing_s and details_p (or weighted)
  listing_s: number; // Average of S1 and S2
  details_p: number; // Average of P1-P5
  s1: number; // Listing title score (0-100)
  s2: number; // Listing badge score (0-100)
  p1: number; // PDP title score (0-100)
  p2: number; // PDP badge score (0-100)
  p3: number; // Spec presence score (0-100)
  p4: number; // Intel-led Rich Media score (0-100)
  p5: number; // OEM Rich Media score (0-100)

  // Additional Product Information
  ram: number; // Numeric GB
  storage: number; // Numeric GB
  storage_type: 'HDD' | 'SSD' | 'eMMC' | 'Hybrid';
  screen_size: number; // Numeric inches e.g. 14.0, 15.6, 16.0
  screen_type?: string; // e.g. OLED FHD+, IPS 144Hz
  operating_system: string;
  oem: string; // Manufacturer (LG, HP, Dell, ASUS, Lenovo, Apple, Acer)
  model: string; // Product series model (Gram, Omen, Inspiron, XPS, Yoga, ROG)
  gen: string; // 1st Gen to 14th Gen, Series 1, Series 2
  processor_model: string; // Ultra 7, Core 7, i7, Ultra 9, i5, etc.
  number: string; // SKU of processor e.g. 155H, 155U, 220V, 1335U
  '3p_1p': '1P' | '3P';
  Flag: string; // MoM PDP status relative to previous month (e.g. 101, 102)
  concatenate: string; // Premier SKU identifier: 'Y' | 'N'

  // Provenance Metadata
  extraction_method: ScrapeMethod;
  source_url: string;
  scraped_at: string;
  cache_status: 'HIT' | 'MISS';
  extraction_status: ScrapeStatus;
  evidence_url: string;
  screenshot_available: boolean;
  data_confidence: number;
  data_label: DataCategory;

  // Real Artifacts & Cryptographic Provenance Lineage
  screenshot_path?: string;
  screenshot_sha256?: string | null;
  provenance?: {
    source_url?: string;
    extraction_id?: string;
    provider?: string;
    provider_request_id?: string | null;
    captured_at?: string;
    recorded_at?: string;
    access_status?: string;
    artifact_sha256?: string;
  };

  // Rich Media Evidence
  rich_media_evidence?: {
    s1_text?: string;
    s2_badge_detected?: string;
    s2_badge_image?: string;
    s2_badge_sha256?: string;
    p1_text?: string;
    p2_badge_detected?: string;
    p2_badge_image?: string;
    p2_badge_sha256?: string;
    p3_spec_text?: string;
    p4_a_plus_content?: string;
    p4_a_plus_sha256?: string;
    p5_oem_media?: string;
    p5_oem_sha256?: string;
    raw_html_path?: string;
    raw_html_sha256?: string;
  };

  // Lineage Price History
  price_history: Array<{
    date: string;
    selling_price: number;
    usd_selling_price: number;
    account: string;
  }>;
}

export interface ScorecardAccount {
  account: string;
  country: string;
  account_type: AccountType;
  top_account: boolean;
  source: SourceType;
  tracking_frequency: 'Monthly' | 'Once per quarter' | 'Second month of quarter' | 'Twice per quarter' | 'Direct Feed';
  active: boolean;
  website: string;
  products_count: number;
  intel_skus_count: number;
  competitor_skus_count: number;
  sos_pct: number;
  sov_pct: number;
  Overall_score: number;
  listing_s_score: number;
  details_p_score: number;
  s1_score: number;
  s2_score: number;
  p1_score: number;
  p2_score: number;
  p3_score: number;
  p4_score: number;
  p5_score: number;
  laptop_score: number;
  desktop_score: number;
  evo_count: number;
  premium_count: number;
  gaming_count: number;
  vpro_count: number;
  last_successful_crawl: string;
  data_freshness: string;
  extraction_success_rate: number;
  cached_pages_count: number;
  live_requests_count: number;
  brightdata_requests_count: number;
  data_label: DataCategory;
}

export interface ScorecardBanner {
  banner_id: string;
  banner_url: string;
  account: string;
  country: string;
  banner_brand: 'Intel' | 'Intel Core' | 'AMD' | 'Qualcomm' | 'Apple' | 'PC Mix';
  banner_type: string;
  destination_url: string;
  screenshot: string;
  first_seen: string;
  last_seen: string;
  discount: string;
  EVO: 'Y' | 'N';
  Gaming: 'Y' | 'N';
  Premier_SKU: 'Y' | 'N';
  headline: string;
  subheadline: string;
  has_destination_link: boolean;
  data_label: DataCategory;
}

export interface ScorecardKeyword {
  Intel_keyword: string;
  keyword_rank: number;
  search_volume: number;
  country: string;
  account: string;
  intel_product_count: number;
  competitor_product_count: number;
  intel_presence_pct: number;
  intel_share_pct: number;
  sponsored_intel_share_pct: number;
  total_results: number;
  scoring_eligible_results: number; // page_rank 1-2 & keyword_rank 1-20
  top_ranked_sku: string;
  s1_score: number;
  s2_score: number;
  p1_score: number;
  p2_score: number;
  p3_score: number;
  p4_score: number;
  p5_score: number;
  overall_score: number;
  retailer_breakdown: Record<string, number>;
}

export interface ProgramHistoryMetrics {
  year: number;
  accounts_count: number;
  tracking_cadence: string;
  sos: {
    total_products: number;
    avg_monthly_products: number;
    avg_category_pages_month: number;
  };
  sov: {
    total_products: number;
    avg_monthly_products: number;
    avg_keywords_month: number;
  };
  banners: {
    urls_count: number;
    accounts_count: number;
    total_banners: number;
    avg_monthly_banners: number;
  };
  account_changes: {
    added: string[];
    removed: string[];
  };
  account_composition: string[];
}

export interface ExtractionWaterfallMetrics {
  total_candidate_urls: number;
  cached_urls: number;
  existing_dataset_urls: number;
  sdk_urls: number;
  serp_urls: number;
  brightdata_required_urls: number;
  cache_hit_rate_pct: number;
  requests_avoided: number;
  used_requests: number;
  budget_requests: number;
  estimated_cost_usd: number;
}

export interface InSeasonPricingSummary {
  frequency: '3 times daily';
  sites_scope: {
    one_p_retailers_count: 173;
    three_p_marketplaces_count: 14;
    oem_websites_count: 6;
    key_countries_count: 23;
  };
  form_factors: string[];
  competitors_tracked: string[];
  last_feed_sync: string;
  sftp_delivery_status: 'HEALTHY' | 'SYNCING' | 'PENDING';
}

export interface DeliveryScheduleItem {
  scope_item: string;
  cadence: 'MultiDaily' | 'Daily' | 'Weekly' | 'Monthly';
  deliverable_format: string;
  status: 'DELIVERED' | 'ACTIVE_STREAM' | 'SCHEDULED';
  last_delivery: string;
  next_delivery: string;
  sla_compliance_pct: number;
}
