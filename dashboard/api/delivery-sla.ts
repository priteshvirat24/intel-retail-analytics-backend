import { DELIVERY_SCHEDULE_ITEMS, PROGRAM_HISTORY_METRICS } from '../src/data/scorecardsData.js';

export default function handler(req: any, res: any) {
  res.status(200).json({
    success: true,
    overall_sla_compliance_pct: 99.9,
    delivery_schedule: DELIVERY_SCHEDULE_ITEMS,
    program_summary: {
      active_program_year: 2025,
      monitored_accounts_count: 50,
      cadence_tiering: '22 Monthly / 6 Mid-Quarter / 22 Quarterly',
      flexible_account_pool: 63
    },
    timestamp: new Date().toISOString()
  });
}
