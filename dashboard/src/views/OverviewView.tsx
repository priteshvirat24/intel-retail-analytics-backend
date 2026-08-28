import React, { useState } from 'react';
import {
  Layers,
  Search,
  Award,
  ShieldCheck,
  TrendingUp,
  Cpu,
  DollarSign,
  Laptop,
  CheckCircle2,
  AlertCircle,
  ExternalLink,
  Calendar,
  Sparkles,
  ArrowRight,
  Globe,
  Store,
  Inbox
} from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Legend
} from 'recharts';
import { useApp } from '../context/AppContext';
import { PROGRAM_HISTORY_METRICS } from '../data/scorecardsData';

export const OverviewView: React.FC = () => {
  const {
    setActiveTab,
    costMetrics,
    filteredScorecardAccounts,
    filteredScorecardProducts,
    overviewKpis,
    sosDistribution,
    oemDistribution,
    programConfig
  } = useApp() as any;

  const [accountSearch, setAccountSearch] = useState<string>('');

  const accounts = filteredScorecardAccounts || [];
  const products = filteredScorecardProducts || [];

  const filteredAccounts = accounts.filter((a: any) => {
    if (!accountSearch) return true;
    const term = accountSearch.toLowerCase();
    return (
      (a.account && a.account.toLowerCase().includes(term)) ||
      (a.country && a.country.toLowerCase().includes(term)) ||
      (a.account_type && a.account_type.toLowerCase().includes(term))
    );
  });

  const topKpis = [
    {
      label: 'Accounts Monitored',
      value: overviewKpis.totalAccounts > 0 ? `${overviewKpis.totalAccounts} Accounts` : '0 Accounts',
      sub: `${overviewKpis.totalCountries} Countries Filtered`,
      icon: Store,
      color: 'text-intel-navy',
      bg: 'bg-blue-50'
    },
    {
      label: 'Verified Global SKUs',
      value: overviewKpis.totalSkus > 0 ? `${overviewKpis.totalSkus.toLocaleString()} SKUs` : '0 SKUs',
      sub: overviewKpis.totalAccounts > 0 ? `Avg ~${Math.round((overviewKpis.totalSkus / overviewKpis.totalAccounts) * 10) / 10} / site` : 'No data',
      icon: Laptop,
      color: 'text-slate-800',
      bg: 'bg-slate-50'
    },
    {
      label: 'Global Intel SOS %',
      value: overviewKpis.intelSosPct !== null ? `${overviewKpis.intelSosPct}%` : 'N/A',
      sub: `${overviewKpis.intelSkus.toLocaleString()} Intel of ${overviewKpis.totalSkus.toLocaleString()} SKUs`,
      icon: Layers,
      color: 'text-intel-blue',
      bg: 'bg-blue-50'
    },
    {
      label: 'Average Intel SOV %',
      value: overviewKpis.averageIntelSovPct !== null ? `${overviewKpis.averageIntelSovPct}%` : 'N/A',
      sub: 'Across Priority Keywords',
      icon: Search,
      color: 'text-purple-600',
      bg: 'bg-purple-50'
    },
    {
      label: 'Average Overall Score',
      value: overviewKpis.avgOverallScore !== null ? `${overviewKpis.avgOverallScore} / 100` : 'N/A',
      sub: `Listing S: ${overviewKpis.avgListingScore ?? 'N/A'} | Details P: ${overviewKpis.avgPdpScore ?? 'N/A'}`,
      icon: Award,
      color: 'text-emerald-600',
      bg: 'bg-emerald-50'
    },
    {
      label: 'Average Listing Score',
      value: overviewKpis.avgListingScore !== null ? `${overviewKpis.avgListingScore} / 100` : 'N/A',
      sub: 'S1 Title & S2 Badge Audit',
      icon: ShieldCheck,
      color: 'text-intel-navy',
      bg: 'bg-blue-50'
    },
    {
      label: 'Average PDP Score',
      value: overviewKpis.avgPdpScore !== null ? `${overviewKpis.avgPdpScore} / 100` : 'N/A',
      sub: 'P1-P5 Content Quality',
      icon: Sparkles,
      color: 'text-purple-700',
      bg: 'bg-purple-50'
    },
    {
      label: 'Intel EVO Badged SKUs',
      value: `${overviewKpis.evoCount} SKUs`,
      sub: 'Certified Evo Edition Adoption',
      icon: Award,
      color: 'text-purple-600',
      bg: 'bg-purple-50'
    },
    {
      label: 'Geographic Markets',
      value: `${overviewKpis.totalCountries} Countries`,
      sub: 'Americas, EMEA, APAC',
      icon: Globe,
      color: 'text-emerald-700',
      bg: 'bg-emerald-50'
    },
    {
      label: 'Avg Selling Price',
      value: overviewKpis.avgSellingPriceUsd !== null ? `$${overviewKpis.avgSellingPriceUsd.toLocaleString()}` : 'N/A',
      sub: 'Normalized USD Market Rate',
      icon: DollarSign,
      color: 'text-emerald-700',
      bg: 'bg-emerald-50'
    },
    {
      label: 'Cache Hit Rate',
      value: `${costMetrics.cache_hit_rate_pct}%`,
      sub: `${costMetrics.cached_requests} Requests Cached`,
      icon: CheckCircle2,
      color: 'text-emerald-600',
      bg: 'bg-emerald-50'
    },
  ];

  // Dynamic Top Accounts for Chart from actual accounts & products
  const topAccountsChart = accounts.slice(0, 10).map((a: any) => {
    const accProducts = products.filter((p: any) => (p.account || p.retailer) === a.account);
    const intelCount = accProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel').length;
    const compCount = accProducts.length - intelCount;

    return {
      name: a.account.length > 14 ? a.account.slice(0, 12) + '..' : a.account,
      Intel: accProducts.length > 0 ? intelCount : (a.intel_skus_count || 0),
      Competitor: accProducts.length > 0 ? compCount : (a.competitor_skus_count || 0),
    };
  });

  // Dynamic Share of Shelf Pie Data from actual products
  const pieData = sosDistribution && sosDistribution.length > 0
    ? sosDistribution.map((item: any) => ({
        name: `${item.name} (${item.percentage}%)`,
        value: item.count,
        color: item.color || '#0071C5',
      }))
    : [];

  const p2024 = PROGRAM_HISTORY_METRICS['2024'];
  const p2025 = PROGRAM_HISTORY_METRICS['2025'];

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* 1. Scorecards Program Purpose Banner */}
      <div className="p-5 bg-gradient-to-r from-slate-900 via-intel-navy to-slate-900 rounded-2xl text-white shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div className="space-y-1 max-w-3xl">
          <div className="flex items-center space-x-2">
            <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-intel-cyan text-slate-950 uppercase font-mono">
              {programConfig.program_name} ({programConfig.version})
            </span>
            <span className="text-[11px] text-slate-300 font-mono">
              Scope: <strong className="text-white">{overviewKpis.totalAccounts} Accounts &bull; {overviewKpis.totalCountries} Countries</strong>
            </span>
          </div>
          <h2 className="text-lg font-bold tracking-tight text-white">
            Intel Online Tracking &amp; Retail Execution Intelligence Platform
          </h2>
          <p className="text-xs text-slate-300 leading-relaxed">
            Dynamic omnichannel intelligence engine measuring Intel presence, Share of Shelf (SOS), Share of Voice (SOV), pricing corridors, and S1..P5 digital compliance across all active retail partners.
          </p>
        </div>

        <div className="flex items-center space-x-2 shrink-0">
          <button
            onClick={() => setActiveTab('scorecards')}
            className="px-4 py-2 rounded-xl bg-white text-intel-navy hover:bg-slate-100 font-bold text-xs shadow-sm transition-colors flex items-center gap-1.5"
          >
            <span>View All Scorecards</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* 2. Top KPIs Strip */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center space-x-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700">
              Active Benchmark Intelligence Metrics
            </h3>
          </div>
          <span className="text-[11px] text-slate-400 font-mono">
            {overviewKpis.totalSkus > 0 ? `${overviewKpis.totalSkus.toLocaleString()} Real Records Computed` : 'No data in active filter'}
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-3">
          {topKpis.map((kpi, idx) => {
            const Icon = kpi.icon;
            return (
              <div key={idx} className="ent-card p-3.5 rounded-xl flex flex-col justify-between space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-tight line-clamp-1">
                    {kpi.label}
                  </span>
                  <div className={`p-1.5 rounded-lg ${kpi.bg}`}>
                    <Icon className={`w-3.5 h-3.5 ${kpi.color}`} />
                  </div>
                </div>
                <div>
                  <div className="text-lg font-black text-slate-900 tracking-tight">{kpi.value}</div>
                  <div className="text-[10px] text-slate-500 font-medium truncate">{kpi.sub}</div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* ZERO DATA EMPTY STATE */}
      {overviewKpis.totalSkus === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No SKU Data Available</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no product records matching your current filter selection or loaded in the active universe. Adjust filters or run a live ingestion job.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* 3. Analytics Visualizations Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Share of Shelf Distribution by Processor Family */}
            <div className="ent-card rounded-2xl p-5 shadow-xs">
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h4 className="text-sm font-bold text-slate-900">Share of Shelf (SOS) Breakdown</h4>
                  <p className="text-xs text-slate-500">Processor share derived from {products.length.toLocaleString()} active SKU records</p>
                </div>
                <span className="text-[10px] px-2 py-0.5 rounded-full font-mono font-bold bg-intel-navy text-white">
                  {overviewKpis.intelSosPct !== null ? `${overviewKpis.intelSosPct}% Intel` : 'N/A'}
                </span>
              </div>

              {pieData.length > 0 ? (
                <div className="h-64">
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={pieData}
                        cx="50%"
                        cy="50%"
                        innerRadius={60}
                        outerRadius={90}
                        paddingAngle={3}
                        dataKey="value"
                      >
                        {pieData.map((entry, index) => (
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
                  No SOS records available
                </div>
              )}
            </div>

            {/* Top 10 Accounts Competitor Comparison Bar Chart */}
            <div className="lg:col-span-2 ent-card rounded-2xl p-5 shadow-xs">
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h4 className="text-sm font-bold text-slate-900">Intel vs Competitor Shelf Volume by Account</h4>
                  <p className="text-xs text-slate-500">Live SKU volume comparison across top active retail targets</p>
                </div>
                <div className="flex items-center space-x-3 text-xs font-semibold">
                  <div className="flex items-center space-x-1.5">
                    <span className="w-3 h-3 rounded-sm bg-intel-blue"></span>
                    <span className="text-slate-600">Intel</span>
                  </div>
                  <div className="flex items-center space-x-1.5">
                    <span className="w-3 h-3 rounded-sm bg-rose-500"></span>
                    <span className="text-slate-600">Competitors</span>
                  </div>
                </div>
              </div>

              {topAccountsChart.length > 0 ? (
                <div className="h-64">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={topAccountsChart} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                      <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} angle={-25} textAnchor="end" />
                      <YAxis tick={{ fontSize: 10, fill: '#64748B' }} />
                      <Tooltip />
                      <Bar dataKey="Intel" fill="#0071C5" radius={[4, 4, 0, 0]} />
                      <Bar dataKey="Competitor" fill="#EF4444" radius={[4, 4, 0, 0]} />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              ) : (
                <div className="h-64 flex items-center justify-center text-xs text-slate-400">
                  No account volume data available
                </div>
              )}
            </div>
          </div>

          {/* 4. Filterable Accounts Performance Matrix Table */}
          <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
              <div>
                <h4 className="text-sm font-bold text-slate-900">
                  Active Account Intelligence Performance Matrix
                </h4>
                <p className="text-xs text-slate-500">
                  Showing {filteredAccounts.length} evaluated accounts &bull; S1 (Listing) &amp; P1–P5 (Product Page) execution scores
                </p>
              </div>

              <div className="flex items-center space-x-2">
                <div className="relative">
                  <Search className="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" />
                  <input
                    type="text"
                    placeholder="Search account..."
                    value={accountSearch}
                    onChange={(e) => setAccountSearch(e.target.value)}
                    className="pl-8 pr-3 py-1.5 rounded-lg border border-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-intel-blue w-48"
                  />
                </div>
              </div>
            </div>

            <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-50 text-slate-500 font-bold sticky top-0 uppercase tracking-wider text-[10px] border-b border-slate-200">
                  <tr>
                    <th className="py-2.5 px-3">Account &amp; Domain</th>
                    <th className="py-2.5 px-2">Country</th>
                    <th className="py-2.5 px-2">Type</th>
                    <th className="py-2.5 px-2 text-center">SKUs</th>
                    <th className="py-2.5 px-2 text-center">Intel SOS</th>
                    <th className="py-2.5 px-2 text-center">Listing S</th>
                    <th className="py-2.5 px-2 text-center">Details P</th>
                    <th className="py-2.5 px-2 text-center">Overall</th>
                    <th className="py-2.5 px-3 text-right">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {filteredAccounts.map((a: any, idx: number) => {
                    const accProducts = products.filter((p: any) => (p.account || p.retailer) === a.account);
                    const accIntel = accProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel').length;
                    const accSos = accProducts.length > 0 ? Math.round((accIntel / accProducts.length) * 100) : a.sos_intel_pct;

                    return (
                      <tr key={a.account || idx} className="hover:bg-slate-50/80 transition-colors">
                        <td className="py-2.5 px-3">
                          <div className="font-bold text-slate-900">{a.account}</div>
                          <div className="text-[10px] text-slate-400 font-mono truncate max-w-xs">{a.website || a.domain}</div>
                        </td>
                        <td className="py-2.5 px-2 font-medium text-slate-700">{a.country}</td>
                        <td className="py-2.5 px-2">
                          <span className="px-1.5 py-0.5 rounded text-[10px] font-semibold bg-slate-100 text-slate-600">
                            {a.account_type || a.type}
                          </span>
                        </td>
                        <td className="py-2.5 px-2 text-center font-mono font-bold text-slate-900">
                          {accProducts.length > 0 ? accProducts.length : (a.products_count || 0)}
                        </td>
                        <td className="py-2.5 px-2 text-center font-mono font-bold text-intel-blue">
                          {accSos ? `${accSos}%` : 'N/A'}
                        </td>
                        <td className="py-2.5 px-2 text-center font-mono font-semibold text-slate-700">
                          {a.listing_s_score ?? 'N/A'}
                        </td>
                        <td className="py-2.5 px-2 text-center font-mono font-semibold text-slate-700">
                          {a.details_p_score ?? 'N/A'}
                        </td>
                        <td className="py-2.5 px-2 text-center">
                          <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                            (a.Overall_score || 0) >= 85
                              ? 'bg-emerald-100 text-emerald-800'
                              : (a.Overall_score || 0) >= 70
                              ? 'bg-amber-100 text-amber-800'
                              : 'bg-rose-100 text-rose-800'
                          }`}>
                            {a.Overall_score ?? 'N/A'}
                          </span>
                        </td>
                        <td className="py-2.5 px-3 text-right">
                          <button
                            onClick={() => setActiveTab('scorecards')}
                            className="px-2 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-semibold transition-colors"
                          >
                            Scorecard
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </>
      )}
    </div>
  );
};
