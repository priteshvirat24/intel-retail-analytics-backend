import sovKeywordsData from '../src/data/canonical_sov_keywords.json' with { type: 'json' };

export default function handler(req: any, res: any) {
  const { retailer, search } = req.query || {};

  const matrix = sovKeywordsData.matrix;
  let results: Record<string, string[]> = {};

  if (retailer) {
    const key = Object.keys(matrix).find(k => k.toLowerCase().includes(String(retailer).toLowerCase()));
    if (key) {
      results[key] = matrix[key as keyof typeof matrix];
    }
  } else {
    results = matrix;
  }

  if (search) {
    const q = String(search).toLowerCase();
    const filtered: Record<string, string[]> = {};
    for (const [r, kws] of Object.entries(results)) {
      const matchKws = kws.filter(k => k.toLowerCase().includes(q));
      if (matchKws.length > 0) {
        filtered[r] = matchKws;
      }
    }
    results = filtered;
  }

  res.status(200).json({
    success: true,
    total_retailers: Object.keys(results).length,
    matrix: results,
    timestamp: new Date().toISOString()
  });
}
