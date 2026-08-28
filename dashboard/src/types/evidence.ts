/**
 * Canonical Evidence Layer Data Model
 * Intel Scorecards Intelligence Platform
 *
 * This file defines the core type contracts for verifiable, auditable evidence.
 * All fields use honest nullability (no forced fake values).
 */

// ============================================================
// 1. Core Enumerations and Unions
// ============================================================

/**
 * Supported Evidence Types (Exact Union per Spec)
 */
export type EvidenceType =
  | 'LISTING_EVIDENCE'
  | 'PDP_EVIDENCE'
  | 'SCREENSHOT_EVIDENCE'
  | 'TEXT_EVIDENCE'
  | 'IMAGE_EVIDENCE'
  | 'BADGE_EVIDENCE'
  | 'RICH_MEDIA_EVIDENCE'
  | 'PRICE_EVIDENCE'
  | 'PRODUCT_ATTRIBUTE_EVIDENCE'
  | 'SEARCH_RESULT_EVIDENCE'
  | 'BANNER_EVIDENCE';

/**
 * Verification States (Exact Union per Spec)
 *
 * - VERIFIED: The available source evidence directly supports the claim.
 * - PARTIALLY_VERIFIED: Some evidence exists, but does not completely establish the claim.
 * - UNVERIFIED: The claim cannot currently be verified from captured evidence.
 * - INSUFFICIENT_EVIDENCE: The required source material was not captured or is insufficient.
 */
export type VerificationStatus =
  | 'VERIFIED'
  | 'PARTIALLY_VERIFIED'
  | 'UNVERIFIED'
  | 'INSUFFICIENT_EVIDENCE';

/**
 * Result of the Evidence / Rule Evaluation
 */
export type EvidenceResult =
  | 'PASS'
  | 'FAIL'
  | 'UNVERIFIED';

/** Alias for backward compatibility */
export type AuditRuleResult = EvidenceResult | 'INSUFFICIENT_EVIDENCE';

/**
 * Scorecards Evaluation Components Supported by Evidence
 */
export type ScoreComponent =
  | 'S1'
  | 'S2'
  | 'P1'
  | 'P2'
  | 'P3'
  | 'P4'
  | 'P5'
  | 'PRICE'
  | 'ATTRIBUTE'
  | 'SOS'
  | 'SOV';

/**
 * Canonical Page Types
 */
export type EvidencePageType =
  | 'LISTING'
  | 'PDP'
  | 'SEARCH'
  | 'BANNER';

/**
 * Canonical Extraction Methods
 */
export type EvidenceExtractionMethod =
  | 'CACHE'
  | 'SDK'
  | 'SERP'
  | 'BRIGHT_DATA';

/**
 * Media Evidence Categories
 */
export type MediaType =
  | 'IMAGE'
  | 'VIDEO'
  | 'IFRAME'
  | 'HTML'
  | 'OTHER';

// ============================================================
// 2. Structured Provenance & Evidence Containers
// ============================================================

/**
 * Raw Captured Evidence Container
 * Retains exact un-normalized strings, HTML snippets, and attribute dictionaries.
 */
export interface RawEvidence {
  text?: string | null;
  html?: string | null;
  attributes?: Record<string, unknown> | null;
  metadata?: Record<string, unknown> | null;
}

/**
 * Detection Details Container
 * Explains what was detected, where it was detected, and selector context.
 */
export interface DetectionDetail {
  field?: string | null;
  value?: string | number | boolean | null;
  text?: string | null;
  selector?: string | null;
  attribute?: string | null;
  reason?: string | null;
}

/**
 * Structured Source & Provenance
 */
export interface EvidenceSource {
  url: string;
  pageType: EvidencePageType;
  capturedAt: string; // ISO 8601 or captured timestamp string
  extractionMethod: EvidenceExtractionMethod;
  extractionId?: string | null;
  providerRequestId?: string | null; // e.g. Bright Data request ID if present
}

/**
 * Visual Screenshot Evidence Reference
 */
export interface ScreenshotEvidence {
  screenshotUrl?: string | null;
  screenshotTimestamp?: string | null;
  screenshotPageType?: EvidencePageType | null;
  storagePath?: string | null;
}

/**
 * Rich Media Evidence Reference
 */
export interface MediaEvidence {
  mediaType: MediaType;
  mediaUrl?: string | null;
  sourceElement?: string | null;
  metadata?: Record<string, unknown> | null;
}

/**
 * Versioned Rule Reference
 */
export interface RuleReference {
  ruleId: string;
  ruleVersion: string;
}

