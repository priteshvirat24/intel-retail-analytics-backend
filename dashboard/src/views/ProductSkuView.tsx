import React, { useState } from 'react';
import {
  Laptop,
  Download,
  Search,
  ArrowUpDown,
  ExternalLink,
  ShieldCheck,
  Award,
  Zap,
  Filter,
  CheckCircle2,
  Calendar,
  Sparkles,
  Tag
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
import { ProductsSubTab, ScorecardSKU } from '../types/scorecards';
import { SCORECARD_PRODUCTS } from '../data/scorecardsData';

export const ProductSkuView: React.FC = () => {
  const { setSelectedSkuDetail, setLiveValidationTarget, pricingData, filteredScorecardProducts } = useApp() as any;
  const [subTab, setSubTab] = useState<ProductsSubTab>('product-explorer');
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [sortField, setSortField] = useState<keyof ScorecardSKU>('selling_price');
  const [sortAsc, setSortAsc] = useState<boolean>(true);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const pageSize = 50;

  const handleSort = (field: keyof ScorecardSKU) => {
    if (sortField === field) {
      setSortAsc(!sortAsc);
    } else {
      setSortField(field);
      setSortAsc(true);
    }
  };

  const filteredProducts = (filteredScorecardProducts || SCORECARD_PRODUCTS).filter((p: ScorecardSKU) => {
    if (!searchTerm) return true;
    const term = searchTerm.toLowerCase();
    return (
      p.product_title.toLowerCase().includes(term) ||
      p.oem.toLowerCase().includes(term) ||
      p.model.toLowerCase().includes(term) ||
      p.account.toLowerCase().includes(term) ||
      (p.product_id && p.product_id.toLowerCase().includes(term)) ||
      p.processor_model.toLowerCase().includes(term)
    );
  });

  const sortedProducts = [...filteredProducts].sort((a: any, b: any) => {
    let valA = a[sortField];
    let valB = b[sortField];
    if (typeof valA === 'string') valA = valA.toLowerCase();
    if (typeof valB === 'string') valB = valB.toLowerCase();
    if (valA < valB) return sortAsc ? -1 : 1;
    if (valA > valB) return sortAsc ? 1 : -1;
    return 0;
  });

  const totalPages = Math.ceil(sortedProducts.length / pageSize) || 1;
  const paginatedProducts = sortedProducts.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  const exportCSV = () => {
    const headers = [
      'date', 'month', 'quarter', 'year', 'source', 'top_account', 'country', 'account',
      'form_factor', 'Intel_keyword', 'keyword_rank', 'search_volume', 'category_url',
      'product_url', 'product_id', 'product_title', 'page_rank', 'product_rank',
      'original_price', 'selling_price', 'usd_original_price', 'usd_selling_price',
      'processor', 'graphic_card', 'Gaming', 'Evo', 'Vpro', 'Premium',
      'Overall', 'listing_s', 'details_p', 's1', 's2', 'p1', 'p2', 'p3', 'p4', 'p5',
      'ram', 'storage', 'storage_type', 'screen_size', 'operating_system', 'oem',
      'model', 'gen', 'processor_model', 'number', '3p_1p', 'Flag', 'concatenate'
    ];

    const rows = sortedProducts.map((p) => [
      `"${p.date}"`, p.month, p.quarter, p.year, p.source, p.top_account, `"${p.country}"`, `"${p.account}"`,
      p.form_factor, `"${p.Intel_keyword || ''}"`, p.keyword_rank || '', p.search_volume || '', `"${p.category_url || ''}"`,
      `"${p.product_url}"`, `"${p.product_id}"`, `"${p.product_title}"`, p.page_rank, p.product_rank,
      p.original_price, p.selling_price, p.usd_original_price, p.usd_selling_price,
      p.processor, `"${p.graphic_card}"`, p.Gaming, p.Evo, p.Vpro, p.Premium,
      p.Overall, p.listing_s, p.details_p, p.s1, p.s2, p.p1, p.p2, p.p3, p.p4, p.p5,
      p.ram, p.storage, p.storage_type, p.screen_size, `"${p.operating_system}"`, `"${p.oem}"`,
      `"${p.model}"`, `"${p.gen}"`, `"${p.processor_model}"`, `"${p.number}"`, p['3p_1p'], `"${p.Flag}"`, p.concatenate
    ]);

    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map((e) => e.join(','))].join('\n');
    const link = document.createElement('a');
    link.href = encodeURI(csvContent);
    link.download = 'intel_scorecards_master_catalog.csv';
    link.click();
  };

  const likeForLike = pricingData?.like_for_like_comparisons || [];

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Laptop className="w-5 h-5 text-intel-navy" />
            <span>Products Intelligence &amp; Master SKU Catalog</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Normalized 40+ column Intel Scorecards schema tracking time, account, hardware specifications, pricing, and S1..P5 scoring
          </p>
        </div>

        {/* 4 Products SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'product-explorer', label: 'Product Explorer' },
            { id: 'product-detail', label: 'Product Detail' },
            { id: 'product-comparison', label: 'Product Comparison' },
            { id: 'price-intelligence', label: 'Price Intelligence' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as ProductsSubTab)}
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

      {/* 1. Product Explorer Tab (Master Table) */}
      {subTab === 'product-explorer' && (
        <div className="space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div className="relative">
              <Search className="w-3.5 h-3.5 absolute left-3 top-2.5 text-slate-400" />
              <input
                type="text"
                placeholder="Search product, OEM, model, ID..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-8 pr-3 py-1.5 rounded-lg border border-slate-200 bg-white text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-intel-navy w-64"
              />
            </div>

            <button
              onClick={exportCSV}
              className="px-3.5 py-1.5 rounded-lg bg-intel-navy hover:bg-intel-blue text-white font-semibold text-xs flex items-center space-x-1.5 shadow-xs transition-colors"
            >
              <Download className="w-3.5 h-3.5" />
              <span>Export Master CSV</span>
            </button>
          </div>

          <div className="ent-card rounded-xl overflow-hidden shadow-xs">
            <div className="p-3.5 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-xs text-slate-500">
              <span className="font-semibold text-slate-700">Showing {sortedProducts.length} Scraped PC SKUs</span>
              <span className="text-[11px] text-intel-navy italic">Click any product row to open detailed drawer</span>
            </div>

            <div className="overflow-x-auto max-h-[calc(100vh-280px)]">
              <table className="w-full text-left text-xs whitespace-nowrap">
                <thead className="ent-table-header sticky top-0 z-10">
                  <tr>
                    <th onClick={() => handleSort('date')} className="py-2.5 px-3 cursor-pointer hover:text-slate-900">
                      <div className="flex items-center gap-1"><span>Date</span><ArrowUpDown className="w-3 h-3" /></div>
                    </th>
                    <th onClick={() => handleSort('account')} className="py-2.5 px-3 cursor-pointer hover:text-slate-900">
                      <div className="flex items-center gap-1"><span>Account</span><ArrowUpDown className="w-3 h-3" /></div>
                    </th>
                    <th onClick={() => handleSort('model')} className="py-2.5 px-3 cursor-pointer hover:text-slate-900">
                      <div className="flex items-center gap-1"><span>OEM / Model</span><ArrowUpDown className="w-3 h-3" /></div>
                    </th>
                    <th className="py-2.5 px-3">Product ID</th>
                    <th onClick={() => handleSort('processor')} className="py-2.5 px-3 cursor-pointer hover:text-slate-900">
                      <div className="flex items-center gap-1"><span>Processor</span><ArrowUpDown className="w-3 h-3" /></div>
                    </th>
                    <th className="py-2.5 px-3">Processor Model</th>
                    <th className="py-2.5 px-3">Number</th>
                    <th className="py-2.5 px-3">Generation</th>
                    <th className="py-2.5 px-3">GPU</th>
                    <th className="py-2.5 px-3">RAM (GB)</th>
                    <th className="py-2.5 px-3">Storage (GB)</th>
                    <th className="py-2.5 px-3">Type</th>
                    <th className="py-2.5 px-3">Screen</th>
                    <th className="py-2.5 px-3">Form Factor</th>
                    <th onClick={() => handleSort('selling_price')} className="py-2.5 px-3 cursor-pointer hover:text-slate-900 text-right">
                      <div className="flex items-center justify-end gap-1"><span>Selling Price</span><ArrowUpDown className="w-3 h-3" /></div>
                    </th>
                    <th className="py-2.5 px-3 text-right">USD Selling</th>
                    <th className="py-2.5 px-3 text-center">Evo</th>
                    <th className="py-2.5 px-3 text-center">Gaming</th>
                    <th className="py-2.5 px-3 text-center">vPro</th>
                    <th className="py-2.5 px-3 text-center">Premier SKU</th>
                    <th className="py-2.5 px-3 text-center">1P/3P</th>
                    <th className="py-2.5 px-3 text-center">Listing S</th>
                    <th className="py-2.5 px-3 text-center">Details P</th>
                    <th className="py-2.5 px-3 text-right">Overall</th>
                    <th className="py-2.5 px-3 text-center">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 text-slate-700">
                  {paginatedProducts.map((p: any, idx: number) => {
                    const isIntel = p.processor === 'Intel';
                    return (
                      <tr
                        key={p.product_id || p.sku_index || idx}
                        onClick={() => setSelectedSkuDetail(p)}
                        className="ent-table-row cursor-pointer font-mono text-[11px]"
                      >
                        <td className="py-2.5 px-3 text-slate-500">{p.date}</td>
                        <td className="py-2.5 px-3 font-bold text-slate-900 font-sans">{p.account}</td>
                        <td className="py-2.5 px-3 font-semibold text-slate-800 font-sans max-w-[180px] truncate">
                          {p.oem} {p.model}
                        </td>
                        <td className="py-2.5 px-3 text-slate-600">{p.product_id || 'ID: NULL'}</td>
                        <td className="py-2.5 px-3">
                          <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                            isIntel ? 'bg-intel-navy text-white' : 'bg-slate-200 text-slate-800'
                          }`}>
                            {p.processor}
                          </span>
                        </td>
                        <td className="py-2.5 px-3 font-semibold text-slate-800">{p.processor_model}</td>
                        <td className="py-2.5 px-3 text-intel-navy font-bold">{p.number}</td>
                        <td className="py-2.5 px-3 text-slate-500 font-sans">{p.gen}</td>
                        <td className="py-2.5 px-3 text-slate-600 max-w-[140px] truncate">{p.graphic_card}</td>
                        <td className="py-2.5 px-3">{p.ram}</td>
                        <td className="py-2.5 px-3">{p.storage}</td>
                        <td className="py-2.5 px-3">{p.screen_size || '—'}</td>
                        <td className="py-2.5 px-3 font-sans">{p.form_factor || 'Laptop'}</td>
                        <td className="py-2.5 px-3 text-right font-semibold text-slate-800">
                          {p.currency && p.currency !== 'USD' ? `${p.currency} ` : '$'}{p.selling_price?.toLocaleString()}
                        </td>
                        <td className="py-2.5 px-3 text-right font-extrabold text-emerald-700">
                          ${p.usd_selling_price?.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                        </td>
                        <td className="py-2.5 px-3 text-center">
                          {p.Evo === 'Y' ? <span className="text-purple-700 font-bold">Y</span> : <span className="text-slate-300">N</span>}
                        </td>
                        <td className="py-2.5 px-3 text-center">
                          {p.Gaming === 'Y' ? <span className="text-rose-600 font-bold">Y</span> : <span className="text-slate-300">N</span>}
                        </td>
                        <td className="py-2.5 px-3 text-center">
                          {p.Vpro === 'Y' ? <span className="text-intel-navy font-bold">Y</span> : <span className="text-slate-300">N</span>}
                        </td>
                        <td className="py-2.5 px-3 text-center">
                          {p.Premium === 'Y' ? <span className="text-intel-blue font-bold">Y</span> : <span className="text-slate-300">N</span>}
                        </td>
                        <td className="py-2.5 px-3 text-center font-bold">{p['3p_1p']}</td>
                        <td className="py-2.5 px-3 text-center font-bold text-slate-800">{p.listing_s}</td>
                        <td className="py-2.5 px-3 text-center font-bold text-slate-800">{p.details_p}</td>
                        <td className="py-2.5 px-3 text-right">
                          <div className="flex flex-col items-end gap-1">
                            <span className={`px-2 py-0.5 rounded font-bold text-[11px] ${
                              p.Overall >= 80 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                            }`}>
                              {p.Overall}/100
                            </span>
                            {p.details_p !== undefined && p.details_p !== null ? (
                              <span className="px-1.5 py-0.5 rounded text-[8px] font-bold tracking-tight bg-blue-50 text-blue-700 border border-blue-200" title="Evaluated across all 7 S1-S2 & P1-P5 rules">
                                FULL PDP (7-Rule)
                              </span>
                            ) : (
                              <span className="px-1.5 py-0.5 rounded text-[8px] font-bold tracking-tight bg-slate-100 text-slate-600 border border-slate-200" title="Evaluated on Listing rules S1-S2 only">
                                LISTING ONLY (2-Rule)
                              </span>
                            )}
                          </div>
                        </td>
                        <td className="py-2.5 px-3 text-center">
                          <button
                            onClick={(e) => {
                              e.stopPropagation();
                              setLiveValidationTarget(p);
                            }}
                            className="px-2 py-1 bg-intel-blue/10 hover:bg-intel-blue text-intel-blue hover:text-white rounded text-[10px] font-bold transition-colors"
                          >
                            Audit Evidence
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

            {/* Pagination Controls */}
            <div className="p-3 bg-slate-50 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-slate-600">
              <div>
                Showing <span className="font-bold text-slate-900">{Math.min((currentPage - 1) * pageSize + 1, sortedProducts.length)}</span> to{' '}
                <span className="font-bold text-slate-900">{Math.min(currentPage * pageSize, sortedProducts.length)}</span> of{' '}
                <span className="font-bold text-intel-blue">{sortedProducts.length.toLocaleString()}</span> Live SKUs
              </div>

              <div className="flex items-center space-x-2">
                <button
                  disabled={currentPage === 1}
                  onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
                  className="px-3 py-1 rounded-lg border border-slate-200 bg-white font-semibold text-slate-700 hover:bg-slate-100 disabled:opacity-40 disabled:cursor-not-allowed"
                >
                  Previous
                </button>
                <span className="font-mono text-xs text-slate-500 font-semibold">
                  Page {currentPage} of {totalPages}
                </span>
                <button
                  disabled={currentPage >= totalPages}
                  onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
                  className="px-3 py-1 rounded-lg border border-slate-200 bg-white font-semibold text-slate-700 hover:bg-slate-100 disabled:opacity-40 disabled:cursor-not-allowed"
                >
                  Next
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* 2. Product Detail Tab */}
      {subTab === 'product-detail' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {filteredProducts.slice(0, 50).map((p) => (
            <div
              key={p.product_id || p.product_title}
              onClick={() => setSelectedSkuDetail(p)}
              className="ent-card p-4 rounded-xl cursor-pointer hover:border-intel-navy space-y-2"
            >
              <div className="flex justify-between font-bold text-xs">
                <span>{p.oem} {p.model}</span>
                <span className="text-emerald-700 font-mono">${p.selling_price}</span>
              </div>
              <p className="text-xs text-slate-500 line-clamp-1">{p.product_title}</p>
              <div className="flex justify-between text-[11px] text-slate-500 font-mono pt-2 border-t border-slate-100">
                <span>{p.processor_model} {p.number}</span>
                <span>Score: {p.Overall ?? 'N/A'}%</span>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* 3. Product Comparison Tab */}
      {subTab === 'product-comparison' && (
        <div className="space-y-4">
          <div className="ent-card p-4 rounded-xl">
            <h3 className="text-sm font-bold text-slate-900 mb-1">Direct Like-for-Like Hardware Comparisons</h3>
            <p className="text-xs text-slate-500">Matching comparable Intel vs Competitor hardware configurations</p>
          </div>

          <div className="space-y-4">
            {likeForLike.map((pair: any, idx: number) => (
              <div key={idx} className="ent-card p-4 rounded-xl space-y-3">
                <span className="text-xs font-bold uppercase text-intel-navy">{pair.category}</span>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-3 bg-blue-50/40 rounded-xl border border-blue-200">
                    <span className="text-[10px] font-bold text-intel-navy block uppercase">Intel Platform</span>
                    <h4 className="text-xs font-bold text-slate-900 mt-1">{pair.intel_config.name}</h4>
                    <span className="text-sm font-extrabold text-emerald-700 font-mono mt-1 block">
                      ${pair.intel_config.price_usd?.toLocaleString()}
                    </span>
                  </div>
                  <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="text-[10px] font-bold text-slate-600 block uppercase">Competitor Platform</span>
                    <h4 className="text-xs font-bold text-slate-900 mt-1">{pair.competitor_config.name}</h4>
                    <span className="text-sm font-extrabold text-slate-800 font-mono mt-1 block">
                      ${pair.competitor_config.price_usd?.toLocaleString()}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 4. Price Intelligence Tab */}
      {subTab === 'price-intelligence' && (
        <div className="ent-card p-5 rounded-xl space-y-4">
          <h3 className="text-sm font-bold text-slate-900">In-Season Price Corridors &amp; Historical Trajectory</h3>
          <p className="text-xs text-slate-500">Tracking original price, selling price, and USD FX conversion</p>
          <div className="space-y-2 text-xs">
            {filteredProducts.slice(0, 50).map((p) => (
              <div key={p.product_id || p.product_title} className="p-3 bg-slate-50 rounded-lg border border-slate-200 flex justify-between items-center font-mono">
                <div>
                  <span className="font-bold text-slate-900 font-sans">{p.oem} {p.model}</span>
                  <div className="text-[11px] text-slate-400">Account: {p.account}</div>
                </div>
                <div className="text-right">
                  <span className="font-extrabold text-emerald-700 text-sm">${p.selling_price}</span>
                  <span className="text-slate-400 line-through text-[11px] ml-2">${p.original_price}</span>
                  <span className="text-[10px] text-amber-700 font-bold bg-amber-50 px-1.5 py-0.2 rounded border border-amber-200 ml-2">
                    -{p.discount_pct}%
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
