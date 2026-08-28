import React, { useState } from 'react';
import { AlertCircle, X, CheckCircle2, Zap, ShieldCheck } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const LiveValidationModal: React.FC = () => {
  const { liveValidationTarget, setLiveValidationTarget, executeLiveValidation } = useApp();
  const [isValidating, setIsValidating] = useState(false);
  const [result, setResult] = useState<{ success: boolean; fromCache: boolean } | null>(null);

  if (!liveValidationTarget) return null;

  const handleValidate = async () => {
    setIsValidating(true);
    const res = await executeLiveValidation(liveValidationTarget);
    setResult(res);
    setIsValidating(false);
  };

  const handleClose = () => {
    setLiveValidationTarget(null);
    setResult(null);
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl w-full max-w-lg overflow-hidden shadow-2xl animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="p-1.5 rounded-lg bg-amber-100 border border-amber-300 text-amber-800">
              <Zap className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900">LIVE VALIDATION</h3>
              <p className="text-[11px] text-slate-500">Controlled Bright Data invocation guardrail</p>
            </div>
          </div>
          <button onClick={handleClose} className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-4 text-xs">
          {!result ? (
            <>
              <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-amber-900 flex items-start space-x-2.5">
                <AlertCircle className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
                <div className="space-y-0.5">
                  <span className="font-semibold block">This action may consume a Bright Data request.</span>
                  <span className="text-[11px] text-amber-800 block">
                    The POC engine checks local cache and duplicate requests before making a live network call.
                  </span>
                </div>
              </div>

              <div className="space-y-2.5 bg-slate-50 p-4 rounded-xl border border-slate-200">
                <div>
                  <span className="text-[11px] text-slate-500 block">Target Product SKU:</span>
                  <span className="font-semibold text-slate-900">{liveValidationTarget.oem} {liveValidationTarget.model_series}</span>
                </div>

                <div>
                  <span className="text-[11px] text-slate-500 block">Target URL:</span>
                  <span className="font-mono text-slate-700 break-all text-[11px] block">{liveValidationTarget.sourceUrl}</span>
                </div>

                <div className="grid grid-cols-2 gap-3 pt-2 border-t border-slate-200 text-[11px]">
                  <div>
                    <span className="text-slate-500 block">Previous Extraction:</span>
                    <span className="font-semibold text-slate-800">1.2 hours ago</span>
                  </div>
                  <div>
                    <span className="text-slate-500 block">Cache Status:</span>
                    <span className="font-semibold text-emerald-600">Available (Valid TTL)</span>
                  </div>
                  <div>
                    <span className="text-slate-500 block">Estimated Request Impact:</span>
                    <span className="font-semibold font-mono text-intel-navy">1 Request (or 0 if cached)</span>
                  </div>
                  <div>
                    <span className="text-slate-500 block">Estimated Cost:</span>
                    <span className="font-semibold font-mono text-slate-800">&le; $0.02</span>
                  </div>
                </div>
              </div>
            </>
          ) : (
            <div className="p-4 bg-emerald-50 rounded-xl border border-emerald-200 text-emerald-900 space-y-2 text-center">
              <CheckCircle2 className="w-8 h-8 text-emerald-600 mx-auto" />
              <h4 className="text-sm font-bold">Validation Successful</h4>
              <p className="text-xs text-emerald-800">
                {result.fromCache
                  ? '⚡ Returned from Local Cache (0 Bright Data requests consumed).'
                  : '🌐 Live Bright Data request executed successfully and cached.'}
              </p>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-200 flex justify-end space-x-2">
          {!result ? (
            <>
              <button
                onClick={handleClose}
                className="px-3.5 py-1.5 rounded-lg border border-slate-300 text-slate-700 hover:bg-slate-100 font-medium text-xs"
              >
                Cancel
              </button>
              <button
                onClick={handleValidate}
                disabled={isValidating}
                className="px-4 py-1.5 rounded-lg bg-intel-navy text-white hover:bg-intel-blue font-semibold text-xs flex items-center space-x-1.5 shadow-sm"
              >
                <Zap className="w-3.5 h-3.5" />
                <span>{isValidating ? 'Validating...' : 'Validate'}</span>
              </button>
            </>
          ) : (
            <button
              onClick={handleClose}
              className="px-4 py-1.5 rounded-lg bg-emerald-700 text-white hover:bg-emerald-800 font-semibold text-xs"
            >
              Done
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