/**
 * Score Association Reference
 */
export interface ScoreReference {
  scoreComponent?: ScoreComponent | null;
  scoreId?: string | null;
  scoreAwarded?: number | null; // 0-100 or null if unverified
}

/**
 * Audit Rule Definition Contract
 */
export interface AuditRule {
  rule_id: string;
  rule_name: string;
  rule_version: string;
  description: string;
  component: ScoreComponent;
  input_evidence_type: EvidenceType;
  evaluation_standard: string;
}

// ============================================================
// 3. Canonical Evidence Record
// ============================================================

/**
 * Canonical Immutable Evidence Record
 * Connects product claims to exact source URLs, timestamps, detection text, and rules.
 */
export interface EvidenceRecord {
  // Primary Identifiers
  id: string; // e.g. "ev-s1-sku123"
  evidence_id?: string; // Compatibility alias to id
  evidenceType: EvidenceType;
  verificationStatus: VerificationStatus;
  verification_status?: VerificationStatus; // Compatibility alias
  result: EvidenceResult;

  // Product Context
  productId?: string | null;
  product_id?: string; // Compatibility alias
  productUrl?: string | null;
  product_url?: string; // Compatibility alias
  productTitle?: string | null;
  product_title?: string; // Compatibility alias

  // Account / Retailer Context
  retailer?: string | null;
  country?: string | null;
  account?: string | null;

  // Page & Provenance Context
  pageType?: EvidencePageType | string | null;
  page_type?: EvidencePageType | string; // Compatibility alias
  sourceUrl?: string | null;
  source_url?: string; // Compatibility alias
  captureTimestamp?: string | null;
  capture_timestamp?: string; // Compatibility alias
  extractionId?: string | null;
  extraction_id?: string; // Compatibility alias
  extractionMethod?: EvidenceExtractionMethod | string | null;
  extraction_method?: string; // Compatibility alias
  providerRequestId?: string | null; // Optional Bright Data request ID

  // Rule & Scoring Context
  ruleId?: string | null;
  rule_id?: string; // Compatibility alias
  rule_name?: string; // Compatibility alias
  ruleVersion?: string | null;
  rule_version?: string; // Compatibility alias
  scoreComponent?: ScoreComponent | null;
  component?: ScoreComponent; // Compatibility alias
  scoreReference?: ScoreReference | null;
  score_awarded?: number | null; // Compatibility alias

  // Detection & Value Context
  detectedValue?: string | number | boolean | null;
  detected_text?: string | null; // Compatibility alias
  detected_element?: string | null; // Compatibility alias
  attribute_name?: string | null; // Compatibility alias
  attribute_value?: string | number | null; // Compatibility alias
  detection_reason?: string; // Compatibility alias
  detection?: DetectionDetail | null;
  rawEvidence?: RawEvidence | null;
  raw_source_text?: string | null; // Compatibility alias

  // Visual & Media Assets
  screenshot?: ScreenshotEvidence | null;
  screenshotUrl?: string | null;
  screenshot_url?: string | null; // Compatibility alias
  screenshot_available?: boolean; // Compatibility alias
  media?: MediaEvidence | null;
  mediaUrl?: string | null;
  media_url?: string | null; // Compatibility alias

  // Immutable Metadata
  createdAt: string;
}

// ============================================================
// 4. Product-Level Evidence Aggregation Maps
// ============================================================

export interface ProductScorecardEvidenceMap {
  product_id: string;
  overall_score: number | null;
  overall_status: VerificationStatus;
  listing_s_score: number | null;
  details_p_score: number | null;
  components: {
    s1: EvidenceRecord;
    s2: EvidenceRecord;
    p1: EvidenceRecord;
    p2: EvidenceRecord;
    p3: EvidenceRecord;
    p4: EvidenceRecord;
    p5: EvidenceRecord;
  };
  price_evidence: EvidenceRecord;
  attribute_evidence: Record<string, EvidenceRecord>;
}

export interface EvidenceHealthSummary {
  total_score_records: number;
  scorecard_component_records: number;
  commercial_price_records: number;
  verified_records: number;
  partially_verified_records: number;
  unverified_records: number;
  insufficient_evidence_records: number;
  scorecard_verified_records: number;
  scorecard_partially_verified_records: number;
  scorecard_insufficient_records: number;
  verification_coverage_pct: number;
  scorecard_coverage_pct: number;
  screenshot_coverage_pct: number;
  source_url_coverage_pct: number;
  timestamp_coverage_pct: number;
  provenance_coverage_pct: number;
}
