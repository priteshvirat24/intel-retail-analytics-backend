import React, { useState } from 'react';
import {
  Calendar,
  Layers,
  Search,
  Image,
  Store,
  TrendingDown,
  TrendingUp,
  AlertCircle,
  Clock,
  ArrowRight,
  History,
  CheckCircle2,
  Send,
  Zap,
  Server,
  FileSpreadsheet,
  Globe,
  Sliders
} from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend
} from 'recharts';
import {
  PROGRAM_HISTORY_METRICS,
  DELIVERY_SCHEDULE_ITEMS,
  IN_SEASON_PRICING_SUMMARY
} from '../data/scorecardsData';

export const ProgramHistoryView: React.FC = () => {
  const p2024 = PROGRAM_HISTORY_METRICS['2024'];
  const p2025 = PROGRAM_HISTORY_METRICS['2025'];
  const [activeHistoryTab, setActiveHistoryTab] = useState<'comparison' | 'delivery-schedule' | 'in-season-scope' | '2024' | '2025' | 'cadence'>('comparison');

  const comparisonRows = [
    { metric: 'Accounts Monitored', y2024: '52 Accounts (from March)', y2025: '50 Accounts (Tiered)', change: '-2 Accounts (OEM stores removed)' },
    { metric: 'SOS Total Products Tracked', y2024: p2024.sos.total_products.toLocaleString(), y2025: p2025.sos.total_products.toLocaleString(), change: '-344,868 (-24.0%)' },
    { metric: 'Average SOS Products / Month', y2024: p2024.sos.avg_monthly_products.toLocaleString(), y2025: p2025.sos.avg_monthly_products.toLocaleString(), change: '-28,739 / month' },
    { metric: 'Average SOS Category Pages / Month', y2024: `${p2024.sos.avg_category_pages_month} Pages`, y2025: `${p2025.sos.avg_category_pages_month} Pages`, change: '-143 Pages / month' },
    { metric: 'SOV Total Products Tracked', y2024: p2024.sov.total_products.toLocaleString(), y2025: p2025.sov.total_products.toLocaleString(), change: '-1,470,421 (-29.7%)' },
    { metric: 'Average SOV Products / Month', y2024: p2024.sov.avg_monthly_products.toLocaleString(), y2025: p2025.sov.avg_monthly_products.toLocaleString(), change: '-122,535 / month' },
    { metric: 'Average SOV Keywords / Month', y2024: `${p2024.sov.avg_keywords_month} Keywords`, y2025: `${p2025.sov.avg_keywords_month} Keywords`, change: '-236 Keywords / month' },
    { metric: 'Banner URLs Monitored', y2024: `${p2024.banners.urls_count} URLs`, y2025: `${p2025.banners.urls_count} URLs`, change: '-26 URLs' },
    { metric: 'Banner Account URLs Monitored', y2024: `${p2024.banners.accounts_count} Accounts`, y2025: `${p2025.banners.accounts_count} Accounts`, change: '+2 Accounts' },
    { metric: 'Total Banners Captured', y2024: p2024.banners.total_banners.toLocaleString(), y2025: p2025.banners.total_banners.toLocaleString(), change: '+7,353 (+7.2%)' },
    { metric: 'Average Monthly Banners', y2024: p2024.banners.avg_monthly_banners.toLocaleString(), y2025: p2025.banners.avg_monthly_banners.toLocaleString(), change: '+613 / month' },
  ];

  const chartData = [
    { metric: 'SOS Products (k)', y2024: p2024.sos.total_products / 1000, y2025: p2025.sos.total_products / 1000 },
    { metric: 'SOV Products (k)', y2024: p2024.sov.total_products / 1000, y2025: p2025.sov.total_products / 1000 },
    { metric: 'Banners (k)', y2024: p2024.banners.total_banners / 1000, y2025: p2025.banners.total_banners / 1000 },
  ];

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Calendar className="w-5 h-5 text-purple-700" />
            <span>Program Specifications, Delivery SLA &amp; Historical Archive</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Operational delivery matrices, 3x daily in-season pricing feeds, 2024 vs 2025 scope reconciliation, and flexible 63-account scoring roster
          </p>
        </div>

        {/* Sub-Tabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'comparison', label: '2024 vs 2025 Variance' },
            { id: 'delivery-schedule', label: 'Delivery Schedule & SLAs' },
            { id: 'in-season-scope', label: 'In-Season 3x Daily Scope' },
            { id: '2024', label: '2024 Program Details' },
            { id: '2025', label: '2025 Tiered Cadence' },
            { id: 'cadence', label: 'Cadence Shift Analysis' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveHistoryTab(tab.id as any)}
              className={`px-3 py-1.5 rounded-lg transition-colors ${
                activeHistoryTab === tab.id
                  ? 'bg-intel-navy text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* 1. Comparison Tab */}
      {activeHistoryTab === 'comparison' && (
        <div className="space-y-6">
          {/* Executive Summary Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>Account Coverage Model</span>
                <Store className="w-4 h-4 text-intel-navy" />
              </div>
              <div className="text-xl font-bold text-slate-900">52 &rarr; 50 Accounts</div>
              <div className="text-[11px] text-amber-600 font-medium mt-1">Tiered Cadence (22/6/22)</div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>SOS Volume Change</span>
                <Layers className="w-4 h-4 text-intel-blue" />
              </div>
              <div className="text-xl font-bold text-slate-900">1.44M &rarr; 1.09M</div>
              <div className="text-[11px] text-slate-500 mt-1">-24.0% annualized volume</div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>SOV Volume Change</span>
                <Search className="w-4 h-4 text-purple-600" />
              </div>
              <div className="text-xl font-bold text-slate-900">4.95M &rarr; 3.48M</div>
              <div className="text-[11px] text-slate-500 mt-1">-29.7% annualized volume</div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>Banner Capture Growth</span>
                <Image className="w-4 h-4 text-emerald-600" />
              </div>
              <div className="text-xl font-bold text-slate-900">102K &rarr; 109.8K</div>
              <div className="text-[11px] text-emerald-600 font-semibold mt-1">+7.2% capture density</div>
            </div>
          </div>

          {/* Side-by-Side Comparison Table */}
          <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-xs">
            <div className="p-4 border-b border-slate-100 bg-slate-50 flex items-center justify-between">
              <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider">
                Full 2024 vs 2025 Metric Variance Matrix
              </h3>
              <span className="text-xs text-slate-500 font-medium">Data verified against official program specification</span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-100/75 text-slate-600 font-bold border-b border-slate-200">
                  <tr>
                    <th className="py-2.5 px-4">Metric / Dimension</th>
                    <th className="py-2.5 px-4 text-right">2024 Official Baseline</th>
                    <th className="py-2.5 px-4 text-right">2025 Revised Program</th>
                    <th className="py-2.5 px-4 text-right">Variance / Impact</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 text-slate-700 font-mono text-[11px]">
                  {comparisonRows.map((row, idx) => (
                    <tr key={idx} className="hover:bg-slate-50/50">
                      <td className="py-2.5 px-4 font-sans font-semibold text-slate-900">{row.metric}</td>
                      <td className="py-2.5 px-4 text-right">{row.y2024}</td>
                      <td className="py-2.5 px-4 text-right font-bold text-intel-navy">{row.y2025}</td>
                      <td className="py-2.5 px-4 text-right">
                        <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                          row.change.startsWith('+') ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-slate-100 text-slate-600'
                        }`}>
                          {row.change}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Volume Comparison Chart */}
          <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider mb-4">
              Annual Volume Comparison by Workstream (in Thousands)
            </h3>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={chartData} margin={{ top: 10, right: 20, left: 10, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                  <XAxis dataKey="metric" tick={{ fontSize: 11 }} />
                  <YAxis tick={{ fontSize: 11 }} />
                  <Tooltip formatter={(val: any) => `${Number(val).toLocaleString()}k units`} />
                  <Legend wrapperStyle={{ fontSize: '11px' }} />
                  <Bar dataKey="y2024" name="2024 Baseline" fill="#94a3b8" radius={[4, 4, 0, 0]} />
                  <Bar dataKey="y2025" name="2025 Program" fill="#0071c5" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      )}

      {/* 2. Delivery Schedule & SLAs Tab */}
      {activeHistoryTab === 'delivery-schedule' && (
        <div className="space-y-6">
          {/* Header SLA Summary */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>sFTP Feed Delivery SLA</span>
                <Server className="w-4 h-4 text-emerald-600" />
              </div>
              <div className="text-xl font-bold text-emerald-600">100.0%</div>
              <div className="text-[11px] text-slate-500 mt-1">Daily Automated Ingestion</div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>Price Updates Cadence</span>
                <Zap className="w-4 h-4 text-intel-cyan" />
              </div>
              <div className="text-xl font-bold text-slate-900">3x Daily</div>
              <div className="text-[11px] text-slate-500 mt-1">Multi-Daily Real-time Stream</div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>Banner Audit Refresh</span>
                <Image className="w-4 h-4 text-purple-600" />
              </div>
              <div className="text-xl font-bold text-slate-900">2x Daily (10 Sites)</div>
              <div className="text-[11px] text-slate-500 mt-1">50 Retailers / 145 URLs Total</div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-xs text-slate-500 font-semibold mb-1">
                <span>Flexible Account Pool</span>
                <Sliders className="w-4 h-4 text-intel-navy" />
              </div>
              <div className="text-xl font-bold text-slate-900">63 Accounts</div>
              <div className="text-[11px] text-slate-500 mt-1">Monthly Selection Flexibility</div>
            </div>
          </div>

          {/* Delivery Matrix Table */}
          <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-xs">
            <div className="p-4 border-b border-slate-100 bg-slate-50 flex items-center justify-between">
              <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-2">
                <Send className="w-4 h-4 text-intel-blue" />
                <span>Intel Scorecards Official Delivery Schedule &amp; Format Specifications</span>
              </h3>
              <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded border border-emerald-200">
                All Streams Active &amp; Verified
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-100/75 text-slate-600 font-bold border-b border-slate-200">
                  <tr>
                    <th className="py-2.5 px-4">Deliverable Scope Item</th>
                    <th className="py-2.5 px-4">Cadence</th>
                    <th className="py-2.5 px-4">Format &amp; Destination</th>
                    <th className="py-2.5 px-4">Last Sync</th>
                    <th className="py-2.5 px-4">Next Scheduled</th>
                    <th className="py-2.5 px-4 text-right">SLA</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 text-slate-700 font-mono text-[11px]">
                  {DELIVERY_SCHEDULE_ITEMS.map((item, idx) => (
                    <tr key={idx} className="hover:bg-slate-50/50">
                      <td className="py-2.5 px-4 font-sans font-semibold text-slate-900 flex items-center gap-2">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                        <span>{item.scope_item}</span>
                      </td>
                      <td className="py-2.5 px-4">
                        <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                          item.cadence === 'MultiDaily' ? 'bg-purple-100 text-purple-700' :
                          item.cadence === 'Daily' ? 'bg-blue-100 text-blue-700' : 'bg-slate-100 text-slate-700'
                        }`}>
                          {item.cadence}
                        </span>
                      </td>
                      <td className="py-2.5 px-4 font-sans text-slate-600">{item.deliverable_format}</td>
                      <td className="py-2.5 px-4">{item.last_delivery}</td>
                      <td className="py-2.5 px-4 text-intel-blue">{item.next_delivery}</td>
                      <td className="py-2.5 px-4 text-right font-bold text-emerald-600">{item.sla_compliance_pct}%</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* 3. In-Season 3x Daily Scope Tab */}
      {activeHistoryTab === 'in-season-scope' && (
        <div className="space-y-6">
          <div className="bg-intel-navy text-white p-6 rounded-2xl shadow-md">
            <div className="flex items-center gap-2.5 mb-2">
              <Zap className="w-5 h-5 text-intel-cyan" />
              <h3 className="text-base font-bold">In-Season Category Management &amp; Segment Pricing Strategies</h3>
            </div>
            <p className="text-xs text-slate-300 max-w-3xl leading-relaxed">
              Real-time Intel &amp; Competitor pricing and promotion tracking of comparable configs across Retailers, OEMs, SKUs/CPUs/GPUs. Monitored <strong>3 times daily</strong> across 173 1P Retailer websites, 14 3P Marketplaces, and 6 OEM.com flagship sites in 23 countries.
            </p>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-5 pt-5 border-t border-slate-700/60 font-mono text-xs">
              <div>
                <div className="text-slate-400 text-[10px]">1P RETAILER WEBSITES</div>
                <div className="text-lg font-bold text-white">173 Sites</div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">3P MARKETPLACES</div>
                <div className="text-lg font-bold text-white">14 Marketplaces</div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">OEM.COM STORES</div>
                <div className="text-lg font-bold text-white">6 Global OEMs</div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">TARGET COUNTRIES</div>
                <div className="text-lg font-bold text-intel-cyan">23 Countries</div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-2">
                <Layers className="w-4 h-4 text-intel-blue" />
                <span>Form Factors &amp; Device Scope</span>
              </h4>
              <div className="flex flex-wrap gap-2 text-xs">
                {IN_SEASON_PRICING_SUMMARY.form_factors.map((ff, i) => (
                  <span key={i} className="px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200 font-semibold text-slate-800">
                    {ff}
                  </span>
                ))}
              </div>
              <p className="text-[11px] text-slate-500 italic">
                * PC Accessories strictly excluded (Monitors, Cameras, Keyboards, Gift Cards).
              </p>
            </div>

            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-2">
                <Globe className="w-4 h-4 text-purple-600" />
                <span>Competitors &amp; Ecosystem Tracked</span>
              </h4>
              <div className="flex flex-wrap gap-2 text-xs">
                {IN_SEASON_PRICING_SUMMARY.competitors_tracked.map((comp, i) => (
                  <span key={i} className="px-3 py-1.5 rounded-lg bg-purple-50 border border-purple-200 font-semibold text-purple-800">
                    {comp}
                  </span>
                ))}
              </div>
              <p className="text-[11px] text-slate-500">
                Segment focus: <strong>AI PC, Premium, Gaming, Mainstream, Entry</strong> with automated like-for-like device configuration comparisons.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* 4. 2024 Program Details Tab */}
      {activeHistoryTab === '2024' && (
        <div className="space-y-6">
          <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider">
              2024 Monitored Account Composition (52 Accounts)
            </h3>
            <p className="text-xs text-slate-500">
              Tracking cadence: Monthly tracking across all 52 accounts (from March 2024).
            </p>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-xs font-mono">
              {p2024.account_composition.map((acc, idx) => (
                <div key={idx} className="p-2 rounded bg-slate-50 border border-slate-200 text-slate-800">
                  {acc}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* 5. 2025 Tiered Cadence Tab */}
      {activeHistoryTab === '2025' && (
        <div className="space-y-6">
          <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider">
              2025 Tiered Account Composition (50 Accounts Total)
            </h3>
            <p className="text-xs text-slate-500">
              Tracking cadence: 22 Accounts Monthly, 6 Accounts Mid-Quarter (Every 2 months), 22 Accounts Once per Quarter.
            </p>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-xs font-mono">
              {p2025.account_composition.map((acc, idx) => (
                <div key={idx} className="p-2 rounded bg-slate-50 border border-slate-200 text-slate-800">
                  {acc}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* 6. Cadence Shift Analysis */}
      {activeHistoryTab === 'cadence' && (
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
          <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider">
            Cadence &amp; Account Shifts (2024 to 2025)
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div className="p-4 rounded-xl bg-red-50 border border-red-200 space-y-2">
              <h4 className="font-bold text-xs text-red-900">Accounts Removed in 2025 Program</h4>
              <ul className="list-disc list-inside text-xs text-red-800 space-y-1">
                {p2025.account_changes.removed.map((acc, i) => (
                  <li key={i}>{acc}</li>
                ))}
              </ul>
            </div>

            <div className="p-4 rounded-xl bg-emerald-50 border border-emerald-200 space-y-2">
              <h4 className="font-bold text-xs text-emerald-900">Accounts Added in 2025 Program</h4>
              <ul className="list-disc list-inside text-xs text-emerald-800 space-y-1">
                {p2025.account_changes.added.map((acc, i) => (
                  <li key={i}>{acc}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
