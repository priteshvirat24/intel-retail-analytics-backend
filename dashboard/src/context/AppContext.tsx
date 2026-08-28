import React, { createContext, useContext, useState, useMemo } from 'react';
import {
  NavTabId,
  ProductSKU,
  Retailer,
  Banner,
  KeywordSOV,
  ScrapeJob,
  CostMetrics,
  CostGuardrails,
} from '../types';
import {
  ScorecardSKU,
  ScorecardAccount,
  ScorecardBanner,
  ScorecardKeyword,
} from '../types/scorecards';

import rawProductsData from '../data/brand_benchmarking_scores.json';
import pricingData from '../data/category_pricing_segments.json';
import evoData from '../data/intel_evo_tracking_report.json';
import sosData from '../data/share_of_shelf_report.json';
import sovData from '../data/share_of_voice_report.json';
import bannerData from '../data/banner_tracking_report.json';
import cpuData from '../data/processor_comparison_report.json';
import regionalData from '../data/regional_report_us_latam.json';
import screenshotIndex from '../data/screenshot_index.json';

import {
  SCORECARD_PRODUCTS,
  SCORECARD_ACCOUNTS,
  SCORECARD_KEYWORDS,
  SCORECARD_BANNERS,
  LIVE_52_SKU_DATASET,
  LIVE_RETAILER_COVERAGE,
  LIVE_DATASET_SUMMARY
} from '../data/scorecardsData';

import { ProgramConfig, PROGRAM_CONFIG } from '../config/programConfig';
import {
  AnalyticsEngine,
  OverviewKpis,
  SosDistributionItem,
  ScorecardComponentAverages,
  PricingSummary,
  CoverageSummary
} from '../services/analyticsEngine';

export const matchCountry = (accountCountry: string, filter: string) => {
  if (!filter || filter === 'ALL') return true;
  const f = filter.toLowerCase().trim();
  const ac = (accountCountry || '').toLowerCase().trim();
  if (ac === f) return true;
  if ((f === 'us' || f === 'usa') && (ac.includes('united states') || ac === 'us')) return true;
  if ((f === 'uk' || f === 'gb') && (ac.includes('united kingdom') || ac === 'uk' || ac === 'gb')) return true;
  if (f === 'ca' && (ac.includes('canada') || ac === 'ca')) return true;
  if (f === 'de' && (ac.includes('germany') || ac === 'de')) return true;
  if (f === 'fr' && (ac.includes('france') || ac === 'fr')) return true;
  if (f === 'it' && (ac.includes('italy') || ac === 'it')) return true;
  if (f === 'es' && (ac.includes('spain') || ac === 'es')) return true;
  if (f === 'nl' && (ac.includes('netherlands') || ac === 'nl')) return true;
  if (f === 'au' && (ac.includes('australia') || ac === 'au')) return true;
  if (f === 'in' && (ac.includes('india') || ac === 'in')) return true;
  if (f === 'jp' && (ac.includes('japan') || ac === 'jp')) return true;
  if (f === 'kr' && (ac.includes('korea') || ac === 'kr')) return true;
  if (f === 'cn' && (ac.includes('china') || ac === 'cn')) return true;
  if (f === 'br' && (ac.includes('brazil') || ac === 'br')) return true;
  if (f === 'mx' && (ac.includes('mexico') || ac === 'mx')) return true;
  if (f === 'sg' && (ac.includes('singapore') || ac === 'sg')) return true;
  if (f === 'my' && (ac.includes('malaysia') || ac === 'my')) return true;
  if (f === 'pl' && (ac.includes('poland') || ac === 'pl')) return true;
  if (f === 'se' && (ac.includes('sweden') || ac === 'se')) return true;
  if (f === 'no' && (ac.includes('norway') || ac === 'no')) return true;
  if (f === 'dk' && (ac.includes('denmark') || ac === 'dk')) return true;
  if (f === 'tr' && (ac.includes('turkey') || ac === 'tr')) return true;
  return false;
};

