import React, { useState } from 'react';
import { Layers, Award, TrendingUp, Cpu, ArrowUpRight, AlertCircle, ExternalLink, Globe, Laptop, Store, Inbox } from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
  PieChart,
  Pie,
  Cell
} from 'recharts';
import { useApp } from '../context/AppContext';
import { SosSubTab, ScorecardSKU } from '../types/scorecards';

export const ShareOfShelfView: React.FC = () => {
  const {
    setSelectedSkuDetail,
    filteredScorecardProducts,
    filteredScorecardAccounts,
    sosDistribution,
    oemDistribution,
    overviewKpis,
    programConfig
  } = useApp() as any;

  const [subTab, setSubTab] = useState<SosSubTab>('sos-overview');

  const products = filteredScorecardProducts || [];
  const accounts = filteredScorecardAccounts || [];

  // Dynamic Retailer Breakdown Chart Data from actual records
  const retailerChartData = accounts.map((a: any) => {
    const rProducts = products.filter((p: any) => (p.account || p.retailer) === a.account);
    const getCount = (procPattern: RegExp) =>
      rProducts.filter((p: any) => procPattern.test(p.processor || p.processor_brand || '')).length;

    return {
      name: a.account.length > 14 ? a.account.slice(0, 12) + '..' : a.account,
      Intel: getCount(/intel/i),
      AMD: getCount(/amd|ryzen/i),
      Apple: getCount(/apple|m1|m2|m3|m4/i),
      Qualcomm: getCount(/qualcomm|snapdragon/i),
      Other: rProducts.length - (getCount(/intel/i) + getCount(/amd|ryzen/i) + getCount(/apple/i) + getCount(/qualcomm/i)),
    };
  }).filter((d: any) => d.Intel + d.AMD + d.Apple + d.Qualcomm + d.Other > 0);

  // Dynamic Pie Data from sosDistribution
  const pieData = sosDistribution && sosDistribution.length > 0
    ? sosDistribution.map((item: any) => ({
        name: `${item.name} (${item.percentage}%)`,
        value: item.count,
        color: item.color || '#0071C5',
      }))
    : [];

  // Dynamic OEM Ranks from oemDistribution
  const dynamicOemRanks = (oemDistribution || []).map((o: any, idx: number) => {
    const oemProducts = products.filter((p: any) => (p.oem || '').toLowerCase() === o.oem.toLowerCase());
    const amdCount = oemProducts.filter((p: any) => /amd|ryzen/i.test(p.processor || '')).length;
    const otherCount = oemProducts.length - o.intelCount - amdCount;

    return {
      rank: idx + 1,
      oem: o.oem,
      total: o.count,
      intel: o.intelCount,
      sos_pct: o.intelPct,
      amd: amdCount,
      other: otherCount,
    };
  });

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Layers className="w-5 h-5 text-intel-navy" />
            <span>Share of Shelf (SOS) Intelligence</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Real-time digital shelf share calculated from first 2 category listing pages across {accounts.length} active retail storefronts
          </p>
        </div>

        {/* 6 SOS SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'sos-overview', label: 'Overview' },
            { id: 'sos-retailer', label: 'By Retailer' },
            { id: 'sos-country', label: 'By Country' },
            { id: 'sos-oem', label: 'By OEM' },
            { id: 'sos-product', label: 'Product Audit' },
            { id: 'category-urls', label: 'Category URLs' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as SosSubTab)}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                subTab === tab.id
                  ? 'bg-intel-navy text-white shadow-xs font-bold'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* ZERO DATA EMPTY STATE */}
      {products.length === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No Share of Shelf Records</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no category listing records matching the active filters to compute Share of Shelf metrics.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* TAB 1: SOS OVERVIEW */}
          {subTab === 'sos-overview' && (
            <div className="space-y-6">
              {/* Top Summary Cards */}
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Global Intel SOS %
                  </div>
                  <div className="text-2xl font-black text-intel-navy mt-1">
                    {overviewKpis.intelSosPct !== null ? `${overviewKpis.intelSosPct}%` : 'N/A'}
                  </div>
                  <div className="text-[11px] text-emerald-600 mt-1 font-semibold">
                    {overviewKpis.intelSkus.toLocaleString()} of {products.length.toLocaleString()} Active SKUs
                  </div>
                </div>

                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Target Accounts Evaluated
                  </div>
                  <div className="text-2xl font-black text-slate-900 mt-1">
                    {accounts.length}
                  </div>
                  <div className="text-[11px] text-slate-500 mt-1 font-medium">
                    {overviewKpis.totalCountries} Countries Filtered
                  </div>
                </div>

                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Leading OEM Partner
                  </div>
                  <div className="text-2xl font-black text-slate-900 mt-1">
                    {dynamicOemRanks[0] ? dynamicOemRanks[0].oem : 'N/A'}
                  </div>
                  <div className="text-[11px] text-intel-blue mt-1 font-semibold">
                    {dynamicOemRanks[0] ? `${dynamicOemRanks[0].sos_pct}% Intel Share` : 'No data'}
                  </div>
                </div>

                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Category Weights (Config)
                  </div>
                  <div className="text-2xl font-black text-slate-900 mt-1">
                    {Math.round(programConfig.category_weights.laptop * 100)}% / {Math.round(programConfig.category_weights.desktop * 100)}%
                  </div>
                  <div className="text-[11px] text-slate-500 mt-1 font-medium">
                    Laptop vs Desktop Weights
                  </div>
                </div>
              </div>

              {/* Visual Charts Grid */}
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Processor Share Breakdown Pie */}
                <div className="ent-card rounded-2xl p-5 shadow-xs">
                  <h4 className="text-sm font-bold text-slate-900 mb-1">Processor Family Share (SOS)</h4>
                  <p className="text-xs text-slate-500 mb-4">Calculated from {products.length.toLocaleString()} total listing records</p>
                  {pieData.length > 0 ? (
                    <div className="h-64">
                      <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                          <Pie
                            data={pieData}
                            cx="50%"
                            cy="50%"
                            innerRadius={55}
                            outerRadius={85}
                            paddingAngle={3}
                            dataKey="value"
                          >
                            {pieData.map((entry: any, index: number) => (
                              <Cell key={`cell-${index}`} fill={entry.color} />
                            ))}
                          </Pie>
                          <Tooltip formatter={(value: any) => [`${value} SKUs`, 'Count']} />
                          <Legend verticalAlign="bottom" height={36} iconType="circle" />
                        </PieChart>
                      </ResponsiveContainer>
                    </div>
                  ) : (
                    <div className="h-64 flex items-center justify-center text-xs text-slate-400">
                      No processor share data
                    </div>
                  )}
                </div>

                {/* Retailer Multi-Stack Bar Chart */}
                <div className="lg:col-span-2 ent-card rounded-2xl p-5 shadow-xs">
                  <div className="flex items-center justify-between mb-4">
                    <div>
                      <h4 className="text-sm font-bold text-slate-900">Processor Breakdown by Retailer Storefront</h4>
                      <p className="text-xs text-slate-500">Intel vs Competitors across active evaluated accounts</p>
                    </div>
                  </div>
                  {retailerChartData.length > 0 ? (
                    <div className="h-64">
                      <ResponsiveContainer width="100%" height="100%">
                        <BarChart data={retailerChartData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                          <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                          <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} angle={-25} textAnchor="end" />
                          <YAxis tick={{ fontSize: 10, fill: '#64748B' }} />
                          <Tooltip />
                          <Legend verticalAlign="top" height={30} />
                          <Bar dataKey="Intel" stackId="a" fill="#0071C5" />
                          <Bar dataKey="AMD" stackId="a" fill="#EF4444" />
                          <Bar dataKey="Apple" stackId="a" fill="#64748B" />
                          <Bar dataKey="Qualcomm" stackId="a" fill="#8B5CF6" />
                        </BarChart>
                      </ResponsiveContainer>
                    </div>
                  ) : (
                    <div className="h-64 flex items-center justify-center text-xs text-slate-400">
                      No retailer breakdown data
                    </div>
                  )}
                </div>
              </div>

              {/* Dynamic OEM SOS Leaderboard Table */}
              <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
                <div>
                  <h4 className="text-sm font-bold text-slate-900">OEM Share of Shelf Leaderboard</h4>
                  <p className="text-xs text-slate-500">Aggregated brand performance across active retail partners</p>
                </div>
                <div className="overflow-x-auto rounded-xl border border-slate-100">
                  <table className="w-full text-left text-xs">
                    <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                      <tr>
                        <th className="py-2.5 px-3">Rank</th>
                        <th className="py-2.5 px-3">OEM Brand</th>
                        <th className="py-2.5 px-2 text-center">Total SKUs</th>
                        <th className="py-2.5 px-2 text-center">Intel SKUs</th>
                        <th className="py-2.5 px-2 text-center">AMD SKUs</th>
                        <th className="py-2.5 px-2 text-center">Other SKUs</th>
                        <th className="py-2.5 px-3 text-right">Intel SOS %</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {dynamicOemRanks.map((o: any) => (
                        <tr key={o.oem} className="hover:bg-slate-50/80">
                          <td className="py-2 px-3 font-mono font-bold text-slate-400">{o.rank}</td>
                          <td className="py-2 px-3 font-bold text-slate-900">{o.oem}</td>
                          <td className="py-2 px-2 text-center font-mono font-semibold">{o.total}</td>
                          <td className="py-2 px-2 text-center font-mono font-bold text-intel-blue">{o.intel}</td>
                          <td className="py-2 px-2 text-center font-mono text-rose-600">{o.amd}</td>
                          <td className="py-2 px-2 text-center font-mono text-slate-400">{o.other}</td>
                          <td className="py-2 px-3 text-right font-mono font-black text-slate-900">
                            <span className={o.sos_pct >= 70 ? 'text-emerald-600' : 'text-amber-600'}>
                              {o.sos_pct}%
                            </span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: BY RETAILER */}
          {subTab === 'sos-retailer' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Retailer Storefront Share Breakdown</h4>
              <p className="text-xs text-slate-500">Detailed count of Intel vs competitor product placements per storefront</p>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Account</th>
                      <th className="py-2.5 px-2">Country</th>
                      <th className="py-2.5 px-2 text-center">Total Verified</th>
                      <th className="py-2.5 px-2 text-center">Intel</th>
                      <th className="py-2.5 px-2 text-center">AMD</th>
                      <th className="py-2.5 px-2 text-center">Apple</th>
                      <th className="py-2.5 px-2 text-center">Qualcomm</th>
                      <th className="py-2.5 px-3 text-right">Intel Share %</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {[...accounts]
                      .map((a: any) => {
                        const rProducts = products.filter((p: any) => (p.account || p.retailer) === a.account);
                        const rTotal = rProducts.length > 0 ? rProducts.length : (a.products_count || 0);
                        const intelCount = rProducts.filter((p: any) => /intel/i.test(p.processor || '')).length;
                        const amdCount = rProducts.filter((p: any) => /amd|ryzen/i.test(p.processor || '')).length;
                        const appleCount = rProducts.filter((p: any) => /apple/i.test(p.processor || '')).length;
                        const qualcommCount = rProducts.filter((p: any) => /qualcomm/i.test(p.processor || '')).length;
                        const sosPct = rTotal > 0 ? Math.round((intelCount / rTotal) * 1000) / 10 : (a.sos_intel_pct || 0);
                        return { ...a, rTotal, intelCount, amdCount, appleCount, qualcommCount, sosPct };
                      })
                      .sort((a, b) => b.sosPct - a.sosPct)
                      .map((a: any, idx: number) => (
                        <tr key={a.account || idx} className="hover:bg-slate-50/80">
                          <td className="py-2 px-3 font-bold text-slate-900">{a.account}</td>
                          <td className="py-2 px-2 text-slate-600">{a.country}</td>
                          <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">
                            {a.rTotal}
                          </td>
                          <td className="py-2 px-2 text-center font-mono text-intel-blue font-bold">
                            {a.intelCount} <span className="text-[10px] text-slate-400 font-normal">({a.rTotal > 0 ? Math.round((a.intelCount / a.rTotal) * 100) : 0}%)</span>
                          </td>
                          <td className="py-2 px-2 text-center font-mono text-rose-600 font-semibold">
                            {a.amdCount} <span className="text-[10px] text-slate-400 font-normal">({a.rTotal > 0 ? Math.round((a.amdCount / a.rTotal) * 100) : 0}%)</span>
                          </td>
                          <td className="py-2 px-2 text-center font-mono text-slate-500">
                            {a.appleCount} <span className="text-[10px] text-slate-400 font-normal">({a.rTotal > 0 ? Math.round((a.appleCount / a.rTotal) * 100) : 0}%)</span>
                          </td>
                          <td className="py-2 px-2 text-center font-mono text-purple-600">
                            {a.qualcommCount} <span className="text-[10px] text-slate-400 font-normal">({a.rTotal > 0 ? Math.round((a.qualcommCount / a.rTotal) * 100) : 0}%)</span>
                          </td>
                          <td className="py-2 px-3 text-right font-mono font-black">
                            <span className={a.sosPct >= 70 ? 'text-emerald-600' : 'text-amber-600'}>
                              {a.sosPct}% <span className="text-[10px] text-slate-400 font-normal font-sans">(N={a.rTotal})</span>
                            </span>
                          </td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 3: BY COUNTRY */}
          {subTab === 'sos-country' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Geographic Market Share of Shelf</h4>
              <p className="text-xs text-slate-500">Aggregated Intel processor shelf share by country</p>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Country</th>
                      <th className="py-2.5 px-2 text-center">Accounts Monitored</th>
                      <th className="py-2.5 px-2 text-center">Total Extracted SKUs</th>
                      <th className="py-2.5 px-2 text-center">Intel SKUs</th>
                      <th className="py-2.5 px-3 text-right">Intel SOS %</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {Array.from(new Set(accounts.map((a: any) => a.country))).filter(Boolean).map((country: any) => {
                      const cAccounts = accounts.filter((a: any) => a.country === country);
                      const cProducts = products.filter((p: any) => p.country === country);
                      const cIntel = cProducts.filter((p: any) => /intel/i.test(p.processor || '')).length;
                      const cSos = cProducts.length > 0 ? Math.round((cIntel / cProducts.length) * 100) : null;

                      return (
                        <tr key={country} className="hover:bg-slate-50/80">
                          <td className="py-2 px-3 font-bold text-slate-900">{country}</td>
                          <td className="py-2 px-2 text-center font-mono font-semibold">{cAccounts.length}</td>
                          <td className="py-2 px-2 text-center font-mono font-bold">{cProducts.length}</td>
                          <td className="py-2 px-2 text-center font-mono text-intel-blue font-bold">{cIntel}</td>
                          <td className="py-2 px-3 text-right font-mono font-black">
                            {cSos !== null ? (
                              <span className={cSos >= 70 ? 'text-emerald-600' : 'text-amber-600'}>{cSos}%</span>
                            ) : (
                              <span className="text-slate-400">N/A</span>
                            )}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 4: BY OEM */}
          {subTab === 'sos-oem' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">OEM Brand Alignment</h4>
              <p className="text-xs text-slate-500">Distribution of processor architectures per OEM manufacturer</p>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {dynamicOemRanks.map((o: any) => (
                  <div key={o.oem} className="p-4 rounded-xl bg-slate-50 border border-slate-200/80 space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-sm text-slate-900">{o.oem}</span>
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                        o.sos_pct >= 70 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                      }`}>
                        {o.sos_pct}% Intel Share
                      </span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden flex">
                      <div className="bg-intel-blue h-2" style={{ width: `${o.sos_pct}%` }}></div>
                      <div className="bg-rose-500 h-2" style={{ width: `${100 - o.sos_pct}%` }}></div>
                    </div>
                    <div className="flex items-center justify-between text-[11px] text-slate-600">
                      <span>Total: <strong>{o.total}</strong></span>
                      <span>Intel: <strong className="text-intel-blue">{o.intel}</strong></span>
                      <span>AMD/Other: <strong className="text-rose-600">{o.total - o.intel}</strong></span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* TAB 5: PRODUCT AUDIT */}
          {subTab === 'sos-product' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Active Category Products Audit</h4>
              <p className="text-xs text-slate-500">Sample of raw products harvested from first 2 listing pages</p>
              <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Title &amp; Spec</th>
                      <th className="py-2.5 px-2">Account</th>
                      <th className="py-2.5 px-2">OEM</th>
                      <th className="py-2.5 px-2">Processor</th>
                      <th className="py-2.5 px-2 text-right">Price</th>
                      <th className="py-2.5 px-3 text-right">URL</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {products.slice(0, 50).map((p: any, idx: number) => (
                      <tr
                        key={p.product_id || p.sku_index || idx}
                        onClick={() => setSelectedSkuDetail(p)}
                        className="hover:bg-slate-50/80 cursor-pointer"
                      >
                        <td className="py-2 px-3 max-w-sm truncate font-medium text-slate-900">
                          {p.product_title}
                        </td>
                        <td className="py-2 px-2 text-slate-600 font-semibold">{p.account}</td>
                        <td className="py-2 px-2 text-slate-700">{p.oem}</td>
                        <td className="py-2 px-2">
                          <span className={`px-1.5 py-0.5 rounded text-[10px] font-bold ${
                            /intel/i.test(p.processor || '') ? 'bg-intel-blue/10 text-intel-blue' : 'bg-slate-200 text-slate-700'
                          }`}>
                            {p.processor_model || p.processor}
                          </span>
                        </td>
                        <td className="py-2 px-2 text-right font-mono font-bold text-slate-900">
                          ${p.selling_price?.toLocaleString()}
                        </td>
                        <td className="py-2 px-3 text-right">
                          <a
                            href={p.product_url}
                            target="_blank"
                            rel="noreferrer"
                            onClick={(e) => e.stopPropagation()}
                            className="inline-flex items-center space-x-1 text-intel-blue hover:underline text-[11px] font-semibold"
                          >
                            <span>Link</span>
                            <ExternalLink className="w-3 h-3" />
                          </a>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 6: CATEGORY URLS */}
          {subTab === 'category-urls' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Active Category Extraction Endpoints</h4>
              <p className="text-xs text-slate-500">Listing page URLs mapped to active accounts for SOS harvesting</p>
              <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Account</th>
                      <th className="py-2.5 px-2">Country</th>
                      <th className="py-2.5 px-3">Category Endpoint URL</th>
                      <th className="py-2.5 px-3 text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {accounts.map((a: any, idx: number) => (
                      <tr key={a.account || idx} className="hover:bg-slate-50/80">
                        <td className="py-2 px-3 font-bold text-slate-900">{a.account}</td>
                        <td className="py-2 px-2 text-slate-600">{a.country}</td>
                        <td className="py-2 px-3 font-mono text-[11px] text-slate-500 max-w-md truncate">
                          {a.website || a.domain}
                        </td>
                        <td className="py-2 px-3 text-right">
                          <a
                            href={a.website || `https://${a.domain}`}
                            target="_blank"
                            rel="noreferrer"
                            className="inline-flex items-center space-x-1 text-intel-blue hover:underline text-[11px] font-semibold"
                          >
                            <span>Visit</span>
                            <ExternalLink className="w-3 h-3" />
                          </a>
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
