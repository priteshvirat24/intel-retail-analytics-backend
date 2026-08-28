import React from 'react';
import {
  DollarSign,
  ShieldCheck,
  Zap,
  RotateCcw,
  SlidersHorizontal,
  Lock,
  CheckCircle2,
  Database,
  ArrowRight,
  TrendingDown,
  Layers
} from 'lucide-react';
import { useApp } from '../context/AppContext';
import { EXTRACTION_WATERFALL } from '../data/scorecardsData';

export const CostCenterView: React.FC = () => {
  const { costMetrics, guardrails, setRunSampleModalOpen, setSettingsModalOpen } = useApp();
  const w = EXTRACTION_WATERFALL;

  const waterfallSteps = [
    { label: '1. Candidate Evaluation Pool', count: w.total_candidate_urls, desc: 'Incoming candidate target URLs across catalog', color: 'bg-slate-800 text-white', badge: 'Input' },
    { label: '2. Local Cache Layer (TTL 7d)', count: w.cached_urls, desc: 'Serviced instantly from local storage (0 cost)', color: 'bg-emerald-600 text-white', badge: '74.0% Hit' },
    { label: '3. Existing Stored Dataset', count: w.existing_dataset_urls, desc: 'Deduplicated against previously validated catalog', color: 'bg-blue-600 text-white', badge: '18.0% Reused' },
    { label: '4. Direct API / SDK Discovery', count: w.sdk_urls, desc: 'Extracted via lightweight structural endpoints', color: 'bg-purple-600 text-white', badge: '5.5% Direct' },
    { label: '5. SERP Discovery Cache', count: w.serp_urls, desc: 'Resolved from search engine ranking cache', color: 'bg-amber-600 text-white', badge: '2.0% SERP' },
    { label: '6. Bright Data Fallback', count: w.brightdata_required_urls, desc: 'Heavily rate-limited live proxy extraction', color: 'bg-rose-600 text-white', badge: '0.5% Live Req' },
  ];

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <DollarSign className="w-5 h-5 text-intel-navy" />
            <span>Bright Data Cost Center &amp; Extraction Waterfall</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Architecture principle: <strong className="text-slate-900">Bright Data is the expensive fallback, not the default extraction layer</strong>
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={() => setRunSampleModalOpen(true)}
            className="px-3.5 py-1.5 rounded-lg bg-intel-navy hover:bg-intel-blue text-white font-semibold text-xs flex items-center space-x-1.5 shadow-xs"
          >
            <Zap className="w-3.5 h-3.5" />
            <span>Run Sample (Max 3)</span>
          </button>
          <button
            onClick={() => setSettingsModalOpen(true)}
            className="px-3 py-1.5 rounded-lg bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs flex items-center space-x-1"
          >
            <SlidersHorizontal className="w-3.5 h-3.5" />
            <span>Guardrails</span>
          </button>
        </div>
      </div>

      {/* Top Cost KPIs */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Live Bright Data Requests</span>
          <span className="text-2xl font-extrabold text-intel-navy font-mono mt-1 block">
            {costMetrics.used_requests} <span className="text-xs font-normal text-slate-400">/ {costMetrics.total_budget_requests}</span>
          </span>
          <span className="text-[10px] text-slate-400">Budget Remaining: {costMetrics.total_budget_requests - costMetrics.used_requests}</span>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Overall Cache Hit Rate</span>
          <span className="text-2xl font-extrabold text-emerald-600 font-mono mt-1 block">{costMetrics.cache_hit_rate_pct}%</span>
          <span className="text-[10px] text-slate-400">{costMetrics.cached_requests} Requests from Local Cache</span>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Duplicate Requests Blocked</span>
          <span className="text-2xl font-extrabold text-amber-700 font-mono mt-1 block">{costMetrics.blocked_duplicate_requests}</span>
          <span className="text-[10px] text-slate-400">Avoided via URL Normalization</span>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <span className="text-[10px] font-bold uppercase text-slate-500 block">Estimated Extraction Cost</span>
          <span className="text-2xl font-extrabold text-slate-900 font-mono mt-1 block">${costMetrics.estimated_cost_usd}</span>
          <span className="text-[10px] text-slate-400">Estimated @ ~$0.02 / Live Request</span>
        </div>
      </div>

      {/* Extraction Waterfall Process Diagram */}
      <div className="ent-card p-5 rounded-xl space-y-4">
        <div>
          <h3 className="text-sm font-bold text-slate-900">
            Extraction Fallback Waterfall &amp; Request Elimination Pipeline
          </h3>
          <p className="text-xs text-slate-500 mt-0.5">
            Illustrating how 1,000 candidate requests are reduced to only 5 live Bright Data extractions
          </p>
        </div>

        <div className="space-y-3">
          {waterfallSteps.map((step, idx) => (
            <div key={idx} className="p-3.5 bg-slate-50 rounded-xl border border-slate-200 flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <span className={`px-2.5 py-1 rounded-lg text-xs font-bold font-mono ${step.color}`}>
                  {step.count}
                </span>
                <div>
                  <h4 className="text-xs font-bold text-slate-900">{step.label}</h4>
                  <p className="text-[11px] text-slate-500">{step.desc}</p>
                </div>
              </div>

              <span className="text-xs font-mono font-bold px-2.5 py-1 rounded-full bg-white border border-slate-200 text-slate-700 shadow-2xs">
                {step.badge}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
