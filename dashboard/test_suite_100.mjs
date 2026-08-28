import fs from 'fs';
import {
  SCORECARD_PRODUCTS,
  SCORECARD_ACCOUNTS,
  SCORECARD_KEYWORDS,
  SCORECARD_BANNERS,
  EXTRACTION_WATERFALL,
  PROGRAM_HISTORY_METRICS
} from './src/data/scorecardsData.js';

let passed = 0;
let failed = 0;
const results = [];

function assert(condition, testName, details = '') {
  if (condition) {
    passed++;
    results.push({ testName, status: 'PASS', details });
  } else {
    failed++;
    results.push({ testName, status: 'FAIL', details });
    console.error(`❌ FAIL: ${testName} - ${details}`);
  }
}

console.log('====================================================');
console.log('🚀 EXECUTING 100+ AUTOMATED TESTS FOR INTEL SCORECARDS');
console.log('====================================================\n');

// ----------------------------------------------------
// SUITE 1: 52 TARGET ACCOUNT VALIDATION (52 Tests)
// ----------------------------------------------------
console.log('▶ Running Suite 1: 52 Target Account Integrity Tests...');
SCORECARD_ACCOUNTS.forEach((account, idx) => {
  const hasValidFields =
    account.account &&
    account.country &&
    account.account_type &&
    account.website &&
    account.Overall_score >= 0 &&
    account.Overall_score <= 100 &&
    account.listing_s_score >= 0 &&
    account.details_p_score >= 0 &&
    account.products_count > 0;

  assert(
    hasValidFields,
    `[Account ${idx + 1}/52] Target "${account.account}" integrity`,
    `Country: ${account.country}, Type: ${account.account_type}, Score: ${account.Overall_score}%`
  );
});

// ----------------------------------------------------
// SUITE 2: 23 COUNTRY NORMALIZATION & FILTER TESTS (23 Tests)
// ----------------------------------------------------
console.log('\n▶ Running Suite 2: 23 Country Filter & Normalization Tests...');
const countryCodes = [
  { code: 'US', name: 'United States' },
  { code: 'CA', name: 'Canada' },
  { code: 'UK', name: 'United Kingdom' },
  { code: 'GB', name: 'United Kingdom' },
  { code: 'DE', name: 'Germany' },
  { code: 'FR', name: 'France' },
  { code: 'IT', name: 'Italy' },
  { code: 'ES', name: 'Spain' },
  { code: 'IN', name: 'India' },
  { code: 'JP', name: 'Japan' },
  { code: 'AU', name: 'Australia' },
  { code: 'BR', name: 'Brazil' },
  { code: 'MX', name: 'Mexico' },
  { code: 'CN', name: 'China' },
  { code: 'KR', name: 'South Korea' },
  { code: 'PL', name: 'Poland' },
  { code: 'SE', name: 'Sweden' },
  { code: 'NO', name: 'Norway' },
  { code: 'DK', name: 'Denmark' },
  { code: 'TR', name: 'Turkey' },
  { code: 'VN', name: 'Vietnam' },
  { code: 'CL', name: 'Chile' },
  { code: 'CO', name: 'Colombia' },
  { code: 'ID', name: 'Indonesia' },
];

function matchCountryTest(accountCountry, filter) {
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
  if (f === 'in' && (ac.includes('india') || ac === 'in')) return true;
  if (f === 'jp' && (ac.includes('japan') || ac === 'jp')) return true;
  if (f === 'au' && (ac.includes('australia') || ac === 'au')) return true;
  if (f === 'br' && (ac.includes('brazil') || ac === 'br')) return true;
  if (f === 'mx' && (ac.includes('mexico') || ac === 'mx')) return true;
  if (f === 'cn' && (ac.includes('china') || ac === 'cn')) return true;
  if (f === 'kr' && (ac.includes('korea') || ac === 'kr')) return true;
  if (f === 'pl' && (ac.includes('poland') || ac === 'pl')) return true;
  if (f === 'se' && (ac.includes('sweden') || ac === 'se')) return true;
  if (f === 'no' && (ac.includes('norway') || ac === 'no')) return true;
  if (f === 'dk' && (ac.includes('denmark') || ac === 'dk')) return true;
  if (f === 'tr' && (ac.includes('turkey') || ac === 'tr')) return true;
  if (f === 'vn' && (ac.includes('vietnam') || ac === 'vn')) return true;
  if (f === 'cl' && (ac.includes('chile') || ac === 'cl')) return true;
  if (f === 'co' && (ac.includes('colombia') || ac === 'co')) return true;
  if (f === 'id' && (ac.includes('indonesia') || ac === 'id')) return true;
  return false;
}

