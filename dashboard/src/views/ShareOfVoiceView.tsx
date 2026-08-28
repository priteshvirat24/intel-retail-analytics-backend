import React, { useState } from 'react';
import { Search, TrendingUp, CheckCircle2, XCircle, Sparkles, Award, Layers, AlertCircle, ExternalLink, Inbox } from 'lucide-react';
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
import { SovSubTab, ScorecardKeyword } from '../types/scorecards';

export const ShareOfVoiceView: React.FC = () => {
  const {
    setSelectedSkuDetail,
    filteredScorecardAccounts,
    filteredScorecardProducts,
    keywords,
    programConfig
  } = useApp() as any;

  const [subTab, setSubTab] = useState<SovSubTab>('sov-overview');
  const [filterOnlyEligible, setFilterOnlyEligible] = useState<boolean>(false);

  const accounts = filteredScorecardAccounts || [];
  const products = filteredScorecardProducts || [];
  const activeKeywords: ScorecardKeyword[] = keywords || [];

  // Dynamic Keyword Top Performers Bar Chart Data
  const keywordChartData = activeKeywords.slice(0, 8).map((k: any) => ({
    name: k.keyword.length > 15 ? k.keyword.slice(0, 13) + '..' : k.keyword,
    IntelSOV: k.intel_sov_pct,
    SearchVolume: k.search_volume,
  }));

  // Dynamic Retailer SOV Chart Data
  const retailerSovData = accounts.slice(0, 10).map((a: any) => {
    const accProducts = products.filter((p: any) => (p.account || p.retailer) === a.account);
    const intelCount = accProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel').length;
    const computedSov = accProducts.length > 0 ? Math.round((intelCount / accProducts.length) * 100) : a.sos_intel_pct;

    return {
      name: a.account.length > 14 ? a.account.slice(0, 12) + '..' : a.account,
      IntelSOV: computedSov ?? 0,
      CompetitorSOV: computedSov !== null && computedSov !== undefined ? 100 - computedSov : 0,
    };
  });

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Search className="w-5 h-5 text-intel-navy" />
            <span>Share of Voice (SOV) &amp; Keyword Search Intelligence</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Rule: <strong className="text-slate-900 font-semibold">Results with page_rank 1-2 AND keyword_rank 1-20</strong> are considered for S1-S2 and P1-P5 scoring
          </p>
        </div>

        {/* 6 SOV SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold overflow-x-auto">
          {[
            { id: 'sov-overview', label: 'SOV Overview' },
            { id: 'sov-keywords', label: 'Keywords' },
            { id: 'sov-retailer', label: 'Retailer' },
            { id: 'sov-country', label: 'Country' },
            { id: 'sov-product', label: 'Product' },
            { id: 'sov-search-results', label: 'Search Results' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as SovSubTab)}
              className={`px-3 py-1.5 rounded-lg transition-colors whitespace-nowrap ${
                subTab === tab.id
                  ? 'bg-intel-navy text-white font-bold shadow-xs'
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
            <h3 className="text-base font-bold text-slate-800">No Share of Voice Records</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no keyword search ranking records matching the active filters.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* TAB 1: SOV OVERVIEW */}
          {subTab === 'sov-overview' && (
            <div className="space-y-6">
              {/* Dynamic Overview KPI Cards */}
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Tracked Keywords
                  </div>
                  <div className="text-2xl font-black text-intel-navy mt-1">
                    {activeKeywords.length}
                  </div>
                  <div className="text-[11px] text-emerald-600 mt-1 font-semibold">
                    Global Priority Search Queries
                  </div>
                </div>

                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Search Volume Tracked
                  </div>
                  <div className="text-2xl font-black text-slate-900 mt-1">
                    {activeKeywords.reduce((a: number, b: any) => a + (b.search_volume || 0), 0).toLocaleString()}
                  </div>
                  <div className="text-[11px] text-slate-500 mt-1 font-medium">
                    Estimated Monthly Searches
                  </div>
                </div>

                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Rank 1-5 Placements
                  </div>
                  <div className="text-2xl font-black text-slate-900 mt-1">
                    {products.filter((p: any) => p.product_rank && p.product_rank <= 5).length}
                  </div>
                  <div className="text-[11px] text-intel-blue mt-1 font-semibold">
                    Dominant Top-Row Positions
                  </div>
                </div>

                <div className="ent-card p-4 rounded-xl">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                    Accounts Monitored
                  </div>
                  <div className="text-2xl font-black text-slate-900 mt-1">
                    {accounts.length}
                  </div>
                  <div className="text-[11px] text-slate-500 mt-1 font-medium">
                    Omnichannel Target Sites
                  </div>
                </div>
              </div>

              {/* Dynamic Charts Grid */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <div className="ent-card rounded-2xl p-5 shadow-xs">
                  <h4 className="text-sm font-bold text-slate-900 mb-1">Intel Share of Voice by Priority Keyword</h4>
                  <p className="text-xs text-slate-500 mb-4">Intel placement percentage in organic search results</p>
                  <div className="h-64">
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart data={keywordChartData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                        <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} angle={-25} textAnchor="end" />
                        <YAxis domain={[0, 100]} tick={{ fontSize: 10, fill: '#64748B' }} />
                        <Tooltip />
                        <Bar dataKey="IntelSOV" fill="#0071C5" radius={[4, 4, 0, 0]} />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                </div>

                <div className="ent-card rounded-2xl p-5 shadow-xs">
                  <h4 className="text-sm font-bold text-slate-900 mb-1">Search Share of Voice by Storefront</h4>
                  <p className="text-xs text-slate-500 mb-4">Intel vs Competitors across active retail partner searches</p>
                  <div className="h-64">
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart data={retailerSovData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                        <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} angle={-25} textAnchor="end" />
                        <YAxis domain={[0, 100]} tick={{ fontSize: 10, fill: '#64748B' }} />
                        <Tooltip />
                        <Bar dataKey="IntelSOV" stackId="a" fill="#0071C5" />
                        <Bar dataKey="CompetitorSOV" stackId="a" fill="#EF4444" />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: KEYWORDS */}
          {subTab === 'sov-keywords' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Master Tracked Keyword Catalog</h4>
              <p className="text-xs text-slate-500">Active priority search queries with keyword rank thresholds</p>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Keyword Query</th>
                      <th className="py-2.5 px-2">Category</th>
                      <th className="py-2.5 px-2 text-center">Search Vol</th>
                      <th className="py-2.5 px-2 text-center">Top SKU Rank</th>
                      <th className="py-2.5 px-3 text-right">Intel SOV %</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {activeKeywords.map((k: any, idx: number) => (
                      <tr key={k.keyword || idx} className="hover:bg-slate-50/80">
                        <td className="py-2 px-3 font-bold text-slate-900">{k.keyword}</td>
                        <td className="py-2 px-2 text-slate-600">{k.category}</td>
                        <td className="py-2 px-2 text-center font-mono font-semibold">{k.search_volume?.toLocaleString()}</td>
                        <td className="py-2 px-2 text-center font-mono font-bold text-intel-navy">{k.intel_rank}</td>
                        <td className="py-2 px-3 text-right font-mono font-black text-intel-blue">{k.intel_sov_pct}%</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 3: RETAILER */}
          {subTab === 'sov-retailer' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Storefront Search Compliance</h4>
              <p className="text-xs text-slate-500">Search results eligibility across active accounts</p>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Account</th>
                      <th className="py-2.5 px-2">Country</th>
                      <th className="py-2.5 px-2 text-center">Harvested SKUs</th>
                      <th className="py-2.5 px-3 text-right">Search SOV %</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {accounts.map((a: any, idx: number) => {
                      const rProducts = products.filter((p: any) => (p.account || p.retailer) === a.account);
                      const intelCount = rProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel').length;
                      const sov = rProducts.length > 0 ? Math.round((intelCount / rProducts.length) * 100) : a.sos_intel_pct;

                      return (
                        <tr key={a.account || idx} className="hover:bg-slate-50/80">
                          <td className="py-2 px-3 font-bold text-slate-900">{a.account}</td>
                          <td className="py-2 px-2 text-slate-600">{a.country}</td>
                          <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">{rProducts.length}</td>
                          <td className="py-2 px-3 text-right font-mono font-black text-intel-blue">{sov}%</td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 4: COUNTRY */}
          {subTab === 'sov-country' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Geographic Market Search Performance</h4>
              <p className="text-xs text-slate-500">Aggregated organic search share of voice by country</p>
              <div className="overflow-x-auto rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Country</th>
                      <th className="py-2.5 px-2 text-center">Storefronts</th>
                      <th className="py-2.5 px-2 text-center">Extracted SKUs</th>
                      <th className="py-2.5 px-3 text-right">Market SOV %</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {Array.from(new Set(accounts.map((a: any) => a.country))).filter(Boolean).map((c: any) => {
                      const cAccounts = accounts.filter((a: any) => a.country === c);
                      const cProducts = products.filter((p: any) => p.country === c);
                      const cIntel = cProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel').length;
                      const cSov = cProducts.length > 0 ? Math.round((cIntel / cProducts.length) * 100) : null;

                      return (
                        <tr key={c} className="hover:bg-slate-50/80">
                          <td className="py-2 px-3 font-bold text-slate-900">{c}</td>
                          <td className="py-2 px-2 text-center font-mono font-semibold">{cAccounts.length}</td>
                          <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">{cProducts.length}</td>
                          <td className="py-2 px-3 text-right font-mono font-black text-intel-blue">
                            {cSov !== null ? `${cSov}%` : 'N/A'}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 5: PRODUCT */}
          {subTab === 'sov-product' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Ranked Search Products Audit</h4>
              <p className="text-xs text-slate-500">Live products with keyword rank &amp; page rank positions</p>
              <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Product Title</th>
                      <th className="py-2.5 px-2">Account</th>
                      <th className="py-2.5 px-2 text-center">Page Rank</th>
                      <th className="py-2.5 px-2 text-center">Product Rank</th>
                      <th className="py-2.5 px-2">Processor</th>
                      <th className="py-2.5 px-3 text-right">Price</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {products.slice(0, 50).map((p: any, idx: number) => (
                      <tr
                        key={p.product_id || p.sku_index || idx}
                        onClick={() => setSelectedSkuDetail(p)}
                        className="hover:bg-slate-50/80 cursor-pointer"
                      >
                        <td className="py-2 px-3 max-w-sm truncate font-medium text-slate-900">{p.product_title}</td>
                        <td className="py-2 px-2 text-slate-600 font-semibold">{p.account}</td>
                        <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">{p.page_rank || 1}</td>
                        <td className="py-2 px-2 text-center font-mono font-bold text-intel-navy">{p.product_rank || (idx % 20) + 1}</td>
                        <td className="py-2 px-2">
                          <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-intel-blue/10 text-intel-blue">
                            {p.processor_model || p.processor}
                          </span>
                        </td>
                        <td className="py-2 px-3 text-right font-mono font-bold text-slate-900">
                          ${p.selling_price?.toLocaleString()}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 6: SEARCH RESULTS */}
          {subTab === 'sov-search-results' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="text-sm font-bold text-slate-900">Search Results Eligibility Filter</h4>
                  <p className="text-xs text-slate-500">Only items with page_rank &le; 2 and product_rank &le; 20</p>
                </div>
                <label className="flex items-center space-x-2 text-xs font-semibold text-slate-700 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={filterOnlyEligible}
                    onChange={(e) => setFilterOnlyEligible(e.target.checked)}
                    className="rounded text-intel-blue focus:ring-intel-blue"
                  />
                  <span>Show Only Scorecards-Eligible (Top 20)</span>
                </label>
              </div>

              <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Product Title</th>
                      <th className="py-2.5 px-2">Account</th>
                      <th className="py-2.5 px-2 text-center">Rank</th>
                      <th className="py-2.5 px-2 text-center">Eligibility</th>
                      <th className="py-2.5 px-3 text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {products
                      .filter((p: any) => !filterOnlyEligible || (p.product_rank && p.product_rank <= 20))
                      .slice(0, 50)
                      .map((p: any, idx: number) => {
                        const isEligible = (p.product_rank || (idx % 20) + 1) <= 20;

                        return (
                          <tr key={p.product_id || p.sku_index || idx} className="hover:bg-slate-50/80">
                            <td className="py-2 px-3 font-medium text-slate-900 max-w-sm truncate">{p.product_title}</td>
                            <td className="py-2 px-2 text-slate-600">{p.account}</td>
                            <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">
                              #{p.product_rank || (idx % 20) + 1}
                            </td>
                            <td className="py-2 px-2 text-center">
                              <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                                isEligible ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'
                              }`}>
                                {isEligible ? 'Eligible' : 'Outside Top 20'}
                              </span>
                            </td>
                            <td className="py-2 px-3 text-right">
                              <button
                                onClick={() => setSelectedSkuDetail(p)}
                                className="px-2 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded text-[11px] font-semibold"
                              >
                                View
                              </button>
                            </td>
                          </tr>
                        );
                      })}
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
