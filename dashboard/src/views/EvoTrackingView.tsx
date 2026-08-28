import React, { useState } from 'react';
import { Award, CheckCircle2, DollarSign, TrendingUp, Sparkles, Laptop, Store, Cpu, Inbox } from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend
} from 'recharts';
import { useApp } from '../context/AppContext';
import { EvoSubTab, ScorecardSKU } from '../types/scorecards';

export const EvoTrackingView: React.FC = () => {
  const { setSelectedSkuDetail, filteredScorecardProducts, filteredScorecardAccounts, oemDistribution } = useApp() as any;
  const [subTab, setSubTab] = useState<EvoSubTab>('evo-overview');

  const products: ScorecardSKU[] = filteredScorecardProducts || [];
  const accounts = filteredScorecardAccounts || [];

  const evoProducts = products.filter((p: any) => p.Evo === 'Y' || p.intel_evo_certified === true);

  const evoByRetailerData = accounts.slice(0, 10).map((a: any) => {
    const aProds = products.filter((p: any) => (p.account || p.retailer) === a.account);
    const aEvo = aProds.filter((p: any) => p.Evo === 'Y').length;
    return {
      name: a.account.length > 14 ? a.account.slice(0, 12) + '..' : a.account,
      total: aProds.length,
      evo: aEvo,
      rate: aProds.length > 0 ? Math.round((aEvo / aProds.length) * 100) : 0,
    };
  }).filter((d: any) => d.total > 0);

  const evoByOemData = (oemDistribution || []).map((o: any) => {
    const oProds = products.filter((p: any) => (p.oem || '').toLowerCase() === o.oem.toLowerCase());
    const oEvo = oProds.filter((p: any) => p.Evo === 'Y').length;
    return {
      name: o.oem,
      total: o.count,
      evo: oEvo,
    };
  });

  const evoAvgPrice = evoProducts.length > 0
    ? Math.round(evoProducts.reduce((a: number, b: any) => a + (b.usd_selling_price || b.selling_price || 0), 0) / evoProducts.length)
    : null;

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Award className="w-5 h-5 text-purple-600" />
            <span>Intel EVO Badge Tracking &amp; Certification Adoption</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Monitoring official Intel EVO / Evo Edition badge presence, listing mentions, and premium price corridors
          </p>
        </div>

        {/* 4 EVO SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'evo-overview', label: 'EVO Overview' },
            { id: 'evo-products', label: 'EVO Products' },
            { id: 'evo-retailer', label: 'EVO by Retailer' },
            { id: 'evo-oem', label: 'EVO by OEM' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as EvoSubTab)}
              className={`px-3 py-1.5 rounded-lg transition-colors ${
                subTab === tab.id
                  ? 'bg-intel-navy text-white shadow-xs font-bold'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {evoProducts.length === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No EVO Certified SKUs Found</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no EVO-certified products matching your active filter selection.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* Top Dynamic KPI Cards */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Certified EVO Models
              </div>
              <div className="text-2xl font-black text-purple-700 mt-1">
                {evoProducts.length} <span className="text-xs text-slate-400 font-normal">SKUs</span>
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                {products.length > 0 ? `${Math.round((evoProducts.length / products.length) * 100)}% of active catalog` : '0%'}
              </div>
            </div>

            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Average EVO Price (ASP)
              </div>
              <div className="text-2xl font-black text-slate-900 mt-1">
                {evoAvgPrice !== null ? `$${evoAvgPrice.toLocaleString()}` : 'N/A'}
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Normalized Premium Rate
              </div>
            </div>

            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Active EVO Partners
              </div>
              <div className="text-2xl font-black text-intel-navy mt-1">
                {new Set(evoProducts.map((p: any) => p.oem)).size} OEMs
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Dell, HP, Lenovo, LG, ASUS
              </div>
            </div>

            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Retail Storefronts with EVO
              </div>
              <div className="text-2xl font-black text-emerald-600 mt-1">
                {new Set(evoProducts.map((p: any) => p.account)).size} Storefronts
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Certified Badge Deployments
              </div>
            </div>
          </div>

          {/* TAB 1: OVERVIEW */}
          {subTab === 'evo-overview' && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="ent-card p-5 rounded-2xl shadow-xs">
                <h4 className="text-sm font-bold text-slate-900 mb-1">EVO Certified Model Count by Storefront</h4>
                <p className="text-xs text-slate-500 mb-4">Total SKUs vs EVO certified models</p>
                <div className="h-64">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={evoByRetailerData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                      <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} angle={-25} textAnchor="end" />
                      <YAxis tick={{ fontSize: 10, fill: '#64748B' }} />
                      <Tooltip />
                      <Legend verticalAlign="top" height={30} />
                      <Bar dataKey="total" name="Total SKUs" fill="#94A3B8" />
                      <Bar dataKey="evo" name="EVO Certified" fill="#7C3AED" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>

              <div className="ent-card p-5 rounded-2xl shadow-xs">
                <h4 className="text-sm font-bold text-slate-900 mb-1">EVO Platform Adoption by OEM Brand</h4>
                <p className="text-xs text-slate-500 mb-4">Hardware manufacturer certification adoption</p>
                <div className="h-64">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={evoByOemData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                      <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} />
                      <YAxis tick={{ fontSize: 10, fill: '#64748B' }} />
                      <Tooltip />
                      <Bar dataKey="evo" name="EVO Models" fill="#7C3AED" radius={[4, 4, 0, 0]} />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: EVO PRODUCTS */}
          {subTab === 'evo-products' && (
            <div className="ent-card p-5 rounded-2xl shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Certified Intel EVO Models</h4>
              <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Title</th>
                      <th className="py-2.5 px-2">Account</th>
                      <th className="py-2.5 px-2">OEM</th>
                      <th className="py-2.5 px-2">Processor</th>
                      <th className="py-2.5 px-2 text-right">Price</th>
                      <th className="py-2.5 px-3 text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {evoProducts.slice(0, 50).map((p: any, idx: number) => (
                      <tr
                        key={p.product_id || p.sku_index || idx}
                        onClick={() => setSelectedSkuDetail(p)}
                        className="hover:bg-slate-50/80 cursor-pointer"
                      >
                        <td className="py-2 px-3 font-medium text-slate-900 max-w-sm truncate">{p.product_title}</td>
                        <td className="py-2 px-2 text-slate-600 font-semibold">{p.account}</td>
                        <td className="py-2 px-2 text-slate-700">{p.oem}</td>
                        <td className="py-2 px-2">
                          <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-purple-100 text-purple-800">
                            {p.processor_model || p.processor}
                          </span>
                        </td>
                        <td className="py-2 px-2 text-right font-mono font-bold text-slate-900">
                          ${p.selling_price?.toLocaleString()}
                        </td>
                        <td className="py-2 px-3 text-right">
                          <button
                            onClick={(e) => {
                              e.stopPropagation();
                              setSelectedSkuDetail(p);
                            }}
                            className="text-intel-blue hover:underline font-semibold text-[11px]"
                          >
                            Inspect
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 3: BY RETAILER */}
          {subTab === 'evo-retailer' && (
            <div className="ent-card p-5 rounded-2xl shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Storefront EVO Adoption</h4>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Account</th>
                      <th className="py-2.5 px-2 text-center">Total SKUs</th>
                      <th className="py-2.5 px-2 text-center">EVO Certified</th>
                      <th className="py-2.5 px-3 text-right">Adoption Rate</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {evoByRetailerData.map((r: any) => (
                      <tr key={r.name} className="hover:bg-slate-50/80">
                        <td className="py-2 px-3 font-bold text-slate-900">{r.name}</td>
                        <td className="py-2 px-2 text-center font-mono">{r.total}</td>
                        <td className="py-2 px-2 text-center font-mono font-bold text-purple-700">{r.evo}</td>
                        <td className="py-2 px-3 text-right font-mono font-black text-emerald-600">{r.rate}%</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 4: BY OEM */}
          {subTab === 'evo-oem' && (
            <div className="ent-card p-5 rounded-2xl shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">OEM Hardware EVO Adoption</h4>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">OEM</th>
                      <th className="py-2.5 px-2 text-center">Total SKUs</th>
                      <th className="py-2.5 px-2 text-center">EVO Models</th>
                      <th className="py-2.5 px-3 text-right">EVO Share %</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {evoByOemData.map((o: any) => (
                      <tr key={o.name} className="hover:bg-slate-50/80">
                        <td className="py-2 px-3 font-bold text-slate-900">{o.name}</td>
                        <td className="py-2 px-2 text-center font-mono">{o.total}</td>
                        <td className="py-2 px-2 text-center font-mono font-bold text-purple-700">{o.evo}</td>
                        <td className="py-2 px-3 text-right font-mono font-black text-emerald-600">
                          {o.total > 0 ? Math.round((o.evo / o.total) * 100) : 0}%
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
};
