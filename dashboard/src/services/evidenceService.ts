import {
  EvidenceRecord,
  ProductScorecardEvidenceMap,
  EvidenceHealthSummary,
  VerificationStatus,
  ScoreComponent,
} from '../types/evidence';
import { ScorecardSKU } from '../types/scorecards';
import { EvidenceRuleEngine } from './evidenceRuleEngine';

export class EvidenceService {
  /**
   * Builds and retrieves the full deterministic evidence map for a given SKU.
   */
  static getProductEvidenceMap(sku: ScorecardSKU): ProductScorecardEvidenceMap {
    return EvidenceRuleEngine.buildProductEvidenceMap(sku);
  }

  /**
   * Retrieves all evidence records for a given product or product ID from an active SKU array.
   */
  static getEvidenceBySku(productOrId: string | ScorecardSKU, products: ScorecardSKU[] = []): EvidenceRecord[] {
    const sku = typeof productOrId === 'object' ? productOrId : products.find((p) => p.product_id === productOrId);
    if (!sku) return [];
    const map = EvidenceRuleEngine.buildProductEvidenceMap(sku);
    return [
      map.components.s1,
      map.components.s2,
      map.components.p1,
      map.components.p2,
      map.components.p3,
      map.components.p4,
      map.components.p5,
      map.price_evidence,
    ];
  }

  /**
   * Retrieves all evidence records matching a specific rule ID across products.
   */
  static getEvidenceByRule(ruleId: string, products: ScorecardSKU[] = []): EvidenceRecord[] {
    const all = this.getAllEvidenceRecords(products);
    return all.filter((r) => r.ruleId === ruleId || r.rule_id === ruleId);
  }

  /**
   * Retrieves a specific score component evidence record for a product.
   */
  static getEvidenceByScore(
    productOrId: string | ScorecardSKU,
    scoreComponent: ScoreComponent,
    products: ScorecardSKU[] = []
  ): EvidenceRecord | null {
    const sku = typeof productOrId === 'object' ? productOrId : products.find((p) => p.product_id === productOrId);
    if (!sku) return null;
    const map = EvidenceRuleEngine.buildProductEvidenceMap(sku);

    switch (scoreComponent) {
      case 'S1': return map.components.s1;
      case 'S2': return map.components.s2;
      case 'P1': return map.components.p1;
      case 'P2': return map.components.p2;
      case 'P3': return map.components.p3;
      case 'P4': return map.components.p4;
      case 'P5': return map.components.p5;
      case 'PRICE': return map.price_evidence;
      default: return null;
    }
  }

  /**
   * Extracts flat list of all component evidence records across all active products.
   */
  static getAllEvidenceRecords(products: ScorecardSKU[] = []): EvidenceRecord[] {
    const records: EvidenceRecord[] = [];
    products.forEach((sku) => {
      const map = EvidenceRuleEngine.buildProductEvidenceMap(sku);
      records.push(map.components.s1);
      records.push(map.components.s2);
      records.push(map.components.p1);
      records.push(map.components.p2);
      records.push(map.components.p3);
      records.push(map.components.p4);
      records.push(map.components.p5);
      records.push(map.price_evidence);
    });
    return records;
  }

  /**
   * Computes dynamic Evidence Health and Provenance Completeness across all active records.
   * Does NOT count unverified records as verified.
   */
  static getEvidenceCompleteness(products: ScorecardSKU[] = []): EvidenceHealthSummary {
    return this.computeEvidenceHealthSummary(products);
  }

