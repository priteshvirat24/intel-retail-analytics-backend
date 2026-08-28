import React from 'react';
import {
  X,
  ExternalLink,
  ShieldCheck,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Camera,
  FileText,
  Clock,
  Layers,
  Globe,
  Database,
  Search,
  EyeOff,
  Video,
  Info
} from 'lucide-react';
import { EvidenceRecord } from '../../types/evidence';

interface EvidenceDrawerProps {
  evidence: EvidenceRecord | null;
  onClose: () => void;
}

export const EvidenceDrawer: React.FC<EvidenceDrawerProps> = ({ evidence, onClose }) => {
  if (!evidence) return null;

  const isPass = evidence.result === 'PASS';
  const isFail = evidence.result === 'FAIL';
  const isUnverified = evidence.result === 'UNVERIFIED';

  const scoreDisplay = evidence.score_awarded !== null && evidence.score_awarded !== undefined
    ? `${evidence.score_awarded} / 100`
    : 'N/A (Score Not Evaluated / Missing Evidence)';

  const hasSourceUrl = Boolean(evidence.sourceUrl || evidence.source_url);
  const sourceUrl = evidence.sourceUrl || evidence.source_url || '';

  const hasScreenshot = Boolean(
    evidence.screenshot?.screenshotUrl ||
    evidence.screenshotUrl ||
    evidence.screenshot_url
  );
  const screenshotUrl = evidence.screenshot?.screenshotUrl || evidence.screenshotUrl || evidence.screenshot_url;
  const screenshotTimestamp = evidence.screenshot?.screenshotTimestamp || evidence.captureTimestamp || evidence.capture_timestamp;
  const screenshotPage = evidence.screenshot?.screenshotPageType || evidence.pageType || evidence.page_type || 'PDP';

  const hasMedia = Boolean(evidence.media?.mediaUrl || evidence.mediaUrl || evidence.media_url);
  const mediaUrl = evidence.media?.mediaUrl || evidence.mediaUrl || evidence.media_url;

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex justify-end animate-in fade-in duration-150">
      <div className="bg-white w-full max-w-2xl h-full shadow-2xl flex flex-col border-l border-slate-200 overflow-y-auto text-xs">
        {/* Drawer Header */}
        <div className="px-6 py-4 bg-slate-50 border-b border-slate-200 sticky top-0 z-10 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-intel-navy text-white">
              <ShieldCheck className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="text-sm font-bold text-slate-900">Verifiable Evidence Audit Record</h3>
                <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-slate-200 text-slate-700">
                  {evidence.id || evidence.evidence_id}
                </span>
              </div>
              <p className="text-[11px] text-slate-500 mt-0.5">
                Component: <strong className="text-intel-navy">{evidence.scoreComponent || evidence.component}</strong> &bull; Rule: <span className="font-mono">{evidence.ruleId || evidence.rule_id} (v{evidence.ruleVersion || evidence.rule_version || '1.0'})</span>
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            aria-label="Close evidence drawer"
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Drawer Body - 7 Structured Sections */}
        <div className="p-6 space-y-6">
          {/* SECTION 1: EVIDENCE (Provenance & Account Context) */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <Database className="w-3.5 h-3.5 text-intel-navy" />
              <span>1. Evidence Provenance &amp; Storefront Context</span>
            </h4>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 bg-slate-50 p-4 rounded-xl border border-slate-200 font-mono text-[11px]">
              <div>
                <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Product</span>
                <strong className="text-slate-900 font-sans text-xs line-clamp-1" title={evidence.productTitle || evidence.product_title || ''}>
                  {evidence.productTitle || evidence.product_title || 'N/A'}
                </strong>
                <span className="text-[10px] text-slate-500">ID: {evidence.productId || evidence.product_id || 'N/A'}</span>
              </div>

              <div>
                <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Retailer &amp; Country</span>
                <strong className="text-slate-900 font-sans text-xs">{evidence.retailer || evidence.account || 'Unknown'}</strong>
                <div className="text-[10px] text-slate-500">{evidence.country || 'N/A'}</div>
              </div>

              <div>
                <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Page Type</span>
                <strong className="text-slate-900 font-sans text-xs">{evidence.pageType || evidence.page_type || 'PDP'}</strong>
              </div>

              <div>
                <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Captured Timestamp</span>
                <span className="text-slate-800 text-[10px] block">{evidence.captureTimestamp || evidence.capture_timestamp || 'Not captured'}</span>
              </div>

              <div>
                <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Extraction Lineage</span>
                <strong className="text-intel-blue text-xs block">{evidence.extractionMethod || evidence.extraction_method || 'CACHE'}</strong>
                <span className="text-[9px] text-slate-500 truncate block">ID: {evidence.extractionId || evidence.extraction_id || 'N/A'}</span>
              </div>

              <div>
                <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Provider Request ID</span>
                <span className="text-slate-600 text-[10px] block">
                  {evidence.providerRequestId ? evidence.providerRequestId : 'Not captured'}
                </span>
              </div>

              {evidence.rawEvidence?.attributes && (evidence.rawEvidence.attributes as any).artifact_sha256 && (
                <div className="col-span-2 sm:col-span-3">
                  <span className="text-[10px] text-slate-400 uppercase font-bold block font-sans">Artifact SHA-256 Hash</span>
                  <code className="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded text-[10px] font-mono border border-emerald-200 block truncate">
                    {(evidence.rawEvidence.attributes as any).artifact_sha256}
                  </code>
                </div>
              )}

              <div className="col-span-2 sm:col-span-3 pt-1 border-t border-slate-200/80 flex items-center justify-between">
                <span className="text-[10px] font-bold text-slate-600 uppercase font-sans">Verification Status:</span>
                <span className={`inline-flex items-center gap-1 font-bold text-[10px] px-2.5 py-0.5 rounded-full ${
                  evidence.verificationStatus === 'VERIFIED'
                    ? 'bg-emerald-100 text-emerald-800 border border-emerald-200'
                    : evidence.verificationStatus === 'PARTIALLY_VERIFIED'
                    ? 'bg-amber-100 text-amber-800 border border-amber-200'
                    : 'bg-rose-100 text-rose-800 border border-rose-200'
                }`}>
                  {evidence.verificationStatus}
                </span>
              </div>
            </div>
          </div>

          {/* SECTION 2: RESULT (Rule & Score attribution) */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <Layers className="w-3.5 h-3.5 text-intel-navy" />
              <span>2. Evaluation Rule, Score &amp; Result</span>
            </h4>
            <div className="ent-card p-4 rounded-xl space-y-3 bg-white border border-slate-200">
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-400 font-mono">Rule</span>
                  <h4 className="text-xs font-bold text-slate-900">{evidence.rule_name || evidence.ruleId || 'Audit Rule'}</h4>
                  <span className="text-[10px] text-slate-500 font-mono">{evidence.ruleId || evidence.rule_id} &bull; v{evidence.ruleVersion || evidence.rule_version || '1.0'}</span>
                </div>

                <div className="flex items-center space-x-3 text-right">
                  <div>
                    <span className="text-[10px] font-bold uppercase text-slate-400 font-mono block">Score</span>
                    <strong className="text-sm font-black text-slate-900 font-mono block">{scoreDisplay}</strong>
                  </div>
                  <div>
                    <span className="text-[10px] font-bold uppercase text-slate-400 font-mono block">Result</span>
                    <span className={`inline-flex items-center gap-1 font-mono font-bold text-[10px] px-2.5 py-0.5 rounded-full ${
                      isPass
                        ? 'bg-emerald-100 text-emerald-800 border border-emerald-200'
                        : isFail
                        ? 'bg-rose-100 text-rose-800 border border-rose-200'
                        : 'bg-slate-200 text-slate-700 border border-slate-300'
                    }`}>
                      {isPass && <CheckCircle2 className="w-3 h-3" />}
                      {isFail && <XCircle className="w-3 h-3" />}
                      {isUnverified && <AlertTriangle className="w-3 h-3" />}
                      {evidence.result}
                    </span>
                  </div>
                  <div>
                    <span className="text-[10px] font-bold uppercase text-slate-400 font-mono block">Evidence Status</span>
                    <span className={`inline-flex items-center font-mono font-bold text-[10px] px-2.5 py-0.5 rounded-full ${
                      evidence.verificationStatus === 'VERIFIED'
                        ? 'bg-emerald-50 text-emerald-800 border border-emerald-300'
                        : evidence.verificationStatus === 'PARTIALLY_VERIFIED'
                        ? 'bg-amber-50 text-amber-800 border border-amber-300'
                        : 'bg-slate-100 text-slate-700 border border-slate-300'
                    }`}>
                      {evidence.verificationStatus}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* SECTION 3: DETECTION */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <Search className="w-3.5 h-3.5 text-intel-navy" />
              <span>3. What Was Detected</span>
            </h4>
            <div className="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2.5">
              <div>
                <span className="text-[10px] text-slate-500 font-bold block">Detection Reason:</span>
                <p className="text-xs text-slate-800 leading-relaxed">{evidence.detection_reason || evidence.detection?.reason || 'No detection reason recorded.'}</p>
              </div>

              {(evidence.detectedValue || evidence.detected_text) && (
                <div>
                  <span className="text-[10px] text-slate-500 font-bold block">Detected String / Element:</span>
                  <div className="p-2.5 bg-slate-900 text-emerald-400 rounded-lg font-mono text-[11px] break-all border border-slate-800">
                    {String(evidence.detectedValue || evidence.detected_text)}
                  </div>
                </div>
              )}

              {(evidence.detected_element || evidence.detection?.selector) && (
                <div>
                  <span className="text-[10px] text-slate-500 font-bold block">DOM Selector / Element:</span>
                  <code className="p-1.5 bg-slate-200 text-slate-800 rounded font-mono text-[10px] block truncate">
                    {evidence.detected_element || evidence.detection?.selector}
                  </code>
                </div>
              )}
            </div>
          </div>

          {/* SECTION 4: RAW EVIDENCE */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <FileText className="w-3.5 h-3.5 text-intel-navy" />
              <span>4. Raw Captured Evidence (Un-normalized)</span>
            </h4>
            {evidence.rawEvidence?.text || evidence.raw_source_text ? (
              <pre className="p-3 bg-slate-900 text-slate-200 rounded-xl font-mono text-[10px] overflow-x-auto border border-slate-800 leading-relaxed max-h-44">
                {evidence.rawEvidence?.text || evidence.raw_source_text}
              </pre>
            ) : evidence.rawEvidence?.attributes ? (
              <pre className="p-3 bg-slate-900 text-slate-200 rounded-xl font-mono text-[10px] overflow-x-auto border border-slate-800 leading-relaxed max-h-44">
                {JSON.stringify(evidence.rawEvidence.attributes, null, 2)}
              </pre>
            ) : (
              <div className="p-4 bg-slate-50 rounded-xl border border-dashed border-slate-300 text-center text-slate-500 font-medium">
                Raw evidence unavailable
              </div>
            )}
          </div>

          {/* SECTION 5: SOURCE */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <Globe className="w-3.5 h-3.5 text-intel-navy" />
              <span>5. Storefront Source Link</span>
            </h4>
            <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs">
              <div className="font-mono text-[11px] text-slate-700 truncate max-w-md">
                {hasSourceUrl ? sourceUrl : 'Source unavailable'}
              </div>
              {hasSourceUrl ? (
                <a
                  href={sourceUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="px-3 py-1.5 rounded-lg bg-intel-navy text-white hover:bg-intel-blue font-semibold text-xs inline-flex items-center space-x-1 shrink-0 shadow-2xs"
                >
                  <span>Verify Source</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              ) : (
                <button
                  disabled
                  className="px-3 py-1.5 rounded-lg bg-slate-200 text-slate-400 font-semibold text-xs cursor-not-allowed"
                >
                  Source unavailable
                </button>
              )}
            </div>
          </div>

          {/* SECTION 6: VISUAL EVIDENCE */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <Camera className="w-3.5 h-3.5 text-intel-navy" />
              <span>6. Captured Visual Screenshot</span>
            </h4>
            {hasScreenshot && screenshotUrl ? (
              <div className="rounded-xl overflow-hidden border border-slate-200 bg-slate-100 relative group">
                <div className="p-2 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-[10px] text-slate-600 font-mono">
                  <span>Captured at: <strong>{screenshotTimestamp || 'Not captured'}</strong></span>
                  <span>Page: <strong>{screenshotPage}</strong></span>
                </div>
                <div className="max-h-64 overflow-hidden flex items-center justify-center">
                  <img
                    src={screenshotUrl}
                    alt={evidence.productTitle || 'Captured screenshot'}
                    className="w-full h-full object-cover"
                    onError={(e: any) => {
                      e.target.style.display = 'none';
                      e.target.parentElement.innerHTML = '<div class="p-6 text-center text-xs text-slate-500 font-medium">Screenshot unavailable</div>';
                    }}
                  />
                </div>
              </div>
            ) : (
              <div className="p-6 rounded-xl border border-dashed border-slate-300 bg-slate-50 text-center space-y-1">
                <EyeOff className="w-5 h-5 text-slate-400 mx-auto" />
                <div className="text-xs font-bold text-slate-700">Screenshot unavailable</div>
                <p className="text-[10px] text-slate-500 max-w-xs mx-auto">
                  No visual screenshot was captured during extraction for this specific component.
                </p>
              </div>
            )}
          </div>

          {/* SECTION 7: MEDIA EVIDENCE */}
          <div className="space-y-2">
            <h4 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 font-mono flex items-center gap-1.5">
              <Video className="w-3.5 h-3.5 text-intel-navy" />
              <span>7. Rich Media Evidence</span>
            </h4>
            {hasMedia && mediaUrl ? (
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1 font-mono text-[11px]">
                <div><span className="text-slate-500">Media Type:</span> <strong className="text-slate-900">{evidence.media?.mediaType || 'IMAGE'}</strong></div>
                <div><span className="text-slate-500">Media URL:</span> <span className="text-intel-blue underline truncate block">{mediaUrl}</span></div>
              </div>
            ) : (
              <div className="p-4 bg-slate-50 rounded-xl border border-dashed border-slate-300 text-center text-slate-500 font-medium">
                Media evidence unavailable
              </div>
            )}
          </div>
        </div>

        {/* Drawer Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-200 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-slate-800 text-white hover:bg-slate-900 font-semibold text-xs"
          >
            Close Audit Drawer
          </button>
        </div>
      </div>
    </div>
  );
};
