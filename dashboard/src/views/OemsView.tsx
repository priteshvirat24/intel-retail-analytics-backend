import React from 'react';
import { Cpu, Award, ShieldCheck, Layers, Sparkles, CheckCircle2, Inbox } from 'lucide-react';
import { useApp } from '../context/AppContext';

export const OemsView: React.FC = () => {
  const { filteredScorecardProducts, oemDistribution } = useApp() as any;
  const products = filteredScorecardProducts || [];

  const dynamicOems = (oemDistribution || []).map((o: any) => {
    const oemProducts = products.filter((p: any) => (p.oem || '').toLowerCase() === o.oem.toLowerCase());
    const evoCount = oemProducts.filter((p: any) => p.Evo === 'Y').length;
    const premierCount = oemProducts.filter((p: any) => p.Premium === 'Y' || p.concatenate === 'Y').length;
    const scores = oemProducts.map((p: any) => p.Overall).filter(Boolean);
    const avgScore = scores.length > 0 ? Math.round(scores.reduce((a: number, b: number) => a + b, 0) / scores.length) : 80;

    return {
      name: o.oem,
      total: o.count,
      intel: o.intelCount,
      sos_pct: o.intelPct,
      avg_score: avgScore,
      evo: evoCount,
      premier: premierCount,
    };
  });

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Cpu className="w-5 h-5 text-intel-navy" />
            <span>OEM Manufacturer Platform &amp; Audit Benchmark</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Benchmarking {dynamicOems.length} active OEM hardware partners for Intel Core/Ultra penetration and brand compliance
          </p>
        </div>
      </div>

      {dynamicOems.length === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No OEM Data Available</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no OEM records matching your current filter selection.
            </p>
          </div>
        </div>
      ) : (
        /* OEM Benchmark Cards */
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {dynamicOems.map((o: any) => (
            <div key={o.name} className="ent-card p-5 rounded-xl space-y-3">
              <div className="flex items-center justify-between">
                <h3 className="text-base font-bold text-slate-900">{o.name}</h3>
                <span className="text-xs font-mono font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                  {o.avg_score}% Score
                </span>
              </div>

              <div className="space-y-1.5 text-xs text-slate-600">
                <div className="flex justify-between">
                  <span>Intel Share of Shelf:</span>
                  <span className="font-mono font-bold text-intel-navy">{o.sos_pct}% ({o.intel}/{o.total} SKUs)</span>
                </div>
                <div className="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                  <div className="bg-intel-navy h-full rounded-full" style={{ width: `${o.sos_pct}%` }}></div>
                </div>

                <div className="flex justify-between pt-2 border-t border-slate-100 font-mono text-[11px]">
                  <span>EVO Models: <strong className="text-purple-700">{o.evo}</strong></span>
                  <span>Premier SKUs: <strong className="text-intel-navy">{o.premier}</strong></span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
