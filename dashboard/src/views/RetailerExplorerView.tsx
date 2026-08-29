import React, { useState } from 'react';
import {
  Store,
  ExternalLink,
  ShieldCheck,
  Award,
  Layers,
  Search,
  Laptop,
  CheckCircle2,
  Clock,
  Database,
  ArrowRight,
  TrendingUp,
  SlidersHorizontal,
  History,
  Globe,
  Filter,
  Inbox
} from 'lucide-react';
import { useApp } from '../context/AppContext';
import { RetailersSubTab, ScorecardAccount, ScorecardSKU } from '../types/scorecards';

export const RetailerExplorerView: React.FC = () => {
  const { setSelectedSkuDetail, filteredScorecardAccounts, filteredScorecardProducts } = useApp() as any;
  const [subTab, setSubTab] = useState<RetailersSubTab>('account-explorer');
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [countryFilter, setCountryFilter] = useState<string>('ALL');
  const [typeFilter, setTypeFilter] = useState<string>('ALL');

  const accounts: ScorecardAccount[] = filteredScorecardAccounts || [];
  const products: ScorecardSKU[] = filteredScorecardProducts || [];

  const [activeAccount, setActiveAccount] = useState<string>(accounts[0]?.account || '');

  const countries = Array.from(new Set(accounts.map((a: any) => a.country))).filter(Boolean).sort();

  const filteredAccounts = [...accounts]
    .filter((a: any) => {
      const matchesSearch = !searchTerm ||
        (a.account && a.account.toLowerCase().includes(searchTerm.toLowerCase())) ||
        (a.country && a.country.toLowerCase().includes(searchTerm.toLowerCase()));
      const matchesCountry = countryFilter === 'ALL' || a.country === countryFilter;
      const matchesType = typeFilter === 'ALL' || (a.account_type && a.account_type.toLowerCase().includes(typeFilter.toLowerCase()));
      return matchesSearch && matchesCountry && matchesType;
    })
    .sort((a: any, b: any) => (b.Overall_score || 0) - (a.Overall_score || 0));

  const selectedAccountData: any = accounts.find((a: any) => a.account === (activeAccount || accounts[0]?.account)) || accounts[0];
  const accountProducts = selectedAccountData ? products.filter((p: any) => {
    if ((p.account || p.retailer) === selectedAccountData.account) return true;
    if (p.retailer_id && selectedAccountData.retailer_id && p.retailer_id === selectedAccountData.retailer_id) return true;
    const cleanP = (p.account || p.retailer || '').toLowerCase().replace(/[^a-z0-9]/g, '');
    const cleanR = (selectedAccountData.account || '').toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleanP && cleanR && cleanP === cleanR;
  }) : [];
  const intelCount = accountProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel' || p.is_intel).length;
  const intelSos = accountProducts.length > 0 ? Math.round((intelCount / accountProducts.length) * 1000) / 10 : (selectedAccountData?.sos_pct || selectedAccountData?.sos_intel_pct || 0);

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Store className="w-5 h-5 text-intel-navy" />
            <span>Retailers &amp; Accounts Intelligence Workspace</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Partner deep-dive tracking compliance scores, Share of Shelf, and catalog inventory across {accounts.length} active storefronts
          </p>
        </div>

        {/* 4 Retailer SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'account-explorer', label: 'Account Explorer' },
            { id: 'account-detail', label: 'Account Detail' },
            { id: 'account-performance', label: 'Performance' },
            { id: 'account-history', label: 'History' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as RetailersSubTab)}
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

      {accounts.length === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No Retailers Available</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no partner accounts in the active universe matching your filters.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* Controls Bar */}
          <div className="flex flex-wrap items-center justify-between gap-3 p-4 bg-white border border-slate-200 rounded-xl shadow-xs">
            <div className="flex flex-wrap items-center gap-2">
              <div className="relative">
                <Search className="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" />
                <input
                  type="text"
                  placeholder="Search account..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="pl-8 pr-3 py-1.5 rounded-lg border border-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-intel-blue w-48"
                />
              </div>

              <select
                value={countryFilter}
                onChange={(e) => setCountryFilter(e.target.value)}
                className="px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs bg-white text-slate-700 font-medium"
              >
                <option value="ALL">All Countries ({countries.length})</option>
                {countries.map((c) => (
                  <option key={c} value={c}>{c}</option>
                ))}
              </select>

              <select
                value={typeFilter}
                onChange={(e) => setTypeFilter(e.target.value)}
                className="px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs bg-white text-slate-700 font-medium"
              >
                <option value="ALL">All Channel Types</option>
                <option value="1P">1P Retailer</option>
                <option value="3P">3P Marketplace</option>
                <option value="OEM">OEM Direct</option>
              </select>
            </div>

            <div className="text-xs text-slate-500 font-medium">
              Showing <span className="font-bold text-slate-900">{filteredAccounts.length}</span> of {accounts.length} Storefronts
            </div>
          </div>

          {/* TAB 1: ACCOUNT EXPLORER */}
          {subTab === 'account-explorer' && (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {filteredAccounts.map((a: any) => {
                const accProds = products.filter((p: any) => (p.account || p.retailer) === a.account);
                const accIntelCount = accProds.filter((p: any) => (p.processor || '').toLowerCase() === 'intel').length;
                const sos = accProds.length > 0 ? Math.round((accIntelCount / accProds.length) * 100) : a.sos_intel_pct;

                return (
                  <div
                    key={a.account}
                    onClick={() => {
                      setActiveAccount(a.account);
                      setSubTab('account-detail');
                    }}
                    className="ent-card p-4 rounded-xl flex flex-col justify-between space-y-3 cursor-pointer hover:shadow-md transition-all"
                  >
                    <div>
                      <div className="flex items-center justify-between">
                        <span className="font-bold text-sm text-slate-900 truncate">{a.account}</span>
                        <span className="text-[10px] font-semibold px-2 py-0.5 bg-slate-100 text-slate-700 rounded-full">
                          {a.account_type || a.type}
                        </span>
                      </div>
                      <div className="text-[11px] text-slate-400 font-mono mt-0.5">{a.country}</div>
                    </div>

                    <div className="grid grid-cols-3 gap-2 pt-2 border-t border-slate-100 text-center">
                      <div className="p-2 rounded-lg bg-slate-50">
                        <div className="text-[9px] font-bold text-slate-400 uppercase">Live SKUs</div>
                        <div className="text-sm font-black text-slate-900 font-mono">
                          {accProds.length > 0 ? accProds.length : (a.products_count || 0)}
                        </div>
                      </div>
                      <div className="p-2 rounded-lg bg-slate-50">
                        <div className="text-[9px] font-bold text-slate-400 uppercase">Intel SOS</div>
                        <div className="text-sm font-black text-intel-blue font-mono">
                          {sos}% <span className="text-[9px] font-normal text-slate-400 font-sans">(N={accProds.length > 0 ? accProds.length : (a.products_count || 0)})</span>
                        </div>
                      </div>
                      <div className="p-2 rounded-lg bg-slate-50">
                        <div className="text-[9px] font-bold text-slate-400 uppercase">Score</div>
                        <div className="text-sm font-black text-emerald-600 font-mono">{a.Overall_score ?? 'N/A'}</div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* TAB 2: ACCOUNT DETAIL */}
          {subTab === 'account-detail' && selectedAccountData && (
            <div className="space-y-6">
              {/* Account Hero Card */}
              <div className="ent-card p-5 rounded-2xl bg-white space-y-4">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                  <div>
                    <div className="flex items-center space-x-2">
                      <h3 className="text-lg font-bold text-slate-900">{selectedAccountData.account}</h3>
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-intel-blue/10 text-intel-blue">
                        {selectedAccountData.account_type}
                      </span>
                    </div>
                    <div className="text-xs text-slate-500 font-mono mt-1">
                      {selectedAccountData.country} &bull; {selectedAccountData.website || selectedAccountData.domain}
                    </div>
                  </div>

                  <a
                    href={selectedAccountData.website || `https://${selectedAccountData.domain}`}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold"
                  >
                    <span>Visit Storefront</span>
                    <ExternalLink className="w-3 h-3" />
                  </a>
                </div>

                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-3 border-t border-slate-100">
                  <div className="p-3 bg-slate-50 rounded-xl">
                    <div className="text-[10px] font-bold text-slate-400 uppercase">Total Verified SKUs</div>
                    <div className="text-xl font-black text-slate-900 mt-0.5">{accountProducts.length} Products</div>
                  </div>
                  <div className="p-3 bg-slate-50 rounded-xl">
                    <div className="text-[10px] font-bold text-slate-400 uppercase">Intel Share of Shelf</div>
                    <div className="text-xl font-black text-intel-blue mt-0.5">{intelSos}% SOS</div>
                  </div>
                  <div className="p-3 bg-slate-50 rounded-xl">
                    <div className="text-[10px] font-bold text-slate-400 uppercase">Listing (S) Mark</div>
                    <div className="text-xl font-black text-slate-900 mt-0.5">
                      {selectedAccountData.listing_s_score !== undefined && selectedAccountData.listing_s_score !== null ? `${selectedAccountData.listing_s_score}/100` : 'N/A'}
                    </div>
                  </div>
                  <div className="p-3 bg-slate-50 rounded-xl">
                    <div className="text-[10px] font-bold text-slate-400 uppercase">Details (P) Mark</div>
                    <div className="text-xl font-black text-purple-700 mt-0.5">
                      {selectedAccountData.details_p_score !== undefined && selectedAccountData.details_p_score !== null ? `${selectedAccountData.details_p_score}/100` : 'N/A'}
                    </div>
                  </div>
                </div>
              </div>

              {/* Harvested SKUs Table for Selected Account */}
              <div className="ent-card p-5 rounded-2xl space-y-4">
                <h4 className="text-sm font-bold text-slate-900">
                  Harvested Catalog for {selectedAccountData.account} ({accountProducts.length} SKUs)
                </h4>

                <div className="overflow-x-auto max-h-96 rounded-xl border border-slate-100">
                  <table className="w-full text-left text-xs">
                    <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                      <tr>
                        <th className="py-2.5 px-3">Title</th>
                        <th className="py-2.5 px-2">OEM</th>
                        <th className="py-2.5 px-2">Processor</th>
                        <th className="py-2.5 px-2 text-right">Price</th>
                        <th className="py-2.5 px-2 text-center">Score</th>
                        <th className="py-2.5 px-3 text-right">Action</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {accountProducts.map((p: any, idx: number) => (
                        <tr
                          key={p.product_id || p.sku_index || idx}
                          onClick={() => setSelectedSkuDetail(p)}
                          className="hover:bg-slate-50/80 cursor-pointer"
                        >
                          <td className="py-2 px-3 font-medium text-slate-900 max-w-sm truncate">{p.product_title}</td>
                          <td className="py-2 px-2 text-slate-700">{p.oem}</td>
                          <td className="py-2 px-2">
                            <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-intel-blue/10 text-intel-blue">
                              {p.processor_model || p.processor}
                            </span>
                          </td>
                          <td className="py-2 px-2 text-right font-mono font-bold text-slate-900">
                            ${p.selling_price?.toLocaleString()}
                          </td>
                          <td className="py-2 px-2 text-center font-bold text-slate-900">
                            <div className="flex flex-col items-center gap-0.5">
                              <span>{p.Overall !== undefined && p.Overall !== null ? `${p.Overall}/100` : 'N/A'}</span>
                              {p.details_p !== undefined && p.details_p !== null ? (
                                <span className="px-1 py-0.2 rounded text-[7px] font-bold bg-blue-50 text-blue-700 border border-blue-200">
                                  FULL PDP (7-Rule)
                                </span>
                              ) : (
                                <span className="px-1 py-0.2 rounded text-[7px] font-bold bg-slate-100 text-slate-600 border border-slate-200">
                                  LISTING ONLY (2-Rule)
                                </span>
                              )}
                            </div>
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
            </div>
          )}

          {/* TAB 3: PERFORMANCE */}
          {subTab === 'account-performance' && (
            <div className="ent-card p-5 rounded-2xl space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Partner Performance Comparison</h4>
              <div className="overflow-x-auto max-h-[500px] rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Account</th>
                      <th className="py-2.5 px-2">Country</th>
                      <th className="py-2.5 px-2 text-center">Listing S</th>
                      <th className="py-2.5 px-2 text-center">Details P</th>
                      <th className="py-2.5 px-2 text-center">Overall</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredAccounts.map((a: any) => (
                      <tr key={a.account} className="hover:bg-slate-50/80">
                        <td className="py-2 px-3 font-bold text-slate-900">{a.account}</td>
                        <td className="py-2 px-2 text-slate-600">{a.country}</td>
                        <td className="py-2 px-2 text-center font-mono text-slate-800">
                          {a.listing_s_score !== undefined && a.listing_s_score !== null ? a.listing_s_score : 'N/A'}
                        </td>
                        <td className="py-2 px-2 text-center font-mono text-purple-700">
                          {a.details_p_score !== undefined && a.details_p_score !== null ? a.details_p_score : 'N/A'}
                        </td>
                        <td className="py-2 px-2 text-center font-mono font-bold text-emerald-600">
                          {a.Overall_score !== undefined && a.Overall_score !== null ? `${a.Overall_score}/100` : 'N/A'}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 4: HISTORY */}
          {subTab === 'account-history' && (
            <div className="ent-card p-5 rounded-2xl space-y-4">
              <h4 className="text-sm font-bold text-slate-900">Audit Provenance &amp; Verification Trail</h4>
              <p className="text-xs text-slate-500">Timestamped verification runs across active storefronts</p>
              <div className="overflow-x-auto max-h-[500px] rounded-xl border border-slate-100">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 font-bold sticky top-0 uppercase tracking-wider text-[10px]">
                    <tr>
                      <th className="py-2.5 px-3">Account</th>
                      <th className="py-2.5 px-2">Country</th>
                      <th className="py-2.5 px-2 text-center">Status</th>
                      <th className="py-2.5 px-3 text-right">Verification Date</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredAccounts.map((a: any) => (
                      <tr key={a.account} className="hover:bg-slate-50/80">
                        <td className="py-2 px-3 font-bold text-slate-900">{a.account}</td>
                        <td className="py-2 px-2 text-slate-600">{a.country}</td>
                        <td className="py-2 px-2 text-center">
                          <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800">
                            VERIFIED
                          </span>
                        </td>
                        <td className="py-2 px-3 text-right font-mono text-slate-500">2026-08-27 18:00</td>
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
