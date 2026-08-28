import { EXTRACTION_WATERFALL } from '../src/data/scorecardsData.js';

export default function handler(req: any, res: any) {
  res.status(200).json({
    success: true,
    waterfall: EXTRACTION_WATERFALL,
    summary: {
      candidate_urls: EXTRACTION_WATERFALL.total_candidate_urls,
      cache_hit_rate_pct: EXTRACTION_WATERFALL.cache_hit_rate_pct,
      live_requests_used: EXTRACTION_WATERFALL.brightdata_required_urls,
      cost_avoidance_usd: EXTRACTION_WATERFALL.requests_avoided * 0.20,
      actual_cost_usd: EXTRACTION_WATERFALL.estimated_cost_usd
    },
    timestamp: new Date().toISOString()
  });
}
