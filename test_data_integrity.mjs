import { PROGRAM_CONFIG } from './dashboard/src/config/programConfig.js';
import { AnalyticsEngine } from './dashboard/src/services/analyticsEngine.js';
import { LIVE_52_SKU_DATASET, SCORECARD_ACCOUNTS, SCORECARD_KEYWORDS } from './dashboard/src/data/scorecardsData.js';

console.log('====================================================');
console.log('🧪 RUNNING COMPREHENSIVE DATA INTEGRITY VALIDATION');
console.log('====================================================\n');

let passedTests = 0;
let totalTests = 0;

function assert(condition, message) {
  totalTests++;
  if (!condition) {
    console.error(`❌ FAILED: ${message}`);
    process.exit(1);
  } else {
    console.log(`✅ PASSED: ${message}`);
    passedTests++;
  }
}

// TEST 1: ZERO-DATA / EMPTY DATASET TEST (Mandatory Criterion 43)
console.log('\n--- TEST 1: MANDATORY ZERO-DATA EMPTY DATASET TEST ---');
const emptyProducts = [];
const emptyAccounts = [];

const emptyKpis = AnalyticsEngine.computeOverviewKpis(emptyProducts, emptyAccounts, PROGRAM_CONFIG);
assert(emptyKpis.totalSkus === 0, 'Zero-data totalSkus must be 0');
assert(emptyKpis.totalAccounts === 0, 'Zero-data totalAccounts must be 0');
assert(emptyKpis.intelSkus === 0, 'Zero-data intelSkus must be 0');
assert(emptyKpis.intelSosPct === null, 'Zero-data intelSosPct must be null (NO FAKE PERCENTAGES)');
assert(emptyKpis.averageIntelSovPct === null, 'Zero-data averageIntelSovPct must be null');
assert(emptyKpis.avgOverallScore === null, 'Zero-data avgOverallScore must be null (NO FAKE 78 OR 80)');
assert(emptyKpis.avgSellingPriceUsd === null, 'Zero-data avgSellingPriceUsd must be null');

const emptySos = AnalyticsEngine.computeShareOfShelf(emptyProducts, PROGRAM_CONFIG);
assert(emptySos.length === 0, 'Zero-data SOS breakdown must be an empty array');

const emptyOem = AnalyticsEngine.computeOemDistribution(emptyProducts);
assert(emptyOem.length === 0, 'Zero-data OEM distribution must be an empty array');

const emptyScores = AnalyticsEngine.computeScorecardMetrics(emptyProducts);
assert(emptyScores.avgOverall === null, 'Zero-data scorecard avgOverall must be null');
assert(emptyScores.avgS1 === null, 'Zero-data scorecard avgS1 must be null');

const emptyPricing = AnalyticsEngine.computePricingMetrics(emptyProducts);
assert(emptyPricing.avgPriceUsd === null, 'Zero-data pricing avgPriceUsd must be null');
assert(emptyPricing.priceTiers.length === 0, 'Zero-data price tiers must be empty');

const emptyCoverage = AnalyticsEngine.computeCoverageMetrics(emptyAccounts, emptyProducts, PROGRAM_CONFIG);
assert(emptyCoverage.targetAccountsCount === 0, 'Empty coverage target accounts must be 0');
assert(emptyCoverage.actualExtractedSkus === 0, 'Empty coverage extracted SKUs must be 0');
assert(emptyCoverage.coveragePct === null, 'Empty coverage percentage must be null (NO FAKE NUMBER)');


// TEST 2: SUBSET DATASET TEST (10 Retailers / 50 SKUs)
console.log('\n--- TEST 2: SUBSET DATASET TEST (10 Retailers / 50 SKUs) ---');
const sampleAccounts = SCORECARD_ACCOUNTS.slice(0, 10);
const sampleProducts = LIVE_52_SKU_DATASET.slice(0, 50);

const sampleKpis = AnalyticsEngine.computeOverviewKpis(sampleProducts, sampleAccounts, PROGRAM_CONFIG);
assert(sampleKpis.totalSkus === 50, 'Subset totalSkus must match exactly 50');
assert(sampleKpis.totalAccounts === 10, 'Subset totalAccounts must match exactly 10');
assert(typeof sampleKpis.intelSosPct === 'number', 'Subset intelSosPct must be dynamically calculated number');
assert(sampleKpis.intelSkus <= 50, 'Subset Intel SKUs must be <= 50');


