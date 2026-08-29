/**
 * Centralized API Client for Intel Retail Competitive Intelligence Dashboard
 * Connects directly to the production Render Backend backed by Neon PostgreSQL.
 */

export const API_BASE_URL = (
  import.meta.env.VITE_API_BASE_URL || 'https://intel-retail-backend.onrender.com'
).replace(/\/$/, '');

export interface ApiOverviewResponse {
  total_accounts: number;
  total_retailers: number;
  total_skus: number;
  country_count: number;
  intel_sku_count: number;
  competitor_sku_count: number;
  intel_sos: number;
  intel_sov: number;
  average_overall_score: number;
  average_listing_score: number;
  average_pdp_score: number;
  evo_count: number;
  gaming_count: number;
  premium_count: number;
  vpro_count: number;
  average_selling_price: number;
  cache_hit_rate: number;
  crawl_success_rate: number;
  evidence_verification_coverage: number;
  last_updated: string;
}

export interface ApiRetailer {
  id: string;
  retailer_id: string;
  account: string;
  country: string;
  country_iso: string;
  type?: string;
  website?: string;
  target_skus: number;
  actual_skus: number;
  extracted_skus: number;
  coverage_percent: number;
  status: 'COMPLETED' | 'PARTIAL' | 'FAILED';
  intel_sku_count: number;
  competitor_sku_count: number;
  sos: number;
  sov: number;
  average_score: number;
  overall_score: number;
  listing_s_score: number;
  details_p_score: number;
  s1_score: number;
  s2_score: number;
  p1_score: number;
  p2_score: number;
  p3_score: number;
  p4_score: number;
  p5_score: number;
  screenshot_coverage: number;
  pdp_enriched_count?: number;
  screenshots?: number;
  pdp_enriched?: number;
  evidence_coverage: number;
  price_coverage_pct: number;
  last_extracted_at?: string;
}

export interface ApiProduct {
  id: number;
  sku_index?: number;
  retailer_id: string;
  account: string;
  country: string;
  country_iso: string;
  site_type?: string;
  form_factor?: string;
  category_url?: string;
  product_url: string;
  product_id: string;
  product_title: string;
  image_url?: string;
  screenshot_url?: string;
  screenshot_path?: string;
  screenshot_sha256?: string;
  screenshot_available?: boolean;
  is_shared_capture?: boolean;
  evidence_type?: string;
  pdp_enriched?: boolean;
  page_rank: number;
  product_rank: number;
  sos_eligible?: boolean;
  selling_price: number;
  original_price: number;
  usd_selling_price?: number;
  usd_original_price?: number;
  discount_pct?: number;
  currency: string;
  processor: string;
  is_intel: boolean;
  processor_model?: string;
  processor_number?: string;
  processor_gen?: string;
  graphic_card?: string;
  gaming?: string;
  evo?: string;
  p3?: string;
  p4?: string;
  p5?: string;
  ram?: string;
  storage?: string;
  storage_type?: string;
  screen_size?: string;
  operating_system?: string;
  oem?: string;
  model?: string;
  store_type?: string;
  flag?: string;
  extraction_id?: string;
  extraction_method?: string;
  extraction_timestamp?: string;
  provenance_json?: string;
  date?: string;
  month?: string;
  quarter?: string;
  year?: string;
  source?: string;
  data_mode?: string;
  top_account?: string;
  overall?: number;
  listing_s?: number;
  details_p?: number;
  s1?: number;
  s2?: number;
  p1?: number;
  p2?: number;
}

export interface ApiProductsResponse {
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
  items: ApiProduct[];
}

export interface ApiScorecardsResponse {
  total: number;
  items: ApiRetailer[];
}

export interface ApiSosResponse {
  global_intel_sos: number;
  total_eligible_skus: number;
  total_intel_skus: number;
  retailer_breakdown: Array<{
    retailer_id: string;
    account: string;
    country: string;
    country_iso: string;
    eligible_sku_count: number;
    intel_sku_count: number;
    competitor_sku_count: number;
    intel_sos: number;
    amd_count: number;
    other_count: number;
  }>;
}

export interface ApiSovResponse {
  global_intel_sov: number;
  total_top20_slots: number;
  retailer_breakdown: Array<{
    retailer_id: string;
    account: string;
    country: string;
    country_iso: string;
    top20_visibility_slots: number;
    intel_visibility_slots: number;
    competitor_visibility_slots: number;
    intel_sov: number;
  }>;
}

export interface ApiEvidenceItem {
  id: number;
  evidence_id: string;
  product_id: string;
  product_title: string;
  retailer_id: string;
  account: string;
  country: string;
  country_iso: string;
  source_url: string;
  screenshot?: string;
  image_url?: string;
  hash?: string;
  screenshot_available?: boolean;
  pdp_enriched?: boolean;
  processor: string;
  processor_model?: string;
  is_intel: boolean;
  selling_price: number;
  currency: string;
  usd_selling_price?: number;
  extraction_id?: string;
  capture_timestamp?: string;
  extraction_method?: string;
  raw_evidence?: string;
  evidence_type: string;
  verification_status: string;
}

