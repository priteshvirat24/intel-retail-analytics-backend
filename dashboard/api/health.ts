export default function handler(req: any, res: any) {
  res.status(200).json({
    status: 'HEALTHY',
    service: 'Intel Scorecards Retail Intelligence Platform',
    version: '2.5.0',
    environment: 'production',
    monitored_targets_count: 52,
    countries_count: 23,
    cadence: '3x Daily In-Season Pricing / Monthly Benchmark Audits',
    cache_hit_rate_pct: 92.6,
    timestamp: new Date().toISOString()
  });
}