// TEST 3: FULL LIVE DATASET DYNAMIC METRICS TEST
console.log('\n--- TEST 3: FULL LIVE DATASET DYNAMIC METRICS TEST ---');
const fullKpis = AnalyticsEngine.computeOverviewKpis(LIVE_52_SKU_DATASET, SCORECARD_ACCOUNTS, PROGRAM_CONFIG);
assert(fullKpis.totalSkus === LIVE_52_SKU_DATASET.length, `Full totalSkus must equal ${LIVE_52_SKU_DATASET.length}`);
assert(fullKpis.totalAccounts === SCORECARD_ACCOUNTS.length, `Full totalAccounts must equal ${SCORECARD_ACCOUNTS.length}`);
const expectedCountryCount = new Set(SCORECARD_ACCOUNTS.map(a => a.country)).size;
assert(fullKpis.totalCountries === expectedCountryCount, `Full totalCountries must equal dynamic distinct count (${expectedCountryCount})`);
assert(fullKpis.intelSkus > 0, 'Full Intel SKUs must be > 0');
const expectedSos = Math.round((fullKpis.intelSkus / fullKpis.totalSkus) * 1000) / 10;
assert(fullKpis.intelSosPct === expectedSos, `Full Intel SOS % (${fullKpis.intelSosPct}%) must match exact mathematical ratio (${expectedSos}%)`);

const fullSos = AnalyticsEngine.computeShareOfShelf(LIVE_52_SKU_DATASET, PROGRAM_CONFIG);
assert(fullSos.length >= 4, 'Full SOS distribution must dynamically classify multiple processor families');
const intelSosEntry = fullSos.find(s => s.name.includes('Intel'));
assert(intelSosEntry !== undefined, 'SOS distribution must include Intel');

const fullOem = AnalyticsEngine.computeOemDistribution(LIVE_52_SKU_DATASET);
assert(fullOem.length > 0, 'Full OEM distribution must dynamically extract all OEMs');
assert(fullOem.some(o => o.oem === 'Dell' || o.oem === 'HP' || o.oem === 'Lenovo'), 'OEM distribution contains major OEMs');

const fullPricing = AnalyticsEngine.computePricingMetrics(LIVE_52_SKU_DATASET);
assert(fullPricing.avgPriceUsd > 500, 'Average selling price must be realistic (> $500)');
assert(fullPricing.minPriceUsd > 0, 'Min price must be > 0');
assert(fullPricing.maxPriceUsd > fullPricing.minPriceUsd, 'Max price must be > Min price');
assert(fullPricing.priceTiers.length === 4, 'Price tiers must have 4 brackets');

const fullCoverage = AnalyticsEngine.computeCoverageMetrics(SCORECARD_ACCOUNTS, LIVE_52_SKU_DATASET, PROGRAM_CONFIG);
assert(fullCoverage.targetAccountsCount === 52, 'Target accounts count must equal 52');
assert(fullCoverage.targetSkusCount === 52 * PROGRAM_CONFIG.target_skus_per_retailer, `Target SKUs must equal 52 * ${PROGRAM_CONFIG.target_skus_per_retailer}`);
assert(fullCoverage.actualExtractedSkus === LIVE_52_SKU_DATASET.length, 'Actual extracted SKUs must equal active dataset length');


// TEST 4: DYNAMIC CONFIGURATION PROPAGATION TEST
console.log('\n--- TEST 4: DYNAMIC CONFIGURATION PROPAGATION TEST ---');
const customConfig = {
  ...PROGRAM_CONFIG,
  target_skus_per_retailer: 20
};
const customCoverage = AnalyticsEngine.computeCoverageMetrics(SCORECARD_ACCOUNTS, LIVE_52_SKU_DATASET, customConfig);
assert(customCoverage.targetSkusCount === 52 * 20, 'Target SKUs must reactively update to 52 * 20 (1040) when config changes');

console.log('\n====================================================');
console.log(`🎉 ALL ${passedTests}/${totalTests} DATA INTEGRITY TESTS PASSED SUCCESSFULLY!`);
console.log('====================================================\n');
