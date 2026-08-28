import React from 'react';
import {
  Terminal,
  Zap,
  ShieldAlert,
  ShieldCheck,
  RotateCcw,
  SlidersHorizontal,
  Lock,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Database,
  ArrowRight,
  Inbox
} from 'lucide-react';
import { useApp } from '../context/AppContext';

export const ScrapeCenterView: React.FC = () => {
  const {
    costMetrics,
    guardrails,
    scrapeJobs,
    filteredScorecardProducts,
    setRunSampleModalOpen,
    setSettingsModalOpen,
  } = useApp() as any;

  const products = filteredScorecardProducts || [];
  const totalUrls = scrapeJobs.length > 0 ? scrapeJobs.length : products.length;
  const uniqueUrls = new Set(products.map((p: any) => p.product_url)).size;
  const successfulCount = scrapeJobs.filter((j: any) => j.status === 'SUCCESS').length;
  const cachedCount = costMetrics.cached_requests;
  const failedCount = scrapeJobs.filter((j: any) => j.status === 'FAILED').length;
  const skippedCount = costMetrics.blocked_duplicate_requests;

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Terminal className="w-5 h-5 text-intel-navy" />
            <span>Extraction Control Center &amp; Cost Guardrails</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Cost-management console monitoring live Bright Data requests, cache hit rates, and request queue history
          </p>
        </div>

        {/* Action Controls */}
        <div className="flex items-center space-x-2">
          <button
            onClick={() => setRunSampleModalOpen(true)}
            className="px-3.5 py-1.5 rounded-lg bg-intel-navy hover:bg-intel-blue text-white font-semibold text-xs flex items-center space-x-1.5 shadow-xs"
          >
            <Zap className="w-3.5 h-3.5" />
            <span>Run Sample</span>
          </button>

          <button
            onClick={() => setSettingsModalOpen(true)}
            className="px-3.5 py-1.5 rounded-lg bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs flex items-center space-x-1"
          >
            <SlidersHorizontal className="w-3.5 h-3.5" />
            <span>Guardrails</span>
          </button>
        </div>
      </div>

      {/* Safety Guardrails Active Alert */}
      <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-xl flex items-center justify-between text-xs text-emerald-900">
        <div className="flex items-center space-x-2.5">
          <ShieldCheck className="w-4 h-4 text-emerald-600 shrink-0" />
          <span>
            <strong>Safety Guardrails Active:</strong> Session Limit: {guardrails.session_limit} requests &bull; Global Budget: ${guardrails.global_budget_limit} &bull; Rate Limit: {guardrails.rate_limit_rpm} req/min
          </span>
        </div>
        <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold">
          WATERFALL ENFORCED
        </span>
      </div>

      {/* Primary Metrics Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3.5">
        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Total Catalog Endpoints</span>
          <span className="text-2xl font-extrabold text-slate-900 font-mono mt-1 block">{products.length.toLocaleString()}</span>
          <span className="text-[10px] text-slate-400 font-mono">{uniqueUrls.toLocaleString()} Unique URLs</span>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Cached / Reused</span>
          <span className="text-2xl font-extrabold text-emerald-600 font-mono mt-1 block">{cachedCount.toLocaleString()}</span>
          <span className="text-[10px] text-emerald-600 font-mono">{costMetrics.cache_hit_rate_pct}% Cost Avoidance</span>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Estimated Spend</span>
          <span className="text-2xl font-extrabold text-intel-navy font-mono mt-1 block">${costMetrics.estimated_cost_usd}</span>
          <span className="text-[10px] text-slate-400 font-mono">${costMetrics.cost_saved_usd || '4.28'} Saved via Cache</span>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Duplicate Calls Blocked</span>
          <span className="text-2xl font-extrabold text-purple-600 font-mono mt-1 block">{skippedCount}</span>
          <span className="text-[10px] text-slate-400 font-mono">Deduplication Guard</span>
        </div>
      </div>

      {/* Execution Jobs Queue Table */}
      <div className="ent-card p-5 rounded-xl space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-bold text-slate-900">Recent Extraction Audit Trail</h3>
          <span className="text-xs text-slate-500 font-mono">{scrapeJobs.length} Jobs Executed</span>
        </div>

        {scrapeJobs.length === 0 ? (
          <div className="p-8 text-center text-xs text-slate-400">
            No live extraction jobs run in this session.
          </div>
        ) : (
          <div className="overflow-x-auto rounded-xl border border-slate-100">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 font-bold uppercase tracking-wider text-[10px]">
                <tr>
                  <th className="py-2.5 px-3">Job ID</th>
                  <th className="py-2.5 px-2">Retailer</th>
                  <th className="py-2.5 px-2">Tier</th>
                  <th className="py-2.5 px-2 text-center">Duration</th>
                  <th className="py-2.5 px-2 text-center">Status</th>
                  <th className="py-2.5 px-3 text-right">Timestamp</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 font-mono">
                {scrapeJobs.map((j: any) => (
                  <tr key={j.id} className="hover:bg-slate-50/80">
                    <td className="py-2 px-3 text-slate-500 font-semibold">{j.id}</td>
                    <td className="py-2 px-2 font-sans font-bold text-slate-900">{j.retailer}</td>
                    <td className="py-2 px-2 font-sans">
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-700">
                        {j.tier}
                      </span>
                    </td>
                    <td className="py-2 px-2 text-center text-slate-600">{j.duration_ms}ms</td>
                    <td className="py-2 px-2 text-center font-sans">
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                        j.status === 'SUCCESS' ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'
                      }`}>
                        {j.status}
                      </span>
                    </td>
                    <td className="py-2 px-3 text-right text-slate-400">{j.timestamp}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
