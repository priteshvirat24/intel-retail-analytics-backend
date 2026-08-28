import React, { useState } from 'react';
import { Globe, Lock, CheckCircle2, AlertCircle, ArrowRight, ShieldAlert } from 'lucide-react';

interface RegionalReportViewProps {
  regionalData: any;
}

export const RegionalReportView: React.FC<RegionalReportViewProps> = ({ regionalData }) => {
  const [activeRegion, setActiveRegion] = useState<'us' | 'latam'>('us');
  const us = regionalData?.regions?.united_states || {};
  const latam = regionalData?.regions?.latam || {};

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* View Header */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-intel-cyan/20 border border-intel-cyan/30 text-intel-cyan">
              <Globe className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">Regional Reports &amp; Multi-Market Intelligence</h2>
              <p className="text-xs text-slate-400">
                Active United States POC dataset and production LATAM expansion architecture
              </p>
            </div>
          </div>

          {/* Region Selector Tabs */}
          <div className="flex items-center space-x-2 bg-slate-900/90 border border-slate-700/80 p-1.5 rounded-2xl text-xs">
            <button
              onClick={() => setActiveRegion('us')}
              className={`px-4 py-2 rounded-xl font-bold transition-all flex items-center gap-1.5 ${
                activeRegion === 'us'
                  ? 'bg-intel-blue text-white shadow-md shadow-intel-blue/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <span>🇺🇸 United States</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-300 font-mono">
                Active
              </span>
            </button>

            <button
              onClick={() => setActiveRegion('latam')}
              className={`px-4 py-2 rounded-xl font-bold transition-all flex items-center gap-1.5 ${
                activeRegion === 'latam'
                  ? 'bg-slate-800 text-white'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <span>🌎 Latin America (LATAM)</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded bg-slate-800 text-amber-400 font-mono flex items-center gap-0.5">
                <Lock className="w-2.5 h-2.5" /> Placeholder
              </span>
            </button>
          </div>
        </div>
      </div>

      {activeRegion === 'us' ? (
        /* Active US Market Deep Dive */
        <div className="space-y-6">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="glass-card p-4 rounded-xl border border-slate-800">
              <span className="text-xs text-slate-400 block">Sampled Retail Channels</span>
              <span className="text-2xl font-extrabold text-white mt-1 block">
                {us.retailers_sampled} Sites
              </span>
              <span className="text-[11px] text-slate-400 mt-1 block">
                Best Buy, Walmart, Costco, Amazon, Dell, HP
              </span>
            </div>

            <div className="glass-card p-4 rounded-xl border border-slate-800">
              <span className="text-xs text-slate-400 block">Intel Share of Shelf (US)</span>
              <span className="text-2xl font-extrabold text-intel-cyan mt-1 block">
                {us.intel_sos_pct}%
              </span>
              <span className="text-[11px] text-slate-400 mt-1 block">
                Strongest in Direct OEM &amp; Best Buy AI PC hubs
              </span>
            </div>

            <div className="glass-card p-4 rounded-xl border border-slate-800">
              <span className="text-xs text-slate-400 block">Active Currency &amp; Region</span>
              <span className="text-2xl font-extrabold text-emerald-400 mt-1 block">
                {us.currency} ($)
              </span>
              <span className="text-[11px] text-slate-400 mt-1 block">
                North America (US-Domestic)
              </span>
            </div>
          </div>

          <div className="glass-panel p-6 rounded-2xl">
            <h3 className="text-base font-bold text-white mb-3">Key US Market Insights</h3>
            <div className="space-y-3">
              {(us.highlights || []).map((h: string, idx: number) => (
                <div key={idx} className="flex items-start space-x-3 p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-xs">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                  <span className="text-slate-200">{h}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      ) : (
        /* LATAM Placeholder Architecture View */
        <div className="glass-panel p-8 rounded-2xl border border-amber-500/30 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-amber-500/20 border border-amber-500/40 text-amber-400 flex items-center justify-center mx-auto">
            <Lock className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-white">LATAM Regional Expansion Architecture</h3>
            <p className="text-xs text-slate-400 max-w-xl mx-auto mt-1">
              The LATAM regional pipeline is structured and ready for production scaling. In this POC, execution is strictly capped to 1 country (US) to eliminate unnecessary scraping costs.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto text-left pt-4">
            {(latam.target_countries || []).map((c: any) => (
              <div key={c.country} className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
                <span className="text-xs font-bold text-white block">{c.country}</span>
                <span className="text-[10px] text-slate-400 block font-mono">ISO: {c.iso.toUpperCase()}</span>
                <div className="mt-2 space-y-1">
                  {c.target_retailers.map((r: string) => (
                    <span key={r} className="text-[10px] text-slate-400 block truncate font-mono">
                      • {r}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="p-3 bg-slate-900/90 rounded-xl border border-slate-800 text-xs text-amber-300 max-w-xl mx-auto flex items-center justify-center gap-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>Ready to activate on production 173-retailer / 23-country pipeline.</span>
          </div>
        </div>
      )}
    </div>
  );
};
