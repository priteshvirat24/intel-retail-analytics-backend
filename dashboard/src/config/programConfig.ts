/**
 * Intel Scorecards Centralized Program Configuration
 * Source of truth for all business rules, methodologies, weights, and safety limits.
 * Components must NEVER hardcode these values; they must consume this configuration.
 */

export interface ProgramConfig {
  program_name: string;
  version: string;
  scope_description: string;
  // Extraction & Scrape Target Defaults
  target_skus_per_retailer: number;
  safety_request_ceiling: number;
  max_retries_per_url: number;
  cache_ttl_days: number;
  rate_limit_rps: number;
  estimated_cost_per_bd_request_usd: number;
  // Category Weighting Methodology
  category_weights: {
    laptop: number;
    desktop: number;
  };
  // Scorecards Audit Weightings (S1, S2, P1, P2, P3, P4, P5)
  scorecard_weights: {
    s1: number; // Title Presence
    s2: number; // Search & Listing Badges
    p1: number; // Core Specs & Hierarchy
    p2: number; // Key Benefits & Content
    p3: number; // Rich Media & Assets
    p4: number; // Accuracy & Consistency
    p5: number; // Search Engine Optimization / Metadata
  };
  // Grade Thresholds
  grade_thresholds: {
    exemplary: number;
    compliant: number;
    needs_remediation: number;
  };
  // Competitor Classification Universe
  competitor_families: Array<{
    id: string;
    label: string;
    brand: string;
    color: string;
  }>;
  // Currency Conversion Rates to USD (for local price normalization)
  currency_rates_to_usd: Record<string, number>;
}

export const PROGRAM_CONFIG: ProgramConfig = {
  program_name: 'Intel Online Tracking & Retail Execution Intelligence',
  version: '2024-2025 Program Year',
  scope_description: 'Global 52-Retailer Omnichannel Tracking Universe',
  target_skus_per_retailer: 30,
  safety_request_ceiling: 200,
  max_retries_per_url: 1,
  cache_ttl_days: 7,
  rate_limit_rps: 5,
  estimated_cost_per_bd_request_usd: 0.20,
  category_weights: {
    laptop: 0.85,  // 85% Laptop Weighting
    desktop: 0.15, // 15% Desktop Weighting
  },
  scorecard_weights: {
    s1: 0.10,
    s2: 0.10,
    p1: 0.15,
    p2: 0.15,
    p3: 0.20,
    p4: 0.15,
    p5: 0.15,
  },
  grade_thresholds: {
    exemplary: 85,
    compliant: 70,
    needs_remediation: 0,
  },
  competitor_families: [
    { id: 'intel', label: 'Intel', brand: 'Intel', color: '#0071C5' },
    { id: 'amd', label: 'AMD', brand: 'AMD', color: '#ED1C24' },
    { id: 'apple', label: 'Apple', brand: 'Apple', color: '#555555' },
    { id: 'qualcomm', label: 'Qualcomm', brand: 'Qualcomm', color: '#3253DC' },
    { id: 'other', label: 'Other Processors', brand: 'Other', color: '#94A3B8' },
  ],
  currency_rates_to_usd: {
    USD: 1.0,
    EUR: 1.08,
    GBP: 1.28,
    CAD: 0.74,
    AUD: 0.65,
    BRL: 0.18,
    INR: 0.012,
    JPY: 0.0068,
    KRW: 0.00075,
    MXN: 0.051,
    CNY: 0.14,
    SGD: 0.76,
    PLN: 0.25,
    SEK: 0.096,
  },
};
