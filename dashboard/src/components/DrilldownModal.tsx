import React from 'react';
import { X, ExternalLink, CheckCircle2, XCircle, Cpu, ShieldCheck, Tag, Monitor, HardDrive, Layers } from 'lucide-react';

interface DrilldownModalProps {
  sku: any | null;
  onClose: () => void;
}

export const DrilldownModal: React.FC<DrilldownModalProps> = ({ sku, onClose }) => {
  if (!sku) return null;

  const flags = sku.audit_flags || {};
  const isIntel = sku.is_intel_cpu;
  const flagKeys = ['S1', 'S2', 'P1', 'P2', 'P3', 'P4', 'P5'];

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
      <div className="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-4xl max-h-[90vh] overflow-hidden flex flex-col shadow-2xl animate-in fade-in zoom-in-95 duration-200">
        {/* Modal Header */}
        <div className="px-6 py-4 bg-slate-800/90 border-b border-slate-700 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className={`w-9 h-9 rounded-xl flex items-center justify-center font-bold text-sm ${
              isIntel ? 'bg-intel-blue text-white' : 'bg-rose-900 text-rose-200'
            }`}>
              {sku.oem ? sku.oem[0] : 'PC'}
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="text-base font-bold text-white leading-tight">
                  {sku.oem} {sku.model_series}
                </h3>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-700 text-slate-300 font-mono">
                  {sku.sku_id}
                </span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-intel-cyan/20 text-intel-cyan font-semibold border border-intel-cyan/30">
                  {sku.segment}
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                {sku.retailer} • {sku.form_factor} • Product ID: <span className="font-mono text-slate-300">{sku.product_id}</span>
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 overflow-y-auto space-y-6 text-xs text-slate-300">
          {/* Price & Commercial Header */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
              <span className="text-slate-400 text-[11px] block">Current Price (USD)</span>
              <span className="text-xl font-bold text-emerald-400">${sku.current_price?.toLocaleString()}</span>
              {sku.discount_amount > 0 && (
                <span className="text-[10px] text-slate-400 block line-through">Orig: ${sku.original_price?.toLocaleString()}</span>
              )}
            </div>

            <div className="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
              <span className="text-slate-400 text-[11px] block">Promotional Discount</span>
              <span className="text-xl font-bold text-amber-400">
                {sku.discount_pct > 0 ? `-${sku.discount_pct}%` : '0%'}
              </span>
              <span className="text-[10px] text-slate-400 block">Save ${sku.discount_amount}</span>
            </div>

            <div className="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
              <span className="text-slate-400 text-[11px] block">Brand Audit Score</span>
              <span className={`text-xl font-bold ${
                sku.compliance_score >= 80 ? 'text-emerald-400' : sku.compliance_score >= 60 ? 'text-amber-400' : 'text-rose-400'
              }`}>
                {sku.compliance_score}%
              </span>
              <span className="text-[10px] text-slate-400 block">S1..P5 Compliance</span>
            </div>

            <div className="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 flex flex-col justify-between">
              <span className="text-slate-400 text-[11px] block">Live Store Listing</span>
              <a
                href={sku.product_url}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center space-x-1.5 text-intel-cyan hover:underline font-semibold text-xs"
              >
                <span>Open Store PDP</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>

          {/* 18-Attribute Specification Grid */}
          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3 flex items-center gap-1.5">
              <Cpu className="w-4 h-4 text-intel-cyan" />
              <span>Full Hardware &amp; Platform Specifications (18 Attributes)</span>
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Processor Series &amp; Gen</span>
                <span className="font-semibold text-white">{sku.processor_series} ({sku.processor_gen})</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Exact Processor Model</span>
                <span className="font-semibold text-white">{sku.processor_model}</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Graphics Card (GPU)</span>
                <span className="font-semibold text-white">{sku.graphics_card}</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Memory (RAM)</span>
                <span className="font-semibold text-white">{sku.ram_size} ({sku.ram_type})</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Primary Storage</span>
                <span className="font-semibold text-white">{sku.storage_size} ({sku.storage_type})</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Display &amp; Screen Type</span>
                <span className="font-semibold text-white">{sku.screen_size} {sku.screen_type}</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Operating System</span>
                <span className="font-semibold text-white">{sku.operating_system}</span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">EVO / vPro Badges</span>
                <span className="font-semibold text-white">
                  {sku.is_evo ? '⭐ Intel EVO Badged' : ''} {sku.is_vpro ? '🔒 Intel vPro' : ''} {!sku.is_evo && !sku.is_vpro ? 'Standard Platform' : ''}
                </span>
              </div>
              <div className="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800">
                <span className="text-[11px] text-slate-500 block">Gaming Flag</span>
                <span className="font-semibold text-white">{sku.is_gaming ? '🎮 Gaming Certified' : 'Non-Gaming Standard'}</span>
              </div>
            </div>
          </div>

          {/* S1..P5 Audit Compliance Flag Breakdown */}
          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3 flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>Brand Audit Rules Breakdown (S1, S2, P1, P2, P3, P4, P5)</span>
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5">
              {flagKeys.map((fKey) => {
                const fData = flags[fKey] || {};
                const passed = fData.pass;
                return (
                  <div key={fKey} className={`p-3 rounded-xl border ${
                    passed ? 'bg-emerald-950/20 border-emerald-500/40 text-emerald-300' : 'bg-rose-950/20 border-rose-500/40 text-rose-300'
                  }`}>
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-mono font-bold text-xs">{fKey}</span>
                      {passed ? (
                        <span className="inline-flex items-center text-[10px] font-bold text-emerald-400 gap-1">
                          <CheckCircle2 className="w-3.5 h-3.5" /> PASS
                        </span>
                      ) : (
                        <span className="inline-flex items-center text-[10px] font-bold text-rose-400 gap-1">
                          <XCircle className="w-3.5 h-3.5" /> FAIL
                        </span>
                      )}
                    </div>
                    <span className="text-[11px] block font-medium text-slate-200">{fData.label || fKey}</span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Reference PDP Screenshot Image */}
          {sku.screenshot_pdp_path && (
            <div>
              <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                <Monitor className="w-4 h-4 text-intel-cyan" />
                <span>Captured Reference Screenshot (PDP Evidence)</span>
              </h4>
              <div className="rounded-xl overflow-hidden border border-slate-700 bg-slate-950 p-2">
                <img
                  src={`/screenshots/${sku.screenshot_pdp_path.split('/').pop()}`}
                  alt={`Screenshot ${sku.sku_id}`}
                  className="w-full h-auto rounded-lg object-contain max-h-[350px]"
                />
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
