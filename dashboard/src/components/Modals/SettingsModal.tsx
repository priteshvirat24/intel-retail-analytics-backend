import React, { useState } from 'react';
import { SlidersHorizontal, X, ShieldCheck, Check, Save } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { CostGuardrails } from '../../types';

export const SettingsModal: React.FC = () => {
  const { settingsModalOpen, setSettingsModalOpen, guardrails, updateGuardrails } = useApp();
  const [formData, setFormData] = useState<CostGuardrails>(guardrails);
  const [saved, setSaved] = useState(false);

  if (!settingsModalOpen) return null;

  const handleSave = () => {
    updateGuardrails(formData);
    setSaved(true);
    setTimeout(() => {
      setSaved(false);
      setSettingsModalOpen(false);
    }, 600);
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl w-full max-w-md overflow-hidden shadow-2xl animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="p-1.5 rounded-lg bg-intel-navy text-white">
              <SlidersHorizontal className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900">Cost Guardrails &amp; Settings</h3>
              <p className="text-[11px] text-slate-500">Tune rate limits, cache TTL, and budgets</p>
            </div>
          </div>
          <button
            onClick={() => setSettingsModalOpen(false)}
            className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-4 text-xs">
          <div className="space-y-3">
            <div>
              <label className="block text-[11px] font-semibold text-slate-700 mb-1">
                Max Live Requests per Session:
              </label>
              <input
                type="number"
                value={formData.session_limit}
                onChange={(e) => setFormData({ ...formData, session_limit: Number(e.target.value) })}
                className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 font-mono text-slate-900 focus:bg-white focus:outline-none focus:border-intel-blue"
              />
              <span className="text-[10px] text-slate-500 mt-0.5 block">Prevents runaway batch jobs in a single session.</span>
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-slate-700 mb-1">
                Max Live Requests per Retailer:
              </label>
              <input
                type="number"
                value={formData.retailer_limit}
                onChange={(e) => setFormData({ ...formData, retailer_limit: Number(e.target.value) })}
                className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 font-mono text-slate-900 focus:bg-white focus:outline-none focus:border-intel-blue"
              />
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-slate-700 mb-1">
                Max Live Requests per URL:
              </label>
              <input
                type="number"
                value={formData.url_limit}
                onChange={(e) => setFormData({ ...formData, url_limit: Number(e.target.value) })}
                className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 font-mono text-slate-900 focus:bg-white focus:outline-none focus:border-intel-blue"
              />
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-slate-700 mb-1">
                Local Cache TTL (Days):
              </label>
              <input
                type="number"
                value={formData.cache_ttl_days}
                onChange={(e) => setFormData({ ...formData, cache_ttl_days: Number(e.target.value) })}
                className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 font-mono text-slate-900 focus:bg-white focus:outline-none focus:border-intel-blue"
              />
            </div>

            <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-200">
              <div>
                <span className="font-semibold text-slate-900 block text-[11px]">Duplicate URL Protection</span>
                <span className="text-[10px] text-slate-500 block">Deduplicates URLs before issuing live requests</span>
              </div>
              <input
                type="checkbox"
                checked={formData.duplicate_url_protection}
                onChange={(e) => setFormData({ ...formData, duplicate_url_protection: e.target.checked })}
                className="w-4 h-4 text-intel-blue rounded focus:ring-intel-blue cursor-pointer"
              />
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-200 flex justify-end space-x-2">
          <button
            onClick={() => setSettingsModalOpen(false)}
            className="px-3.5 py-1.5 rounded-lg border border-slate-300 text-slate-700 hover:bg-slate-100 font-medium text-xs"
          >
            Cancel
          </button>
          <button
            onClick={handleSave}
            className="px-4 py-1.5 rounded-lg bg-intel-navy text-white hover:bg-intel-blue font-semibold text-xs flex items-center space-x-1.5 shadow-sm"
          >
            {saved ? <Check className="w-3.5 h-3.5 text-emerald-300" /> : <Save className="w-3.5 h-3.5" />}
            <span>{saved ? 'Saved!' : 'Save Settings'}</span>
          </button>
        </div>
      </div>
    </div>
  );
};
