import React, { useState } from 'react';
import { Terminal, X, Zap, AlertCircle, ShieldAlert, Lock, CheckCircle2 } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const RunSampleModal: React.FC = () => {
  const { runSampleModalOpen, setRunSampleModalOpen, executeRunSample } = useApp();
  const [selectedRetailer, setSelectedRetailer] = useState<string>('Best Buy');
  const [sampleCount, setSampleCount] = useState<number>(3);
  const [mode, setMode] = useState<string>('Full PDP Spec Parse');
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [completed, setCompleted] = useState<boolean>(false);

  if (!runSampleModalOpen) return null;

  const handleRun = async () => {
    setIsRunning(true);
    await executeRunSample(selectedRetailer, sampleCount, mode);
    setIsRunning(false);
    setCompleted(true);
  };

  const handleClose = () => {
    setRunSampleModalOpen(false);
    setCompleted(false);
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl w-full max-w-lg overflow-hidden shadow-2xl animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="p-1.5 rounded-lg bg-intel-navy text-white">
              <Terminal className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900">RUN SAMPLE EXTRACTION</h3>
              <p className="text-[11px] text-slate-500">Controlled small-batch Bright Data runner</p>
            </div>
          </div>
          <button onClick={handleClose} className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-4 text-xs">
          {!completed ? (
            <>
              {/* Cost Guardrail Notice */}
              <div className="p-3 bg-blue-50 rounded-xl border border-blue-200 text-blue-900 flex items-start space-x-2">
                <ShieldAlert className="w-4 h-4 text-intel-blue shrink-0 mt-0.5" />
                <div className="text-[11px] space-y-0.5">
                  <span className="font-semibold block">Strict POC Sample Guardrail Active:</span>
                  <span className="text-blue-800 block">
                    Maximum sample size is capped at <strong>3 URLs</strong> per execution to prevent unnecessary Bright Data charges.
                  </span>
                </div>
              </div>

              {/* Form Controls */}
              <div className="space-y-3">
                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">Target Retailer:</label>
                  <select
                    value={selectedRetailer}
                    onChange={(e) => setSelectedRetailer(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 text-xs font-medium text-slate-900 focus:bg-white focus:outline-none focus:border-intel-blue"
                  >
                    <option value="Best Buy">Best Buy US (1P Retailer)</option>
                    <option value="Walmart">Walmart US (1P Retailer)</option>
                    <option value="Costco">Costco US (1P Retailer)</option>
                    <option value="Amazon US">Amazon US (3P Marketplace)</option>
                    <option value="Dell Direct">Dell Direct (OEM Site)</option>
                    <option value="HP Direct">HP Direct (OEM Site)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">
                    Sample Size (Max 3 URLs in POC):
                  </label>
                  <div className="grid grid-cols-3 gap-2">
                    {[1, 2, 3].map((num) => (
                      <button
                        key={num}
                        type="button"
                        onClick={() => setSampleCount(num)}
                        className={`py-1.5 rounded-lg border text-xs font-bold font-mono transition-colors ${
                          sampleCount === num
                            ? 'bg-intel-navy text-white border-intel-navy shadow-xs'
                            : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                        }`}
                      >
                        {num} URL{num > 1 ? 's' : ''}
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">Extraction Mode:</label>
                  <select
                    value={mode}
                    onChange={(e) => setMode(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 text-xs font-medium text-slate-900 focus:bg-white focus:outline-none focus:border-intel-blue"
                  >
                    <option value="Full PDP Spec Parse">Full PDP Hardware Spec &amp; Audit Parse (Recommended)</option>
                    <option value="Fast SERP Discovery">Fast SERP Listing &amp; SOV Discovery</option>
                  </select>
                </div>

                {/* Impact Calculator */}
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 text-[11px] space-y-1 font-mono text-slate-600">
                  <div className="flex justify-between">
                    <span>Bright Data Requests:</span>
                    <span className="font-bold text-intel-navy">+{sampleCount}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Estimated Cost Impact:</span>
                    <span className="font-bold text-slate-800">~${(sampleCount * 0.02).toFixed(2)}</span>
                  </div>
                </div>

                {/* Disabled Full Scrape Architecture Button */}
                <div className="pt-2">
                  <button
                    disabled
                    className="w-full py-2 rounded-xl bg-slate-100 border border-slate-300 text-slate-400 text-xs font-semibold flex items-center justify-center space-x-2 cursor-not-allowed"
                  >
                    <Lock className="w-3.5 h-3.5" />
                    <span>Scrape All 173 Retailers &amp; Full Catalog</span>
                    <span className="text-[10px] px-1.5 py-0.2 rounded bg-amber-100 text-amber-800 border border-amber-300">
                      Disabled in POC
                    </span>
                  </button>
                </div>
              </div>
            </>
          ) : (
            <div className="p-6 bg-emerald-50 rounded-xl border border-emerald-200 text-emerald-900 space-y-2 text-center">
              <CheckCircle2 className="w-8 h-8 text-emerald-600 mx-auto" />
              <h4 className="text-sm font-bold">Sample Extraction Completed</h4>
              <p className="text-xs text-emerald-800">
                Extracted and cached {sampleCount} SKUs from {selectedRetailer}. Request history and cost counters updated.
              </p>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-200 flex justify-end space-x-2">
          {!completed ? (
            <>
              <button
                onClick={handleClose}
                className="px-3.5 py-1.5 rounded-lg border border-slate-300 text-slate-700 hover:bg-slate-100 font-medium text-xs"
              >
                Cancel
              </button>
              <button
                onClick={handleRun}
                disabled={isRunning}
                className="px-4 py-1.5 rounded-lg bg-intel-navy text-white hover:bg-intel-blue font-semibold text-xs flex items-center space-x-1.5 shadow-sm"
              >
                <Zap className="w-3.5 h-3.5" />
                <span>{isRunning ? 'Running Sample...' : `Run ${sampleCount} URL Sample`}</span>
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
