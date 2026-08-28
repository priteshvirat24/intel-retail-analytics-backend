import React, { useState } from 'react';
import { ShieldCheck, CheckCircle2, XCircle, ChevronDown, ChevronUp, AlertCircle, HelpCircle } from 'lucide-react';
import { useApp } from '../context/AppContext';

export const RetailerAuditView: React.FC = () => {
  const { retailers, products, setSelectedSkuDetail } = useApp();
  const [selectedRetailer, setSelectedRetailer] = useState<string>('ALL');

  const filteredProducts = selectedRetailer === 'ALL'
    ? products
    : products.filter((p) => p.retailer === selectedRetailer);

  const flagDefinitions = [
    { key: 'S1', label: 'Listing Page Title Branding', weight: 'Search/SERP' },
    { key: 'S2', label: 'Listing Page Badge Presence', weight: 'Search/SERP' },
    { key: 'P1', label: 'PDP Title Branding Mentions', weight: 'Product Page' },
    { key: 'P2', label: 'PDP Official Platform Badge', weight: 'Product Page' },
    { key: 'P3', label: 'PDP Spec Precision', weight: 'Hardware Table' },
    { key: 'P4', label: 'Intel A+ Rich Media Modules', weight: 'Marketing' },
    { key: 'P5', label: 'OEM Interactive 3D / Video', weight: 'Marketing' },
  ];

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-emerald-600" />
            <span>Retailer Audit &amp; Brand Compliance Scoring</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            S1, S2, P1, P2, P3, P4, P5 rule verification rolled up into a Brand Compliance Score weighted <strong className="text-slate-800 font-semibold">85% Laptop / 15% Desktop</strong>
          </p>
        </div>

        <div className="flex items-center space-x-3 bg-white p-3 rounded-xl border border-slate-200 shadow-2xs font-mono text-xs">
          <span className="text-slate-500">Program Score:</span>
          <span className="text-xl font-extrabold text-emerald-600">72.7%</span>
          <span className="text-[10px] text-slate-400 font-sans">(85/15 Weighted)</span>
        </div>
      </div>

      {/* Flag Definitions Strip */}
      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2.5">
        {flagDefinitions.map((f) => (
          <div key={f.key} className="ent-card p-3 rounded-xl">
            <div className="flex items-center justify-between text-xs mb-1">
              <span className="font-mono font-bold text-intel-navy">{f.key}</span>
              <span className="text-[10px] text-slate-500">{f.weight}</span>
            </div>
            <p className="text-[11px] font-medium text-slate-700 line-clamp-2 leading-tight">
              {f.label}
            </p>
          </div>
        ))}
      </div>

      {/* Retailer Scorecards */}
      <div>
        <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3">
          Channel Compliance Scorecards (85% Laptop / 15% Desktop Weighting)
        </h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          {retailers.map((r) => (
            <div
              key={r.id}
              onClick={() => setSelectedRetailer(selectedRetailer === r.name ? 'ALL' : r.name)}
              className={`ent-card ent-card-hover p-4 rounded-xl cursor-pointer ${
                selectedRetailer === r.name ? 'ring-2 ring-intel-navy bg-blue-50/20' : ''
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <h4 className="text-sm font-bold text-slate-900">{r.name}</h4>
                <span className="text-xs font-mono font-bold text-emerald-700">
                  {r.brand_compliance_score}%
                </span>
              </div>
              <div className="space-y-1 text-xs text-slate-600">
                <div className="flex justify-between">
                  <span>Laptop Score (85%):</span>
                  <span className="text-slate-900 font-mono font-semibold">{r.laptop_compliance_score}%</span>
                </div>
                <div className="flex justify-between">
                  <span>Desktop Score (15%):</span>
                  <span className="text-slate-900 font-mono font-semibold">{r.desktop_compliance_score}%</span>
                </div>
                <div className="flex justify-between pt-1 border-t border-slate-100 text-[11px]">
                  <span>Compliance Grade:</span>
                  <span className="text-intel-navy font-bold">{r.compliance_grade}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* SKU-Level Pass/Fail Audit Matrix */}
      <div className="ent-card rounded-xl overflow-hidden shadow-2xs">
        <div className="p-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between flex-wrap gap-2">
          <div>
            <h3 className="text-sm font-bold text-slate-900">SKU-Level S1..P5 Audit Pass/Fail Matrix</h3>
            <p className="text-xs text-slate-500">
              Showing {filteredProducts.length} SKUs {selectedRetailer !== 'ALL' ? `(Filtered: ${selectedRetailer})` : ''}
            </p>
          </div>
          {selectedRetailer !== 'ALL' && (
            <button
              onClick={() => setSelectedRetailer('ALL')}
              className="text-xs text-intel-blue hover:underline font-semibold"
            >
              Show All Channels
            </button>
          )}
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs whitespace-nowrap">
            <thead className="ent-table-header">
              <tr>
                <th className="py-2.5 px-4">SKU / Model</th>
                <th className="py-2.5 px-3">Retailer</th>
                <th className="py-2.5 px-3">Form Factor</th>
                <th className="py-2.5 px-2 text-center">S1</th>
                <th className="py-2.5 px-2 text-center">S2</th>
                <th className="py-2.5 px-2 text-center">P1</th>
                <th className="py-2.5 px-2 text-center">P2</th>
                <th className="py-2.5 px-2 text-center">P3</th>
                <th className="py-2.5 px-2 text-center">P4</th>
                <th className="py-2.5 px-2 text-center">P5</th>
                <th className="py-2.5 px-3 text-right">Audit Score</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 text-slate-700">
              {filteredProducts.map((p) => (
                <tr
                  key={p.sku_id}
                  onClick={() => setSelectedSkuDetail(p)}
                  className="ent-table-row cursor-pointer"
                >
                  <td className="py-2.5 px-4 font-semibold text-slate-900">
                    <div>{p.oem} {p.model_series}</div>
                    <div className="text-[10px] text-slate-400 font-mono">{p.processor_model}</div>
                  </td>
                  <td className="py-2.5 px-3 text-slate-700">{p.retailer}</td>
                  <td className="py-2.5 px-3">{p.form_factor}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.S1?.pass)}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.S2?.pass)}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.P1?.pass)}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.P2?.pass)}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.P3?.pass)}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.P4?.pass)}</td>
                  <td className="py-2.5 px-2 text-center">{renderPassIcon(p.audit_flags?.P5?.pass)}</td>
                  <td className="py-2.5 px-3 text-right">
                    <span className={`px-2 py-0.5 rounded-md font-bold font-mono text-[11px] ${
                      p.compliance_score >= 80 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                    }`}>
                      {p.compliance_score}%
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

const renderPassIcon = (passed?: boolean) => {
  return passed ? (
    <CheckCircle2 className="w-4 h-4 text-emerald-600 inline" />
  ) : (
    <XCircle className="w-4 h-4 text-rose-500 inline" />
  );
};