interface AppContextType {
  activeTab: NavTabId;
  setActiveTab: (tab: NavTabId) => void;
  // Centralized Configuration
  programConfig: ProgramConfig;
  updateProgramConfig: (cfg: Partial<ProgramConfig>) => void;
  // Dynamic Calculated Analytics
  overviewKpis: OverviewKpis;
  sosDistribution: SosDistributionItem[];
  oemDistribution: Array<{ oem: string; count: number; intelCount: number; intelPct: number }>;
  scorecardMetrics: ScorecardComponentAverages;
  pricingMetrics: PricingSummary;
  coverageMetrics: CoverageSummary;
  // Datasets
  products: ProductSKU[];
  filteredProducts: ProductSKU[];
  scorecardProducts: ScorecardSKU[];
  filteredScorecardProducts: ScorecardSKU[];
  scorecardAccounts: ScorecardAccount[];
  filteredScorecardAccounts: ScorecardAccount[];
  retailers: Retailer[];
  banners: Banner[];
  keywords: KeywordSOV[];
  scrapeJobs: ScrapeJob[];
  costMetrics: CostMetrics;
  guardrails: CostGuardrails;
  sosData: any;
  sovData: any;
  pricingData: any;
  evoData: any;
  cpuData: any;
  regionalData: any;
  screenshotIndex: any;
  // Filters
  searchQuery: string;
  setSearchQuery: (q: string) => void;
  selectedCountry: string;
  setSelectedCountry: (c: string) => void;
  selectedRetailer: string;
  setSelectedRetailer: (r: string) => void;
  selectedCategory: string;
  setSelectedCategory: (cat: string) => void;
  selectedSegment: string;
  setSelectedSegment: (s: string) => void;
  selectedFormFactor: string;
  setSelectedFormFactor: (f: string) => void;
  dateRange: string;
  setDateRange: (d: string) => void;
  // Dynamic Dataset Controls (Zero-Data / Custom Testing)
  setRawProducts: (products: ScorecardSKU[]) => void;
  setRawAccounts: (accounts: ScorecardAccount[]) => void;
  clearData: () => void;
  resetToFullLiveDataset: () => void;
  // Modals & Drawers
  selectedSkuDetail: any | null;
  setSelectedSkuDetail: (sku: any | null) => void;
  selectedRetailerDetail: any | null;
  setSelectedRetailerDetail: (ret: any | null) => void;
  liveValidationTarget: any | null;
  setLiveValidationTarget: (sku: any | null) => void;
  runSampleModalOpen: boolean;
  setRunSampleModalOpen: (open: boolean) => void;
  settingsModalOpen: boolean;
  setSettingsModalOpen: (open: boolean) => void;
  sourceEvidenceTarget: any | null;
  setSourceEvidenceTarget: (sku: any | null) => void;
  reportPreviewTarget: { title: string; type: string; data: any } | null;
  setReportPreviewTarget: (t: { title: string; type: string; data: any } | null) => void;
  // Live Actions
  executeLiveValidation: (sku: any) => Promise<{ success: boolean; fromCache: boolean }>;
  executeRunSample: (retailer: string, count: number, mode: string) => Promise<void>;
  updateGuardrails: (g: CostGuardrails) => void;
  resetFilters: () => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [activeTab, setActiveTab] = useState<NavTabId>('overview');

