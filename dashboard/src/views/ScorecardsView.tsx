import React, { useState } from 'react';
import {
  ShieldCheck,
  CheckCircle2,
  XCircle,
  ExternalLink,
  Award,
  DollarSign,
  Layers,
  Search,
  Sparkles,
  ArrowUpDown,
  Laptop,
  TrendingUp,
  BarChart2,
  ChevronRight,
  Eye,
  Camera,
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
  Legend
} from 'recharts';
import { useApp } from '../context/AppContext';
import { ScorecardsSubTab, ScorecardAccount, ScorecardSKU } from '../types/scorecards';
import { EvidenceService } from '../services/evidenceService';
import { EvidenceRecord } from '../types/evidence';
import { EvidenceDrawer } from '../components/Modals/EvidenceDrawer';

export const ScorecardsView: React.FC = () => {
  const {
    setSelectedSkuDetail,
    setSourceEvidenceTarget,
    filteredScorecardAccounts,
    filteredScorecardProducts,
    scorecardMetrics,
    programConfig
  } = useApp() as any;

  const [subTab, setSubTab] = useState<ScorecardsSubTab>('account-scorecards');
  const [selectedAccount, setSelectedAccount] = useState<string | null>(null);
  const [activeEvidence, setActiveEvidence] = useState<EvidenceRecord | null>(null);

  const displayAccounts = filteredScorecardAccounts || [];
  const displayProducts = filteredScorecardProducts || [];

  // Dynamic Score Distribution Bucketing from actual evaluated accounts
  const distributionData = [
    {
      range: '90-100 (Exceptional)',
      count: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 90).length,
      label: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 90).map((a: any) => a.account).slice(0, 3).join(', ') || 'None',
    },
    {
      range: '80-89 (Strong)',
      count: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 80 && (a.Overall_score || 0) < 90).length,
      label: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 80 && (a.Overall_score || 0) < 90).map((a: any) => a.account).slice(0, 3).join(', ') || 'None',
    },
    {
      range: '70-79 (Moderate)',
      count: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 70 && (a.Overall_score || 0) < 80).length,
      label: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 70 && (a.Overall_score || 0) < 80).map((a: any) => a.account).slice(0, 3).join(', ') || 'None',
    },
    {
      range: '60-69 (Needs Work)',
      count: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 60 && (a.Overall_score || 0) < 70).length,
      label: displayAccounts.filter((a: any) => (a.Overall_score || 0) >= 60 && (a.Overall_score || 0) < 70).map((a: any) => a.account).slice(0, 3).join(', ') || 'None',
    },
    {
      range: '0-59 (Non-Compliant)',
      count: displayAccounts.filter((a: any) => (a.Overall_score || 0) < 60).length,
      label: displayAccounts.filter((a: any) => (a.Overall_score || 0) < 60).map((a: any) => a.account).slice(0, 3).join(', ') || 'None',
    },
  ];

  // Dynamic Component Breakdown Bar Chart
  const componentScoreData = [
    { name: 'S1 Title', score: scorecardMetrics.avgS1 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.s1 * 100)}%` },
    { name: 'S2 Badges', score: scorecardMetrics.avgS2 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.s2 * 100)}%` },
    { name: 'P1 Specs', score: scorecardMetrics.avgP1 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.p1 * 100)}%` },
    { name: 'P2 Benefits', score: scorecardMetrics.avgP2 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.p2 * 100)}%` },
    { name: 'P3 Media', score: scorecardMetrics.avgP3 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.p3 * 100)}%` },
    { name: 'P4 Accuracy', score: scorecardMetrics.avgP4 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.p4 * 100)}%` },
    { name: 'P5 Metadata', score: scorecardMetrics.avgP5 ?? 0, weight: `${Math.round(programConfig.scorecard_weights.p5 * 100)}%` },
  ];

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-intel-navy" />
            <span>Intel Retail Execution Scorecards</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Holistic brand compliance and digital shelf execution scores across S1, S2, and P1–P5 audit dimensions
          </p>
        </div>

        {/* 4 Scorecards SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'account-scorecards', label: 'Account Scorecards' },
            { id: 'product-scorecards', label: 'Product Scorecards' },
            { id: 'score-distribution', label: 'Score Distribution' },
            { id: 'score-trends', label: 'Component Breakdown' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as ScorecardsSubTab)}
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
      {displayAccounts.length === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No Account Scorecards Available</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no evaluated accounts matching the active filters.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* TAB 1: ACCOUNT SCORECARDS */}
          {subTab === 'account-scorecards' && (
            <div className="space-y-6">
              {/* Dynamic Overall Summary Cards */}
              <div className="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-6 gap-3">
                <div className="ent-card p-3 rounded-xl">
                  <div className="text-[10px] font-bold text-slate-400 uppercase font-mono">Overall Average</div>
                  <div className="text-xl font-black text-slate-900 mt-1">
                    {scorecardMetrics.avgOverall !== null ? `${scorecardMetrics.avgOverall} / 100` : 'N/A'}
                  </div>
                  <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">
                    {displayAccounts.length} Accounts
                  </div>
                </div>

                <div className="ent-card p-3 rounded-xl">
                  <div className="text-[10px] font-bold text-slate-400 uppercase font-mono">Listing (S) Avg</div>
                  <div className="text-xl font-black text-intel-navy mt-1">
                    {scorecardMetrics.avgListingS !== null ? `${scorecardMetrics.avgListingS} / 100` : 'N/A'}
                  </div>
                  <div className="text-[10px] text-slate-500 mt-0.5">S1 Title + S2 Badge</div>
                </div>

                <div className="ent-card p-3 rounded-xl">
                  <div className="text-[10px] font-bold text-slate-400 uppercase font-mono">Details (P) Avg</div>
                  <div className="text-xl font-black text-purple-700 mt-1">
                    {scorecardMetrics.avgDetailsP !== null ? `${scorecardMetrics.avgDetailsP} / 100` : 'N/A'}
                  </div>
                  <div className="text-[10px] text-slate-500 mt-0.5">P1–P5 PDP Content</div>
                </div>

                <div className="ent-card p-3 rounded-xl">
                  <div className="text-[10px] font-bold text-slate-400 uppercase font-mono">S1 (Title) Avg</div>
                  <div className="text-xl font-black text-slate-800 mt-1">
                    {scorecardMetrics.avgS1 !== null ? `${scorecardMetrics.avgS1} / 100` : 'N/A'}
                  </div>
                  <div className="text-[10px] text-slate-500 mt-0.5">10% Weight</div>
                </div>

                <div className="ent-card p-3 rounded-xl">
                  <div className="text-[10px] font-bold text-slate-400 uppercase font-mono">S2 (Badge) Avg</div>
                  <div className="text-xl font-black text-slate-800 mt-1">
                    {scorecardMetrics.avgS2 !== null ? `${scorecardMetrics.avgS2} / 100` : 'N/A'}
                  </div>
                  <div className="text-[10px] text-slate-500 mt-0.5">10% Weight</div>
                </div>

                <div className="ent-card p-3 rounded-xl">
                  <div className="text-[10px] font-bold text-slate-400 uppercase font-mono">P3 (Media) Avg</div>
                  <div className="text-xl font-black text-slate-800 mt-1">
                    {scorecardMetrics.avgP3 !== null ? `${scorecardMetrics.avgP3} / 100` : 'N/A'}
                  </div>
                  <div className="text-[10px] text-slate-500 mt-0.5">20% Weight</div>
                </div>
              </div>

              {/* Master Accounts Scorecard Table */}
              <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
                <div className="flex items-center justify-between">
                  <div>
                    <h4 className="text-sm font-bold text-slate-900">Partner Account Compliance Matrix</h4>
                    <p className="text-xs text-slate-500">Comprehensive breakdown of 52 global retail partners</p>
                  </div>
                </div>

                <div className="overflow-x-auto max-h-[500px] rounded-xl border border-slate-100">
                  <table className="w-full text-left text-xs">
                    <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px] border-b border-slate-200">
                      <tr>
                        <th className="py-2.5 px-3">Account &amp; Domain</th>
                        <th className="py-2.5 px-2">Country</th>
                        <th className="py-2.5 px-2 text-center">Type</th>
                        <th className="py-2.5 px-2 text-center">SKUs</th>
                        <th className="py-2.5 px-2 text-center">Listing S</th>
                        <th className="py-2.5 px-2 text-center">Details P</th>
                        <th className="py-2.5 px-2 text-center">S1</th>
                        <th className="py-2.5 px-2 text-center">S2</th>
                        <th className="py-2.5 px-2 text-center">P1</th>
                        <th className="py-2.5 px-2 text-center">P2</th>
                        <th className="py-2.5 px-2 text-center">P3</th>
                        <th className="py-2.5 px-2 text-center">P4</th>
                        <th className="py-2.5 px-2 text-center">P5</th>
                        <th className="py-2.5 px-2 text-center font-black">Overall</th>
                        <th className="py-2.5 px-3 text-right">Inspect</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {displayAccounts.map((a: any, idx: number) => {
                        const accProducts = displayProducts.filter((p: any) => (p.account || p.retailer) === a.account);
                        const isExemplary = (a.Overall_score || 0) >= 85;
                        const isCompliant = (a.Overall_score || 0) >= 70 && (a.Overall_score || 0) < 85;

                        return (
                          <tr key={a.account || idx} className="hover:bg-slate-50/80 transition-colors">
                            <td className="py-2 px-3">
                              <div className="font-bold text-slate-900">{a.account}</div>
                              <div className="text-[10px] text-slate-400 font-mono">{a.website || a.domain}</div>
                            </td>
                            <td className="py-2 px-2 text-slate-700">{a.country}</td>
                            <td className="py-2 px-2 text-center">
                              <span className="px-1.5 py-0.5 rounded text-[10px] font-semibold bg-slate-100 text-slate-600">
                                {a.account_type || a.type}
                              </span>
                            </td>
                            <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">
                              {accProducts.length > 0 ? accProducts.length : (a.products_count || 0)}
                            </td>
                            <td className="py-2 px-2 text-center font-mono font-bold text-intel-navy">
                              {a.listing_s_score ?? 'N/A'}
                            </td>
                            <td className="py-2 px-2 text-center font-mono font-bold text-purple-700">
                              {a.details_p_score ?? 'N/A'}
                            </td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.s1_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.s2_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.p1_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.p2_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.p3_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.p4_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center font-mono text-slate-600">{a.p5_score ?? 'N/A'}</td>
                            <td className="py-2 px-2 text-center">
                              <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                                isExemplary
                                  ? 'bg-emerald-100 text-emerald-800'
                                  : isCompliant
                                  ? 'bg-amber-100 text-amber-800'
                                  : 'bg-rose-100 text-rose-800'
                              }`}>
                                {a.Overall_score ?? 'N/A'}
                              </span>
                            </td>
                            <td className="py-2 px-3 text-right">
                              <button
                                onClick={() => {
                                  setSelectedAccount(a.account);
                                  setSubTab('product-scorecards');
                                }}
                                className="px-2 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded text-[11px] font-semibold"
                              >
                                SKUs
                              </button>
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: PRODUCT SCORECARDS */}
          {subTab === 'product-scorecards' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                <div>
                  <h4 className="text-sm font-bold text-slate-900">
                    Product-Level Scorecard Details {selectedAccount ? `for ${selectedAccount}` : ''}
                  </h4>
                  <p className="text-xs text-slate-500">Individual SKU compliance marks across S1, S2, and P1..P5</p>
                </div>
                {selectedAccount && (
                  <button
                    onClick={() => setSelectedAccount(null)}
                    className="text-xs text-intel-blue hover:underline font-semibold"
                  >
                    Clear Account Filter
                  </button>
                )}
              </div>

              <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Product Title</th>
                      <th className="py-2.5 px-2">Account</th>
                      <th className="py-2.5 px-2">OEM</th>
                      <th className="py-2.5 px-2">Processor</th>
                      <th className="py-2.5 px-2 text-center">S1</th>
                      <th className="py-2.5 px-2 text-center">S2</th>
                      <th className="py-2.5 px-2 text-center">P1</th>
                      <th className="py-2.5 px-2 text-center">P2</th>
                      <th className="py-2.5 px-2 text-center">P3</th>
                      <th className="py-2.5 px-2 text-center">P4</th>
                      <th className="py-2.5 px-2 text-center">P5</th>
                      <th className="py-2.5 px-2 text-center font-bold">Overall</th>
                      <th className="py-2.5 px-3 text-right">Evidence</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {displayProducts
                      .filter((p: any) => !selectedAccount || (p.account || p.retailer) === selectedAccount)
                      .slice(0, 60)
                      .map((p: any, idx: number) => (
                        <tr
                          key={p.product_id || p.sku_index || idx}
                          onClick={() => setSelectedSkuDetail(p)}
                          className="hover:bg-slate-50/80 cursor-pointer"
                        >
                          <td className="py-2 px-3 font-medium text-slate-900 max-w-sm truncate">{p.product_title}</td>
                          <td className="py-2 px-2 text-slate-600 font-semibold">{p.account}</td>
                          <td className="py-2 px-2 text-slate-700">{p.oem}</td>
                          <td className="py-2 px-2">
                            <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-intel-blue/10 text-intel-blue">
                              {p.processor_model || p.processor}
                            </span>
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'S1', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect S1 Evidence"
                          >
                            {p.s1 !== undefined && p.s1 !== null ? p.s1 : 'N/A'}
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'S2', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect S2 Evidence"
                          >
                            {p.s2 !== undefined && p.s2 !== null ? p.s2 : 'N/A'}
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'P1', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect P1 Evidence"
                          >
                            {p.p1 !== undefined && p.p1 !== null ? p.p1 : 'N/A'}
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'P2', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect P2 Evidence"
                          >
                            {p.p2 !== undefined && p.p2 !== null ? p.p2 : 'N/A'}
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'P3', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect P3 Evidence"
                          >
                            {p.p3 !== undefined && p.p3 !== null ? p.p3 : 'N/A'}
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'P4', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect P4 Evidence"
                          >
                            {p.p4 !== undefined && p.p4 !== null ? p.p4 : 'N/A'}
                          </td>
                          <td
                            onClick={(e) => {
                              e.stopPropagation();
                              const ev = EvidenceService.getEvidenceByScore(p, 'P5', displayProducts);
                              setActiveEvidence(ev);
                            }}
                            className="py-2 px-2 text-center font-mono text-slate-700 hover:bg-slate-200 hover:text-intel-navy font-bold rounded cursor-pointer transition-colors"
                            title="Inspect P5 Evidence"
                          >
                            {p.p5 !== undefined && p.p5 !== null ? p.p5 : 'N/A'}
                          </td>
                          <td className="py-2 px-2 text-center font-mono font-bold text-slate-900">
                            <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                              (p.Overall || 0) >= 80 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                            }`}>
                              {p.Overall ?? 'N/A'}/100
                            </span>
                          </td>
                          <td className="py-2 px-3 text-right">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                const ev = EvidenceService.getProductEvidenceMap(p).components.s1;
                                setActiveEvidence(ev);
                              }}
                              className="p-1 rounded hover:bg-slate-200 text-slate-500"
                              title="Inspect Full Evidence"
                            >
                              <Camera className="w-3.5 h-3.5" />
                            </button>
                          </td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 3: SCORE DISTRIBUTION */}
          {subTab === 'score-distribution' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-6">
              <div>
                <h4 className="text-sm font-bold text-slate-900">Partner Score Tier Distribution</h4>
                <p className="text-xs text-slate-500">Distribution of evaluated accounts across compliance tiers</p>
              </div>

              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={distributionData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                    <XAxis dataKey="range" tick={{ fontSize: 10, fill: '#64748B' }} />
                    <YAxis tick={{ fontSize: 10, fill: '#64748B' }} />
                    <Tooltip />
                    <Bar dataKey="count" fill="#0071C5" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-5 gap-3">
                {distributionData.map((d: any) => (
                  <div key={d.range} className="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 space-y-1">
                    <div className="text-xs font-bold text-slate-700">{d.range}</div>
                    <div className="text-2xl font-black text-intel-navy">{d.count}</div>
                    <div className="text-[10px] text-slate-500 truncate">{d.label}</div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* TAB 4: COMPONENT BREAKDOWN */}
          {subTab === 'score-trends' && (
            <div className="ent-card rounded-2xl p-5 shadow-xs space-y-6">
              <div>
                <h4 className="text-sm font-bold text-slate-900">Scorecard Audit Component Averages</h4>
                <p className="text-xs text-slate-500">Average performance across all 7 audit modules</p>
              </div>

              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={componentScoreData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                    <XAxis dataKey="name" tick={{ fontSize: 10, fill: '#64748B' }} />
                    <YAxis domain={[0, 100]} tick={{ fontSize: 10, fill: '#64748B' }} />
                    <Tooltip />
                    <Bar dataKey="score" fill="#0071C5" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>

              <div className="grid grid-cols-2 md:grid-cols-7 gap-3">
                {componentScoreData.map((c: any) => (
                  <div key={c.name} className="p-3 rounded-xl bg-slate-50 border border-slate-200/80 space-y-1 text-center">
                    <div className="text-xs font-bold text-slate-700">{c.name}</div>
                    <div className="text-xl font-black text-intel-blue">{c.score}</div>
                    <div className="text-[10px] text-slate-400">Weight: {c.weight}</div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </>
      )}

      {/* Verifiable Evidence Drawer Modal */}
      {activeEvidence && (
        <EvidenceDrawer
          evidence={activeEvidence}
          onClose={() => setActiveEvidence(null)}
        />
      )}
    </div>
  );
};