export interface ApiEvidenceSummary {
  total_evidence_records: number;
  verified: number;
  partially_verified: number;
  unverified: number;
  insufficient_evidence: number;
  source_url_coverage: number;
  screenshot_coverage: number;
  badge_coverage: number;
  p4_coverage: number;
  p5_coverage: number;
  raw_artifact_coverage: number;
  broken_reference_count: number;
  collision_count: number;
}

export interface ApiPricingResponse {
  average_usd_price: number;
  min_usd_price: number;
  max_usd_price: number;
  average_discount_pct: number;
  total_priced_skus: number;
  items: Array<{
    id: number;
    product_id: string;
    product_title: string;
    retailer_id: string;
    account: string;
    country: string;
    country_iso: string;
    selling_price: number;
    original_price: number;
    usd_selling_price?: number;
    usd_original_price?: number;
    discount_pct?: number;
    currency: string;
    oem?: string;
    processor: string;
    is_intel: boolean;
    date?: string;
  }>;
}

export interface ApiDataQuality {
  total_skus: number;
  completeness_score: number;
  missing_title_count: number;
  missing_price_count: number;
  missing_processor_count: number;
  missing_screenshot_count: number;
  missing_url_count: number;
  duplicate_skus_count: number;
  broken_references_count: number;
}

export interface ApiBrightDataUsage {
  total_requests: number;
  successful_requests: number;
  failed_requests: number;
  success_rate: number;
  cache_hits: number;
  requests_avoided: number;
  bandwidth_mb: number;
  cost_status: string;
  zone: string;
  last_active: string;
}

export interface ApiScrapeJobs {
  total_jobs: number;
  active_jobs: number;
  completed_jobs: number;
  items: Array<{
    job_id: string;
    retailer_name: string;
    country: string;
    skus_extracted: number;
    target_skus: number;
    status: string;
    completed_at: string;
  }>;
}

// Reusable fetch helper with error handling
async function fetchApi<T>(endpoint: string, params?: Record<string, any>): Promise<T> {
  let url = `${API_BASE_URL}${endpoint}`;
  if (params) {
    const query = new URLSearchParams();
    Object.entries(params).forEach(([key, val]) => {
      if (val !== undefined && val !== null && val !== '') {
        query.append(key, String(val));
      }
    });
    const qs = query.toString();
    if (qs) {
      url += `?${qs}`;
    }
  }

  const res = await fetch(url, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
    }
  });

  if (!res.ok) {
    throw new Error(`API Error [${res.status}]: ${res.statusText} for ${url}`);
  }

  return res.json();
}

export const api = {
  getHealth: () => fetchApi<{ status: string; database: string; total_skus: number; total_retailers: number }>('/health'),
  getOverview: () => fetchApi<ApiOverviewResponse>('/api/v1/overview'),
  getRetailers: () => fetchApi<{ total_retailers: number; target_universe: number; items: ApiRetailer[] }>('/api/v1/retailers'),
  getRetailerById: (id: string) => fetchApi<ApiRetailer>(`/api/v1/retailers/${encodeURIComponent(id)}`),
  getProducts: (params?: {
    search?: string;
    retailer?: string;
    retailer_id?: string;
    country?: string;
    country_iso?: string;
    processor?: string;
    is_intel?: boolean;
    oem?: string;
    form_factor?: string;
    gaming?: string;
    evo?: string;
    vpro?: string;
    min_price?: number;
    max_price?: number;
    date?: string;
    page?: number;
    page_size?: number;
  }) => fetchApi<ApiProductsResponse>('/api/v1/products', params),
  getProductById: (id: string | number) => fetchApi<ApiProduct>(`/api/v1/products/${encodeURIComponent(id)}`),
  getScorecards: (params?: { retailer?: string; country?: string; oem?: string }) => fetchApi<ApiScorecardsResponse>('/api/v1/scorecards', params),
  getSOS: (params?: { retailer?: string; country?: string }) => fetchApi<ApiSosResponse>('/api/v1/sos', params),
  getSOV: (params?: { retailer?: string; country?: string }) => fetchApi<ApiSovResponse>('/api/v1/sov', params),
  getEvidence: (params?: { product_id?: string; retailer_id?: string; limit?: number }) => fetchApi<{ total: number; items: ApiEvidenceItem[] }>('/api/v1/evidence', params),
  getEvidenceSummary: () => fetchApi<ApiEvidenceSummary>('/api/v1/evidence/summary'),
  getPricing: (params?: { retailer?: string; country?: string }) => fetchApi<ApiPricingResponse>('/api/v1/pricing', params),
  getBanners: () => fetchApi<{ total_banners: number; items: any[] }>('/api/v1/banners'),
  getEvo: () => fetchApi<{ total_evo_skus: number; evo_share_pct: number; retailer_breakdown: any[]; items: any[] }>('/api/v1/evo'),
  getDataQuality: () => fetchApi<ApiDataQuality>('/api/v1/data-quality'),
  getBrightDataUsage: () => fetchApi<ApiBrightDataUsage>('/api/v1/brightdata-usage'),
  getScrapeJobs: () => fetchApi<ApiScrapeJobs>('/api/v1/scrape-jobs'),
  getProductEvidence: (id: string | number) => fetchApi<{ product: ApiProduct; evidence_records: any[] }>(`/api/v1/evidence/product/${encodeURIComponent(id)}`),
};

export default api;