  // Global Filters
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedCountry, setSelectedCountry] = useState<string>('ALL');
  const [selectedRetailer, setSelectedRetailer] = useState<string>('ALL');
  const [selectedCategory, setSelectedCategory] = useState<string>('ALL');
  const [selectedSegment, setSelectedSegment] = useState<string>('ALL');
  const [selectedFormFactor, setSelectedFormFactor] = useState<string>('ALL');
  const [dateRange, setDateRange] = useState<string>('Current POC Run');

  // Modals
  const [selectedSkuDetail, setSelectedSkuDetail] = useState<any | null>(null);
  const [selectedRetailerDetail, setSelectedRetailerDetail] = useState<any | null>(null);
  const [liveValidationTarget, setLiveValidationTarget] = useState<any | null>(null);
  const [runSampleModalOpen, setRunSampleModalOpen] = useState<boolean>(false);
  const [settingsModalOpen, setSettingsModalOpen] = useState<boolean>(false);
  const [sourceEvidenceTarget, setSourceEvidenceTarget] = useState<any | null>(null);
  const [reportPreviewTarget, setReportPreviewTarget] = useState<{ title: string; type: string; data: any } | null>(null);

  // Initial Cost Metrics
  const [costMetrics, setCostMetrics] = useState<CostMetrics>({
    total_budget_requests: 100,
    used_requests: 17,
    cached_requests: 214,
    blocked_duplicate_requests: 48,
    cache_hit_rate_pct: 92.6,
    estimated_cost_usd: 0.34,
  });

  // Cost Guardrails
  const [guardrails, setGuardrails] = useState<CostGuardrails>({
    session_limit: 10,
    retailer_limit: 3,
    url_limit: 1,
    cache_ttl_days: 7,
    rate_limit_rpm: 30,
    duplicate_url_protection: true,
    global_budget_limit: 100,
  });

  // Centralized Dynamic Configuration
  const [programConfig, setProgramConfig] = useState<ProgramConfig>(PROGRAM_CONFIG);

  const updateProgramConfig = (cfg: Partial<ProgramConfig>) => {
    setProgramConfig((prev) => ({ ...prev, ...cfg }));
  };

  // Dynamic Canonical Datasets (supports live data, custom test datasets, and zero-data tests)
  const [rawProducts, setRawProducts] = useState<ScorecardSKU[]>(LIVE_52_SKU_DATASET);
  const [rawAccounts, setRawAccounts] = useState<ScorecardAccount[]>(SCORECARD_ACCOUNTS);

  const clearData = () => {
    setRawProducts([]);
    setRawAccounts([]);
  };

  const resetToFullLiveDataset = () => {
    setRawProducts(LIVE_52_SKU_DATASET);
    setRawAccounts(SCORECARD_ACCOUNTS);
  };

  const scorecardProducts = rawProducts;
  const scorecardAccounts = rawAccounts;

  // Fully-Wired Filtered Scorecard Products
  const filteredScorecardProducts = useMemo(() => {
    return scorecardProducts.filter((p) => {
      // 1. Search Query
      if (searchQuery) {
        const q = searchQuery.toLowerCase().trim();
        const matches =
          (p.product_title && p.product_title.toLowerCase().includes(q)) ||
          (p.oem && p.oem.toLowerCase().includes(q)) ||
          (p.model && p.model.toLowerCase().includes(q)) ||
          (p.account && p.account.toLowerCase().includes(q)) ||
          (p.product_id && p.product_id.toLowerCase().includes(q)) ||
          (p.processor_model && p.processor_model.toLowerCase().includes(q)) ||
          (p.Intel_keyword && p.Intel_keyword.toLowerCase().includes(q));
        if (!matches) return false;
      }

      // 2. Country Filter
      if (selectedCountry !== 'ALL' && !matchCountry(p.country, selectedCountry)) {
        return false;
      }

      // 3. Retailer Filter
      if (selectedRetailer !== 'ALL' && p.account !== selectedRetailer) {
        return false;
      }

      // 4. Category Filter (Laptops vs Desktops)
      if (selectedCategory !== 'ALL') {
        const cat = selectedCategory.toLowerCase();
        if (cat.includes('laptop') && p.form_factor !== 'Laptop') return false;
        if (cat.includes('desktop') && p.form_factor !== 'Desktop') return false;
      }

      // 5. Segment Filter
      if (selectedSegment !== 'ALL') {
        const seg = selectedSegment.toLowerCase();
        if (seg.includes('gaming') && p.Gaming !== 'Y') return false;
        if (seg.includes('evo') && p.Evo !== 'Y') return false;
        if (seg.includes('premium') && p.Premium !== 'Y') return false;
        if (seg.includes('vpro') && p.Vpro !== 'Y') return false;
      }

      // 6. Form Factor Filter
      if (selectedFormFactor !== 'ALL' && p.form_factor !== selectedFormFactor) {
        return false;
      }

      return true;
    });
  }, [scorecardProducts, searchQuery, selectedCountry, selectedRetailer, selectedCategory, selectedSegment, selectedFormFactor]);

  // Fully-Wired Filtered Scorecard Accounts
  const filteredScorecardAccounts = useMemo(() => {
    return scorecardAccounts.filter((a) => {
      // 1. Search Query
      if (searchQuery) {
        const q = searchQuery.toLowerCase().trim();
        const matches =
          (a.account && a.account.toLowerCase().includes(q)) ||
          (a.country && a.country.toLowerCase().includes(q)) ||
          (a.account_type && a.account_type.toLowerCase().includes(q));
        if (!matches) return false;
      }

      // 2. Country Filter
      if (selectedCountry !== 'ALL' && !matchCountry(a.country, selectedCountry)) {
        return false;
      }

      // 3. Retailer Filter
      if (selectedRetailer !== 'ALL' && a.account !== selectedRetailer) {
        return false;
      }

      return true;
    });
  }, [scorecardAccounts, searchQuery, selectedCountry, selectedRetailer]);

  // Pure Reactive Analytics computed by AnalyticsEngine
  const overviewKpis = useMemo(() => {
    return AnalyticsEngine.computeOverviewKpis(filteredScorecardProducts, filteredScorecardAccounts, programConfig);
  }, [filteredScorecardProducts, filteredScorecardAccounts, programConfig]);

  const sosDistribution = useMemo(() => {
    return AnalyticsEngine.computeShareOfShelf(filteredScorecardProducts, programConfig);
  }, [filteredScorecardProducts, programConfig]);

  const oemDistribution = useMemo(() => {
    return AnalyticsEngine.computeOemDistribution(filteredScorecardProducts);
  }, [filteredScorecardProducts]);

  const scorecardMetrics = useMemo(() => {
    return AnalyticsEngine.computeScorecardMetrics(filteredScorecardProducts);
  }, [filteredScorecardProducts]);

  const pricingMetrics = useMemo(() => {
    return AnalyticsEngine.computePricingMetrics(filteredScorecardProducts);
  }, [filteredScorecardProducts]);

  const coverageMetrics = useMemo(() => {
    return AnalyticsEngine.computeCoverageMetrics(filteredScorecardAccounts, filteredScorecardProducts, programConfig);
  }, [filteredScorecardAccounts, filteredScorecardProducts, programConfig]);

  // Backward compatibility for legacy product array
  const [products] = useState<ProductSKU[]>(() => {
    return (scorecardProducts as any[]).map((p, idx) => ({
      sku_id: p.product_id || `SKU-${p.sku_index || idx + 1}`,
      product_id: p.product_id || `SKU-${p.sku_index || idx + 1}`,
      product_title: p.product_title || 'Untitled Product',
      oem: p.oem || 'Generic',
      model_series: p.model || 'Standard',
      processor_brand: p.processor || 'Intel',
      processor_model: p.processor_model || 'Core',
      processor_generation: p.gen || '14th Gen',
      processor_series: p.processor_model || 'Core',
      processor_gen: p.gen || '14th Gen',
      is_intel_cpu: p.processor === 'Intel',
      gpu_model: p.graphic_card || 'Integrated Graphics',
      graphics_card: p.graphic_card || 'Integrated Graphics',
      ram_size: p.ram ? `${p.ram}GB` : '16GB',
      storage_size: p.storage ? `${p.storage}GB` : '512GB',
      storage_type: p.storage_type || 'SSD',
      screen_size: p.screen_size ? `${p.screen_size}"` : '15.6"',
      form_factor: p.form_factor || 'Laptop',
      operating_system: p.operating_system || 'Windows 11',
      current_price: p.selling_price || 0,
      original_price: p.original_price || p.selling_price || 0,
      currency: p.currency || 'USD',
      price_usd: p.usd_selling_price || p.selling_price || 0,
      discount_amount: p.discount_amount || 0,
      discount_pct: p.discount_pct || 0,
      retailer: p.account || 'Retailer',
      retailer_type: p['3p_1p'] === '1P' ? '1P Retailer' : '3P Marketplace',
      country: p.country || 'United States',
      availability: 'In Stock',
      brand_compliance_score: p.Overall ?? 0,
      s1_score: p.s1 ?? 0,
      s2_score: p.s2 ?? 0,
      p1_score: p.p1 ?? 0,
      p2_score: p.p2 ?? 0,
      p3_score: p.p3 ?? 0,
      p4_score: p.p4 ?? 0,
      p5_score: p.p5 ?? 0,
      segment: p.Gaming === 'Y' ? 'Gaming' : p.Evo === 'Y' ? 'AI PC (Core Ultra)' : 'Mainstream',
      intel_evo_certified: p.Evo === 'Y',
      intel_vpro: p.Vpro === 'Y',
      premier_sku: p.concatenate === 'Y' || p.Premium === 'Y',
      sourceUrl: p.product_url || '#',
      sourceType: 'Retailer PDP',
      scrapedAt: p.scraped_at || '2026-08-27',
      cachedAt: p.scraped_at || '2026-08-27',
      scrapeMethod: p.extraction_method || 'Bright Data',
      status: 'SUCCESS',
      confidence: 0.98,
      price_history: (p.price_history && Array.isArray(p.price_history) ? p.price_history : []).map((ph: any) => ({
        date: ph?.date || p.date || '2026-08-27',
        price: ph?.selling_price || p.selling_price || 0,
        price_usd: ph?.usd_selling_price || p.usd_selling_price || p.selling_price || 0,
        retailer: ph?.account || p.account || 'Retailer'
      }))
    })) as any;
  });

  const filteredProducts = useMemo(() => {
    return products.filter((p) => {
      if (searchQuery) {
        const q = searchQuery.toLowerCase().trim();
        if (!p.product_title.toLowerCase().includes(q) && !p.retailer.toLowerCase().includes(q)) return false;
      }
      if (selectedCountry !== 'ALL' && !matchCountry(p.country, selectedCountry)) return false;
      if (selectedRetailer !== 'ALL' && p.retailer !== selectedRetailer) return false;
      return true;
    });
  }, [products, searchQuery, selectedCountry, selectedRetailer]);

  // Legacy retailers
  const retailers: Retailer[] = useMemo(() => {
    return filteredScorecardAccounts.map((a) => ({
      id: a.account.toLowerCase().replace(/\s+/g, '-'),
      name: a.account,
      domain: a.website.replace('https://', '').replace('http://', '').replace('/', ''),
      country: a.country,
      type: a.account_type as any,
      products_count: a.products_count,
      intel_skus_count: a.intel_skus_count,
      competitor_skus_count: a.competitor_skus_count,
      brand_compliance_score: a.Overall_score,
      laptop_compliance_score: a.laptop_score,
      desktop_compliance_score: a.desktop_score,
      compliance_grade: a.Overall_score >= 85 ? 'A (Exemplary)' : a.Overall_score >= 70 ? 'B (Compliant)' : 'C (Needs Remediation)',
      last_successful_crawl: a.last_successful_crawl,
      data_freshness: a.data_freshness,
      extraction_success_rate: a.extraction_success_rate,
      cached_pages_count: a.cached_pages_count,
      live_requests_count: a.live_requests_count,
      brightdata_requests_count: a.brightdata_requests_count,
      status: 'ACTIVE_POC',
      data_source_mode: 'Real Scraped Data',
    }));
  }, [filteredScorecardAccounts]);

  const [banners] = useState<Banner[]>(() => {
    return (SCORECARD_BANNERS as any[]).map((b) => ({
      banner_id: b.banner_id,
      retailer: b.account,
      country: b.country,
      placement_type: b.banner_type,
      brand: b.banner_brand,
      position: 'Hero',
      intel_branded: b.banner_brand.includes('Intel'),
      headline: b.headline,
      subheadline: b.subheadline,
      subtext: b.subheadline,
      destination_url: b.destination_url,
      has_destination_link: b.has_destination_link,
      promoted_discount: b.discount,
      discount_text: b.discount,
      screenshot_url: b.screenshot,
      first_seen: b.first_seen,
      last_seen: b.last_seen,
      campaign_theme: 'AI PC Campaign',
      status: 'Active',
      data_source: 'Bright Data',
    })) as any;
  });

  const [keywords] = useState<KeywordSOV[]>(() => {
    return (SCORECARD_KEYWORDS as any[]).map((k) => ({
      keyword: k.Intel_keyword,
      search_volume_monthly: k.search_volume,
      intel_share_of_voice: k.intel_share_pct,
      intel_share_pct: k.intel_share_pct,
      sponsored_sov: k.sponsored_intel_share_pct,
      sponsored_intel_share_pct: k.sponsored_intel_share_pct,
      organic_sov: k.intel_presence_pct,
      top_intel_sku: k.top_ranked_sku,
      top_competitor_sku: 'Competitor Alternate SKU',
      retailer_breakdown: k.retailer_breakdown,
      intel_count: k.intel_product_count,
      amd_count: k.competitor_product_count,
      qualcomm_count: 0,
      apple_count: 0,
      other_count: 0,
      total_results: k.total_results,
      scoring_eligible_results: k.scoring_eligible_results
    })) as any;
  });

  const [scrapeJobs, setScrapeJobs] = useState<ScrapeJob[]>([
    {
      id: 'job-101',
      url: 'https://www.bestbuy.com/site/dell-xps-13-plus/6573821.p',
      retailer: 'Best Buy',
      country: 'US',
      reason: 'Automated Catalog Refresh',
      method: 'Cached',
      cache_status: 'HIT',
      priority: 'NORMAL',
      status: 'SUCCESS',
      failure_reason: 'None',
      brightdata_request_count: 0,
      duration_ms: 24,
      fields_extracted: 18,
      timestamp: '2026-08-27 02:50:12',
    },
    {
      id: 'job-102',
      url: 'https://www.walmart.com/ip/HP-Pavilion-15-Laptop/54321987',
      retailer: 'Walmart',
      country: 'US',
      reason: 'Price Corridor Monitoring',
      method: 'Cached',
      cache_status: 'HIT',
      priority: 'NORMAL',
      status: 'SUCCESS',
      failure_reason: 'None',
      brightdata_request_count: 0,
      duration_ms: 18,
      fields_extracted: 18,
      timestamp: '2026-08-27 02:50:14',
    },
    {
      id: 'job-103',
      url: 'https://www.costco.com/lenovo-ideapad-slim-5-16.product.1793284.html',
      retailer: 'Costco',
      country: 'US',
      reason: 'Single SKU Live Probe',
      method: 'Bright Data',
      cache_status: 'MISS',
      priority: 'HIGH',
      status: 'SUCCESS',
      failure_reason: 'None',
      brightdata_request_count: 1,
      duration_ms: 1620,
      fields_extracted: 18,
      timestamp: '2026-08-27 02:50:16',
    },
  ]);

  const executeLiveValidation = async (sku: any): Promise<{ success: boolean; fromCache: boolean }> => {
    setCostMetrics((prev) => ({
      ...prev,
      cached_requests: prev.cached_requests + 1,
      cache_hit_rate_pct: Math.round(((prev.cached_requests + 1) / (prev.used_requests + prev.cached_requests + 1)) * 1000) / 10,
    }));

    const newJob: ScrapeJob = {
      id: `job-${Date.now()}`,
      url: sku.product_url || sku.sourceUrl || 'https://www.intel.com',
      retailer: sku.account || sku.retailer || 'Retailer',
      country: sku.country || 'US',
      reason: `Live Validation: ${sku.oem || ''} ${sku.model || ''}`,
      method: 'Cached',
      cache_status: 'HIT',
      priority: 'NORMAL',
      status: 'CACHED',
      failure_reason: 'None',
      brightdata_request_count: 0,
      duration_ms: 18,
      fields_extracted: 18,
      timestamp: new Date().toISOString().replace('T', ' ').slice(0, 19),
    };

    setScrapeJobs((prev) => [newJob, ...prev]);
    return { success: true, fromCache: true };
  };

  const executeRunSample = async (retailer: string, count: number, mode: string) => {
    const limitedCount = Math.min(count, guardrails.session_limit);
    setCostMetrics((prev) => ({
      ...prev,
      used_requests: prev.used_requests + limitedCount,
      estimated_cost_usd: Math.round((prev.estimated_cost_usd + limitedCount * 0.02) * 100) / 100,
    }));
  };

  const updateGuardrails = (newG: CostGuardrails) => {
    setGuardrails(newG);
  };

  const resetFilters = () => {
    setSearchQuery('');
    setSelectedCountry('ALL');
    setSelectedRetailer('ALL');
    setSelectedCategory('ALL');
    setSelectedSegment('ALL');
    setSelectedFormFactor('ALL');
  };

  return (
    <AppContext.Provider
      value={{
        activeTab,
        setActiveTab,
        products,
        filteredProducts,
        scorecardProducts,
        filteredScorecardProducts,
        scorecardAccounts,
        filteredScorecardAccounts,
        retailers,
        banners,
        keywords,
        scrapeJobs,
        costMetrics,
        guardrails,
        sosData,
        sovData,
        pricingData,
        evoData,
        cpuData,
        regionalData,
        screenshotIndex,
        searchQuery,
        setSearchQuery,
        selectedCountry,
        setSelectedCountry,
        selectedRetailer,
        setSelectedRetailer,
        selectedCategory,
        setSelectedCategory,
        selectedSegment,
        setSelectedSegment,
        selectedFormFactor,
        setSelectedFormFactor,
        dateRange,
        setDateRange,
        selectedSkuDetail,
        setSelectedSkuDetail,
        selectedRetailerDetail,
        setSelectedRetailerDetail,
        liveValidationTarget,
        setLiveValidationTarget,
        runSampleModalOpen,
        setRunSampleModalOpen,
        settingsModalOpen,
        setSettingsModalOpen,
        sourceEvidenceTarget,
        setSourceEvidenceTarget,
        reportPreviewTarget,
        setReportPreviewTarget,
        programConfig,
        updateProgramConfig,
        overviewKpis,
        sosDistribution,
        oemDistribution,
        scorecardMetrics,
        pricingMetrics,
        coverageMetrics,
        setRawProducts,
        setRawAccounts,
        clearData,
        resetToFullLiveDataset,
        executeLiveValidation,
        executeRunSample,
        updateGuardrails,
        resetFilters,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};