countryCodes.forEach((c) => {
  const matches = SCORECARD_ACCOUNTS.filter((a) => matchCountryTest(a.country, c.code));
  assert(
    matches.length > 0,
    `[Country Filter] Country Code "${c.code}" (${c.name}) matches > 0 accounts`,
    `Found ${matches.length} accounts matching ${c.code}`
  );
});

// ----------------------------------------------------
// SUITE 3: MATHEMATICAL SCORECARDS S1..P5 FORMULAS (15 Tests)
// ----------------------------------------------------
console.log('\n▶ Running Suite 3: Scorecards Formula & Rounding Tests...');
SCORECARD_PRODUCTS.slice(0, 15).forEach((sku, idx) => {
  const expectedListing = Math.round((sku.s1 + sku.s2) / 2);
  const expectedDetails = Math.round((sku.p1 + sku.p2 + sku.p3 + sku.p4 + sku.p5) / 5);
  const expectedOverall = Math.round((expectedListing + expectedDetails) / 2);

  const formulaMatches =
    sku.listing_s === expectedListing &&
    sku.details_p === expectedDetails &&
    sku.Overall === expectedOverall;

  assert(
    formulaMatches,
    `[Scoring Math ${idx + 1}/15] SKU "${sku.product_id}" S1..P5 formula check`,
    `Listing S: ${sku.listing_s} (exp: ${expectedListing}), Details P: ${sku.details_p} (exp: ${expectedDetails}), Overall: ${sku.Overall} (exp: ${expectedOverall})`
  );
});

// ----------------------------------------------------
// SUITE 4: SHARE OF SHELF & SHARE OF VOICE METHODOLOGY (10 Tests)
// ----------------------------------------------------
console.log('\n▶ Running Suite 4: SOS & SOV Methodology Tests...');
assert(
  SCORECARD_PRODUCTS.every((p) => p.page_rank <= 2),
  '[SOS Rule] All SOS products belong to Page 1 or 2',
  'First 2 category pages scope strictly satisfied'
);

assert(
  SCORECARD_PRODUCTS.every((p) => p.sos_eligible === true),
  '[SOS Rule] All sampled products have sos_eligible = true',
  'Explicit SOS eligibility flag present'
);

assert(
  SCORECARD_KEYWORDS.length === 10,
  '[SOV Rule] Exactly 10 Sampled Priority Keywords present',
  `Found ${SCORECARD_KEYWORDS.length} keywords`
);

SCORECARD_KEYWORDS.forEach((k) => {
  assert(
    k.search_volume > 0 && k.intel_share_pct > 0 && k.overall_score > 0,
    `[SOV Keyword] "${k.Intel_keyword}" metrics integrity`,
    `Vol: ${k.search_volume}, SOV: ${k.intel_share_pct}%, Score: ${k.overall_score}%`
  );
});

// ----------------------------------------------------
// SUITE 5: COST WATERFALL & HISTORICAL RECONCILIATION (10 Tests)
// ----------------------------------------------------
console.log('\n▶ Running Suite 5: Extraction Waterfall & Program History Tests...');
const waterfall = EXTRACTION_WATERFALL;
const waterfallSum =
  waterfall.cached_urls +
  waterfall.existing_dataset_urls +
  waterfall.sdk_urls +
  waterfall.serp_urls +
  waterfall.brightdata_required_urls;

assert(
  waterfallSum === waterfall.total_candidate_urls,
  '[Cost Waterfall] Candidate URLs reconcile across all tiers (1,000 total)',
  `Sum: ${waterfallSum} === Total: ${waterfall.total_candidate_urls}`
);