  /**
   * Computes dynamic Evidence Health summary metrics.
   */
  static computeEvidenceHealthSummary(products: ScorecardSKU[] = []): EvidenceHealthSummary {
    if (products.length === 0) {
      return {
        total_score_records: 0,
        scorecard_component_records: 0,
        commercial_price_records: 0,
        verified_records: 0,
        partially_verified_records: 0,
        unverified_records: 0,
        insufficient_evidence_records: 0,
        scorecard_verified_records: 0,
        scorecard_partially_verified_records: 0,
        scorecard_insufficient_records: 0,
        verification_coverage_pct: 0,
        scorecard_coverage_pct: 0,
        screenshot_coverage_pct: 0,
        source_url_coverage_pct: 0,
        timestamp_coverage_pct: 0,
        provenance_coverage_pct: 0,
      };
    }

    const allRecords = this.getAllEvidenceRecords(products);
    const total_score_records = allRecords.length;

    const scorecardRecords = allRecords.filter((r) => r.scoreComponent !== 'PRICE');
    const priceRecords = allRecords.filter((r) => r.scoreComponent === 'PRICE');

    const verified_records = allRecords.filter((r) => r.verificationStatus === 'VERIFIED').length;
    const partially_verified_records = allRecords.filter((r) => r.verificationStatus === 'PARTIALLY_VERIFIED').length;
    const unverified_records = allRecords.filter((r) => r.verificationStatus === 'UNVERIFIED').length;
    const insufficient_evidence_records = allRecords.filter((r) => r.verificationStatus === 'INSUFFICIENT_EVIDENCE').length;

    const scorecard_verified_records = scorecardRecords.filter((r) => r.verificationStatus === 'VERIFIED').length;
    const scorecard_partially_verified_records = scorecardRecords.filter((r) => r.verificationStatus === 'PARTIALLY_VERIFIED').length;
    const scorecard_insufficient_records = scorecardRecords.filter((r) => r.verificationStatus === 'INSUFFICIENT_EVIDENCE').length;

    const screenshotCount = products.filter((p: any) => Boolean(p.product_screenshot || p.screenshot_url || p.screenshot_path || p.screenshot_available)).length;
    const sourceUrlCount = products.filter((p) => Boolean(p.product_url && p.product_url.startsWith('http'))).length;
    const timestampCount = products.filter((p) => Boolean(p.date || p.scraped_at)).length;
    const provenanceCount = products.filter((p) => Boolean(p.extraction_method && p.source)).length;

    const verification_coverage_pct = total_score_records > 0
      ? Math.round(((verified_records + partially_verified_records * 0.5) / total_score_records) * 1000) / 10
      : 0;

    const scorecard_coverage_pct = scorecardRecords.length > 0
      ? Math.round(((scorecard_verified_records + scorecard_partially_verified_records * 0.5) / scorecardRecords.length) * 1000) / 10
      : 0;

    return {
      total_score_records,
      scorecard_component_records: scorecardRecords.length,
      commercial_price_records: priceRecords.length,
      verified_records,
      partially_verified_records,
      unverified_records,
      insufficient_evidence_records,
      scorecard_verified_records,
      scorecard_partially_verified_records,
      scorecard_insufficient_records,
      verification_coverage_pct,
      scorecard_coverage_pct,
      screenshot_coverage_pct: Math.round((screenshotCount / products.length) * 1000) / 10,
      source_url_coverage_pct: Math.round((sourceUrlCount / products.length) * 1000) / 10,
      timestamp_coverage_pct: Math.round((timestampCount / products.length) * 1000) / 10,
      provenance_coverage_pct: Math.round((provenanceCount / products.length) * 1000) / 10,
    };
  }

  /**
   * Searches and filters evidence records.
   */
  static searchEvidence(
    products: ScorecardSKU[] = [],
    query: string = '',
    filters: {
      retailer?: string;
      country?: string;
      status?: VerificationStatus | 'ALL';
      component?: string | 'ALL';
    } = {}
  ): EvidenceRecord[] {
    let records = this.getAllEvidenceRecords(products);

    if (query) {
      const q = query.toLowerCase().trim();
      records = records.filter(
        (r) =>
          r.id.toLowerCase().includes(q) ||
          (r.productId && r.productId.toLowerCase().includes(q)) ||
          (r.productTitle && r.productTitle.toLowerCase().includes(q)) ||
          (r.retailer && r.retailer.toLowerCase().includes(q)) ||
          (r.ruleId && r.ruleId.toLowerCase().includes(q)) ||
          (r.detectedValue && String(r.detectedValue).toLowerCase().includes(q))
      );
    }

    if (filters.retailer && filters.retailer !== 'ALL') {
      records = records.filter((r) => r.retailer === filters.retailer || r.account === filters.retailer);
    }

    if (filters.country && filters.country !== 'ALL') {
      records = records.filter((r) => r.country === filters.country);
    }

    if (filters.status && filters.status !== 'ALL') {
      records = records.filter((r) => r.verificationStatus === filters.status);
    }

    if (filters.component && filters.component !== 'ALL') {
      records = records.filter((r) => r.scoreComponent === filters.component || r.component === filters.component);
    }

    return records;
  }
}
