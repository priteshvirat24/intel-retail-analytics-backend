import React, { useState } from 'react';
import { TableProperties, Download, ExternalLink, ArrowUpDown, Cpu, ShieldCheck } from 'lucide-react';

interface ProductAttributeTableProps {
  products: any[];
  onSelectSku: (sku: any) => void;
}

export const ProductAttributeTable: React.FC<ProductAttributeTableProps> = ({ products, onSelectSku }) => {
  const [sortField, setSortField] = useState<string>('current_price');
  const [sortAsc, setSortAsc] = useState<boolean>(true);

  const handleSort = (field: string) => {
    if (sortField === field) {
      setSortAsc(!sortAsc);
    } else {
      setSortField(field);
      setSortAsc(true);
    }
  };

  const sortedProducts = [...products].sort((a, b) => {
    let valA = a[sortField];
    let valB = b[sortField];
    if (typeof valA === 'string') valA = valA.toLowerCase();
    if (typeof valB === 'string') valB = valB.toLowerCase();
    if (valA < valB) return sortAsc ? -1 : 1;
    if (valA > valB) return sortAsc ? 1 : -1;
    return 0;
  });

  const exportCSV = () => {
    const headers = [
      'SKU ID', 'Retailer', 'OEM', 'Model', 'Product ID', 'Processor Model', 'Processor Series', 'GPU',
      'Price USD', 'Orig Price', 'Discount %', 'Form Factor', 'Screen Size', 'Screen Type', 'RAM', 'Storage', 'OS', 'Compliance Score'
    ];
    const rows = sortedProducts.map((p) => [
      p.sku_id, p.retailer, p.oem, `"${p.model_series}"`, p.product_id, `"${p.processor_model}"`,
      p.processor_series, `"${p.graphics_card}"`, p.current_price, p.original_price, p.discount_pct,
      p.form_factor, p.screen_size, `"${p.screen_type}"`, p.ram_size, p.storage_size, `"${p.operating_system}"`, p.compliance_score
    ]);
    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map((e) => e.join(','))].join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'pc_intelligence_product_attributes.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* View Header */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-intel-cyan/20 border border-intel-cyan/30 text-intel-cyan">
              <TableProperties className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">Product Data Attribute Master Explorer</h2>
              <p className="text-xs text-slate-400">
                Complete 18-attribute hardware specification table with interactive search, sorting, and drilldown
              </p>
            </div>
          </div>

          <button
            onClick={exportCSV}
            className="flex items-center space-x-1.5 px-4 py-2 rounded-xl bg-intel-blue hover:bg-intel-navy text-white text-xs font-semibold shadow-md transition-colors"
          >
            <Download className="w-4 h-4" />
            <span>Export CSV Dataset</span>
          </button>
        </div>
      </div>

      {/* Attribute Master Table */}
      <div className="glass-panel rounded-2xl overflow-hidden shadow-2xl">
        <div className="p-4 border-b border-slate-800 flex items-center justify-between text-xs text-slate-400">
          <span>Showing {sortedProducts.length} Scraped PC SKUs</span>
          <span className="text-[11px] text-intel-cyan italic">Click any row for 18-attribute drilldown modal</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs whitespace-nowrap">
            <thead className="bg-slate-950/80 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
              <tr>
                <th onClick={() => handleSort('oem')} className="py-3 px-3 cursor-pointer hover:text-white">
                  <div className="flex items-center gap-1"><span>OEM / Model</span><ArrowUpDown className="w-3 h-3" /></div>
                </th>
                <th onClick={() => handleSort('retailer')} className="py-3 px-3 cursor-pointer hover:text-white">
                  <div className="flex items-center gap-1"><span>Retailer</span><ArrowUpDown className="w-3 h-3" /></div>
                </th>
                <th onClick={() => handleSort('processor_model')} className="py-3 px-3 cursor-pointer hover:text-white">
                  <div className="flex items-center gap-1"><span>Processor (CPU)</span><ArrowUpDown className="w-3 h-3" /></div>
                </th>
                <th onClick={() => handleSort('graphics_card')} className="py-3 px-3 cursor-pointer hover:text-white">
                  <div className="flex items-center gap-1"><span>Graphics (GPU)</span><ArrowUpDown className="w-3 h-3" /></div>
                </th>
                <th onClick={() => handleSort('current_price')} className="py-3 px-3 cursor-pointer hover:text-white text-right">
                  <div className="flex items-center justify-end gap-1"><span>Price (USD)</span><ArrowUpDown className="w-3 h-3" /></div>
                </th>
                <th className="py-3 px-3">Form Factor</th>
                <th className="py-3 px-3">Screen Size / Type</th>
                <th className="py-3 px-3">RAM</th>
                <th className="py-3 px-3">Storage</th>
                <th className="py-3 px-3">OS</th>
                <th onClick={() => handleSort('compliance_score')} className="py-3 px-3 cursor-pointer hover:text-white text-right">
                  <div className="flex items-center justify-end gap-1"><span>Audit Score</span><ArrowUpDown className="w-3 h-3" /></div>
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800 text-slate-300">
              {sortedProducts.map((p) => {
                const isIntel = p.is_intel_cpu;
                return (
                  <tr
                    key={p.sku_id}
                    onClick={() => onSelectSku(p)}
                    className="hover:bg-slate-800/60 cursor-pointer transition-colors"
                  >
                    <td className="py-3 px-3 font-medium text-white">
                      <div className="font-bold">{p.oem} {p.model_series}</div>
                      <div className="text-[10px] text-slate-400 font-mono">ID: {p.product_id}</div>
                    </td>
                    <td className="py-3 px-3 text-slate-300">{p.retailer}</td>
                    <td className="py-3 px-3">
                      <span className={`px-2 py-0.5 rounded font-mono text-[11px] font-semibold ${
                        isIntel ? 'bg-intel-blue/20 text-intel-cyan border border-intel-cyan/30' : 'bg-slate-800 text-rose-300'
                      }`}>
                        {p.processor_model}
                      </span>
                    </td>
                    <td className="py-3 px-3 text-slate-300 font-mono text-[11px]">{p.graphics_card}</td>
                    <td className="py-3 px-3 text-right">
                      <div className="font-extrabold font-mono text-emerald-400 text-sm">
                        ${p.current_price?.toLocaleString()}
                      </div>
                      {p.discount_amount > 0 && (
                        <div className="text-[10px] text-amber-400">-{p.discount_pct}% (${p.discount_amount})</div>
                      )}
                    </td>
                    <td className="py-3 px-3">{p.form_factor}</td>
                    <td className="py-3 px-3">{p.screen_size} {p.screen_type?.slice(0, 14)}</td>
                    <td className="py-3 px-3 font-mono">{p.ram_size}</td>
                    <td className="py-3 px-3 font-mono">{p.storage_size}</td>
                    <td className="py-3 px-3 text-slate-400 text-[11px]">{p.operating_system}</td>
                    <td className="py-3 px-3 text-right">
                      <span className={`px-2 py-0.5 rounded-md font-bold font-mono text-[11px] ${
                        p.compliance_score >= 80 ? 'bg-emerald-950 text-emerald-400' : 'bg-amber-950 text-amber-400'
                      }`}>
                        {p.compliance_score}%
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