assert(
  waterfall.cache_hit_rate_pct === 92.6,
  '[Cost Waterfall] Aggressive cache hit rate equals 92.6%',
  `Cache Hit Rate: ${waterfall.cache_hit_rate_pct}%`
);

assert(
  waterfall.brightdata_required_urls === 5,
  '[Cost Waterfall] Bright Data is strictly rate-limited fallback (5 requests)',
  `Live Requests: ${waterfall.brightdata_required_urls}`
);

assert(
  PROGRAM_HISTORY_METRICS['2024'].accounts_count === 52,
  '[History 2024] 2024 program tracked 52 accounts',
  '52 accounts recorded'
);

assert(
  PROGRAM_HISTORY_METRICS['2024'].sos.total_products === 1437356,
  '[History 2024] 2024 SOS products equal 1,437,356',
  'Preserved official 2024 SOS count'
);

assert(
  PROGRAM_HISTORY_METRICS['2024'].sov.total_products === 4954024,
  '[History 2024] 2024 SOV products equal 4,954,024',
  'Preserved official 2024 SOV count'
);

assert(
  PROGRAM_HISTORY_METRICS['2025'].accounts_count === 50,
  '[History 2025] 2025 program tracks 50 tiered accounts',
  '50 tiered accounts recorded'
);

assert(
  PROGRAM_HISTORY_METRICS['2025'].account_changes.removed.includes('Dell OEM Store'),
  '[History 2025] OEM stores removed in 2025 program',
  'OEM store removals verified'
);

assert(
  PROGRAM_HISTORY_METRICS['2025'].account_changes.added.includes('BIC Camera - JP'),
  '[History 2025] BIC Camera added in 2025 program',
  'BIC Camera addition verified'
);

// ----------------------------------------------------
// SUITE 6: DATA ATTRIBUTE COMPLETENESS (10 Tests)
// ----------------------------------------------------
console.log('\n▶ Running Suite 6: 40+ Column Schema Completeness Tests...');
SCORECARD_PRODUCTS.slice(0, 10).forEach((p, idx) => {
  const hasFullAttributes =
    p.date &&
    p.month &&
    p.quarter &&
    p.year &&
    p.source &&
    p.country &&
    p.account &&
    p.form_factor &&
    p.product_url &&
    p.product_id &&
    p.product_title &&
    p.original_price > 0 &&
    p.selling_price > 0 &&
    p.usd_selling_price > 0 &&
    p.processor &&
    p.graphic_card &&
    p.Gaming &&
    p.Evo &&
    p.Vpro &&
    p.Premium &&
    p.Overall >= 0 &&
    p.listing_s >= 0 &&
    p.details_p >= 0 &&
    p.s1 >= 0 &&
    p.s2 >= 0 &&
    p.p1 >= 0 &&
    p.p2 >= 0 &&
    p.p3 >= 0 &&
    p.p4 >= 0 &&
    p.p5 >= 0 &&
    p.ram > 0 &&
    p.storage > 0 &&
    p.storage_type &&
    p.screen_size > 0 &&
    p.operating_system &&
    p.oem &&
    p.model &&
    p.gen &&
    p.processor_model &&
    p.number &&
    p['3p_1p'] &&
    p.Flag &&
    p.concatenate;

  assert(
    hasFullAttributes,
    `[Attribute Completeness ${idx + 1}/10] SKU "${p.product_id}" has all 40+ columns populated`,
    `OEM: ${p.oem}, Model: ${p.model}, Price: $${p.selling_price}`
  );
});

console.log('\n====================================================');
console.log(`🏁 TEST EXECUTION SUMMARY:`);
console.log(`   TOTAL TESTS RUN: ${passed + failed}`);
console.log(`   PASSED: ${passed}`);
console.log(`   FAILED: ${failed}`);
console.log(`   SUCCESS RATE: ${Math.round((passed / (passed + failed)) * 100)}%`);
console.log('====================================================');

if (failed > 0) {
  process.exit(1);
} else {
  process.exit(0);
}
