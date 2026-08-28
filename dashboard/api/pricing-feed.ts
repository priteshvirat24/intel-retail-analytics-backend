import { IN_SEASON_PRICING_SUMMARY, SCORECARD_PRODUCTS } from '../src/data/scorecardsData.js';

export default function handler(req: any, res: any) {
  res.status(200).json({
    success: true,
    cadence: '3x Daily In-Season Pricing Feed',
    scope: IN_SEASON_PRICING_SUMMARY,
    last_sync: '27/8/2026 12:00 UTC (Run 2 of 3 Daily)',
    pricing_feed_items: SCORECARD_PRODUCTS.map(p => ({
      product_id: p.product_id,
      product_title: p.product_title,
      account: p.account,
      country: p.country,
      processor: p.processor,
      processor_model: p.processor_model,
      original_price_usd: p.usd_original_price,
      current_price_usd: p.usd_selling_price,
      discount_pct: p.discount_pct,
      price_history: p.price_history
    })),
    timestamp: new Date().toISOString()
  });
}
