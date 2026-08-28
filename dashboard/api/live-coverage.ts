import liveDataRaw from '../src/data/live_52_sku_dataset.json' with { type: 'json' };

export default function handler(req: any, res: any) {
  const { country, status, search } = req.query || {};

  let coverage = liveDataRaw.retailer_coverage;
  let heatmap = liveDataRaw.heatmap;

  if (country && country !== 'ALL') {
    coverage = coverage.filter(r => r.country.toLowerCase().includes(String(country).toLowerCase()));
    heatmap = heatmap.filter(h => h.country.toLowerCase().includes(String(country).toLowerCase()));
  }

  if (status && status !== 'ALL') {
    coverage = coverage.filter(r => r.status === status);
    heatmap = heatmap.filter(h => h.status === status);
  }

  if (search) {
    const q = String(search).toLowerCase();
    coverage = coverage.filter(r => r.account.toLowerCase().includes(q) || r.country.toLowerCase().includes(q));
    heatmap = heatmap.filter(h => h.account.toLowerCase().includes(q) || h.country.toLowerCase().includes(q));
  }

  res.status(200).json({
    success: true,
    total_retailers: coverage.length,
    summary: liveDataRaw.summary,
    retailer_coverage: coverage,
    heatmap,
    timestamp: new Date().toISOString()
  });
}
