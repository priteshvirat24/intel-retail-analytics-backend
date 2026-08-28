import React from 'react';
import { Search, Filter, RotateCcw } from 'lucide-react';

export interface FilterState {
  search: string;
  oem: string;
  retailer: string;
  segment: string;
  formFactor: string;
}

interface FilterBarProps {
  filters: FilterState;
  setFilters: React.Dispatch<React.SetStateAction<FilterState>>;
  oemOptions: string[];
  retailerOptions: string[];
  segmentOptions: string[];
}

export const FilterBar: React.FC<FilterBarProps> = ({
  filters,
  setFilters,
  oemOptions,
  retailerOptions,
  segmentOptions,
}) => {
  const resetFilters = () => {
    setFilters({
      search: '',
      oem: 'ALL',
      retailer: 'ALL',
      segment: 'ALL',
      formFactor: 'ALL',
    });
  };

  const isFiltered =
    filters.search !== '' ||
    filters.oem !== 'ALL' ||
    filters.retailer !== 'ALL' ||
    filters.segment !== 'ALL' ||
    filters.formFactor !== 'ALL';

  return (
    <div className="bg-intel-dark/80 backdrop-blur-md border border-slate-800 rounded-2xl p-3.5 mb-6 shadow-md flex flex-wrap items-center justify-between gap-3 text-xs">
      <div className="flex flex-wrap items-center gap-2.5 flex-1 min-w-[280px]">
        {/* Search Input */}
        <div className="relative flex-1 min-w-[200px]">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-2.5" />
          <input
            type="text"
            placeholder="Search SKU, processor, OEM, or model..."
            value={filters.search}
            onChange={(e) => setFilters((prev) => ({ ...prev, search: e.target.value }))}
            className="w-full bg-slate-900/90 border border-slate-700/80 rounded-xl pl-9 pr-3 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-intel-cyan/70 transition-colors"
          />
        </div>

        {/* OEM Filter */}
        <div className="flex items-center space-x-1.5 bg-slate-900/80 border border-slate-700/80 rounded-xl px-2.5 py-1">
          <span className="text-slate-400 text-[11px]">OEM:</span>
          <select
            value={filters.oem}
            onChange={(e) => setFilters((prev) => ({ ...prev, oem: e.target.value }))}
            className="bg-transparent text-white focus:outline-none cursor-pointer py-1 font-medium"
          >
            <option value="ALL" className="bg-slate-900 text-white">All OEMs</option>
            {oemOptions.map((o) => (
              <option key={o} value={o} className="bg-slate-900 text-white">{o}</option>
            ))}
          </select>
        </div>

        {/* Retailer Filter */}
        <div className="flex items-center space-x-1.5 bg-slate-900/80 border border-slate-700/80 rounded-xl px-2.5 py-1">
          <span className="text-slate-400 text-[11px]">Retailer:</span>
          <select
            value={filters.retailer}
            onChange={(e) => setFilters((prev) => ({ ...prev, retailer: e.target.value }))}
            className="bg-transparent text-white focus:outline-none cursor-pointer py-1 font-medium"
          >
            <option value="ALL" className="bg-slate-900 text-white">All Retailers</option>
            {retailerOptions.map((r) => (
              <option key={r} value={r} className="bg-slate-900 text-white">{r}</option>
            ))}
          </select>
        </div>

        {/* Segment Filter */}
        <div className="flex items-center space-x-1.5 bg-slate-900/80 border border-slate-700/80 rounded-xl px-2.5 py-1">
          <span className="text-slate-400 text-[11px]">Segment:</span>
          <select
            value={filters.segment}
            onChange={(e) => setFilters((prev) => ({ ...prev, segment: e.target.value }))}
            className="bg-transparent text-white focus:outline-none cursor-pointer py-1 font-medium"
          >
            <option value="ALL" className="bg-slate-900 text-white">All Segments</option>
            {segmentOptions.map((s) => (
              <option key={s} value={s} className="bg-slate-900 text-white">{s}</option>
            ))}
          </select>
        </div>

        {/* Form Factor Filter */}
        <div className="flex items-center space-x-1.5 bg-slate-900/80 border border-slate-700/80 rounded-xl px-2.5 py-1">
          <span className="text-slate-400 text-[11px]">Form:</span>
          <select
            value={filters.formFactor}
            onChange={(e) => setFilters((prev) => ({ ...prev, formFactor: e.target.value }))}
            className="bg-transparent text-white focus:outline-none cursor-pointer py-1 font-medium"
          >
            <option value="ALL" className="bg-slate-900 text-white">All Form Factors</option>
            <option value="Laptop" className="bg-slate-900 text-white">Laptop / Notebook</option>
            <option value="Desktop" className="bg-slate-900 text-white">Desktop Tower / AIO</option>
          </select>
        </div>
      </div>

      {/* Reset Filter Button */}
      {isFiltered && (
        <button
          onClick={resetFilters}
          className="flex items-center space-x-1 px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 text-[11px] font-medium border border-slate-700 transition-colors shrink-0"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>Reset Filters</span>
        </button>
      )}
    </div>
  );
};
