import React, { useState } from 'react';
import { Camera, X, ExternalLink, CheckCircle2, AlertTriangle, FileText, Globe, Layers, Eye } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { EvidenceService } from '../../services/evidenceService';
import { EvidenceRecord } from '../../types/evidence';
import { EvidenceDrawer } from './EvidenceDrawer';

export const SourceEvidenceModal: React.FC = () => {
  const { sourceEvidenceTarget, setSourceEvidenceTarget } = useApp() as any;
  const [selectedEvidenceRecord, setSelectedEvidenceRecord] = useState<EvidenceRecord | null>(null);

  if (!sourceEvidenceTarget) return null;

  const sku = sourceEvidenceTarget;
  const evidenceMap = EvidenceService.getProductEvidenceMap(sku);

  const componentList = [
    { key: 'S1', name: 'Listing Title Compliance', rec: evidenceMap.components.s1 },
    { key: 'S2', name: 'Listing Badge Presence', rec: evidenceMap.components.s2 },
    { key: 'P1', name: 'PDP Header Title Compliance', rec: evidenceMap.components.p1 },
    { key: 'P2', name: 'PDP Hero Badge Placement', rec: evidenceMap.components.p2 },
    { key: 'P3', name: 'Technical Specifications Processor Branding', rec: evidenceMap.components.p3 },
    { key: 'P4', name: 'Intel-Led Rich Media (A+ Content)', rec: evidenceMap.components.p4 },
    { key: 'P5', name: 'OEM-Led Rich Media Content', rec: evidenceMap.components.p5 },
  ];

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl w-full max-w-4xl max-h-[90vh] overflow-hidden shadow-2xl flex flex-col animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="p-1.5 rounded-lg bg-intel-navy text-white">
              <FileText className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900">Source Evidence &amp; Scorecards Audit Trace</h3>
              <p className="text-[11px] text-slate-500">
                {sku.oem || ''} {sku.model || sku.model_series || ''} ({sku.product_id || sku.sku_id}) &bull; Storefront: <strong className="text-slate-800">{sku.account || sku.retailer}</strong>
              </p>
            </div>
          </div>
          <button
            onClick={() => setSourceEvidenceTarget(null)}
            aria-label="Close modal"
            className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-5 text-xs">
          {/* Metadata Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 p-4 rounded-xl border border-slate-200 font-mono text-[11px]">
            <div>
              <span className="text-[10px] uppercase font-bold text-slate-400 block font-sans">Retailer &amp; Country</span>
              <strong className="text-slate-900 font-sans text-xs">{sku.account || sku.retailer}</strong>
              <div className="text-[10px] text-slate-500">{sku.country}</div>
            </div>

            <div>
              <span className="text-[10px] uppercase font-bold text-slate-400 block font-sans">Extraction Lineage</span>
              <span className="font-semibold text-intel-navy block">{sku.extraction_method || 'CACHE'}</span>
              <span className="text-[10px] text-slate-500">ID: ext-{sku.product_id || 'sku'}</span>
            </div>

            <div>
              <span className="text-[10px] uppercase font-bold text-slate-400 block font-sans">Capture Timestamp</span>
              <span className="font-mono text-slate-800 block">{sku.date || sku.scraped_at || 'Not captured'}</span>
            </div>

            <div>
              <span className="text-[10px] uppercase font-bold text-slate-400 block font-sans">Overall Audit Status</span>
              <span className={`inline-flex items-center gap-1 font-bold text-[10px] px-2 py-0.5 rounded-full ${
                evidenceMap.overall_status === 'VERIFIED'
                  ? 'bg-emerald-100 text-emerald-800'
                  : evidenceMap.overall_status === 'PARTIALLY_VERIFIED'
                  ? 'bg-amber-100 text-amber-800'
                  : 'bg-rose-100 text-rose-800'
              }`}>
                {evidenceMap.overall_status}
              </span>
            </div>
          </div>

          {/* URL & Source Info */}
          <div className="space-y-1">
            <span className="text-[11px] font-bold text-slate-700 block">Captured Storefront URL:</span>
            <div className="flex items-center justify-between p-2.5 bg-slate-50 rounded-xl border border-slate-200 font-mono text-[11px] text-slate-800 break-all">
              <span className="truncate max-w-xl">{sku.product_url || sku.sourceUrl || 'Source unavailable'}</span>
              {sku.product_url || sku.sourceUrl ? (
                <a
                  href={sku.product_url || sku.sourceUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="ml-2 px-2.5 py-1 rounded bg-intel-navy text-white hover:bg-intel-blue font-semibold text-[11px] inline-flex items-center space-x-1 shrink-0"
                >
                  <span>Verify Source</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              ) : (
                <span className="text-slate-400 text-xs">Source unavailable</span>
              )}
            </div>
          </div>

          {/* Component Evidence Breakdown Table */}
          <div className="space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-bold text-slate-700">7-Component Scorecard Evidence Trace:</span>
              <span className="text-[10px] text-slate-500">Click any row to inspect underlying rule and DOM evidence</span>
            </div>

            <div className="divide-y divide-slate-100 border border-slate-200 rounded-xl overflow-hidden bg-white">
              {componentList.map((item) => {
                const rec = item.rec;
                const isPass = rec.result === 'PASS';
                const isFail = rec.result === 'FAIL';
                const isUnverified = rec.result === 'UNVERIFIED';

                return (
                  <div
                    key={item.key}
                    onClick={() => setSelectedEvidenceRecord(rec)}
                    className="p-3 hover:bg-slate-50 flex items-center justify-between gap-3 cursor-pointer transition-colors"
                  >
                    <div className="flex items-center space-x-3 min-w-0">
                      <span className="font-mono font-bold text-xs text-intel-navy w-6 shrink-0">{item.key}</span>
                      <div className="min-w-0">
                        <div className="flex items-center space-x-2">
                          <span className="font-bold text-slate-900 text-xs truncate">{item.name}</span>
                          <span className={`inline-flex items-center text-[9px] font-bold px-2 py-0.5 rounded-full ${
                            rec.verificationStatus === 'VERIFIED'
                              ? 'bg-emerald-100 text-emerald-800'
                              : rec.verificationStatus === 'PARTIALLY_VERIFIED'
                              ? 'bg-amber-100 text-amber-800'
                              : 'bg-slate-200 text-slate-700'
                          }`}>
                            {rec.verificationStatus}
                          </span>
                        </div>
                        <p className="text-[11px] text-slate-500 truncate mt-0.5">
                          {rec.detection_reason}
                        </p>
                      </div>
                    </div>

                    <div className="flex items-center space-x-3 shrink-0">
                      <div className="text-right font-mono">
                        <span className="text-xs font-black text-slate-900">
                          {rec.score_awarded !== null ? `${rec.score_awarded}/100` : 'N/A'}
                        </span>
                      </div>
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          setSelectedEvidenceRecord(rec);
                        }}
                        className="px-2.5 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-[11px] flex items-center space-x-1"
                      >
                        <Eye className="w-3 h-3 text-intel-navy" />
                        <span>Inspect</span>
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-200 flex justify-end">
          <button
            onClick={() => setSourceEvidenceTarget(null)}
            className="px-4 py-1.5 rounded-lg bg-slate-800 text-white hover:bg-slate-900 font-semibold text-xs"
          >
            Close
          </button>
        </div>
      </div>

      {/* Sub-Drawer for Specific Score Evidence Record */}
      {selectedEvidenceRecord && (
        <EvidenceDrawer
          evidence={selectedEvidenceRecord}
          onClose={() => setSelectedEvidenceRecord(null)}
        />
      )}
    </div>
  );
};
