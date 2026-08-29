import React from 'react';
import {
  Search,
  Globe,
  Store,
  Layers,
  Calendar,
  ShieldAlert,
  Zap,
  SlidersHorizontal,
  Database,
  RefreshCw,
} from 'lucide-react';
import { useApp } from '../context/AppContext';

export const TopBar: React.FC = () => {
  const {
    searchQuery,
    setSearchQuery,
    selectedCountry,
    setSelectedCountry,
    selectedRetailer,
    setSelectedRetailer,
    selectedCategory,
    setSelectedCategory,
    dateRange,
    costMetrics,
    setSettingsModalOpen,
    scorecardAccounts,
    overviewKpis,
    isLoading,
    isError,
    errorMessage,
    lastUpdated,
    backendStatus,
    refetchData,
  } = useApp();

  const countriesList = [
    { code: 'ALL', name: `🌍 All Countries (${overviewKpis.totalAccounts} Targets)` },
    { code: 'United States', name: '🇺🇸 United States (US)' },
    { code: 'Canada', name: '🇨🇦 Canada (CA)' },
    { code: 'United Kingdom', name: '🇬🇧 United Kingdom (UK)' },
    { code: 'Germany', name: '🇩🇪 Germany (DE)' },
    { code: 'France', name: '🇫🇷 France (FR)' },
    { code: 'Italy', name: '🇮🇹 Italy (IT)' },
    { code: 'Spain', name: '🇪🇸 Spain (ES)' },
    { code: 'India', name: '🇮🇳 India (IN)' },
    { code: 'Japan', name: '🇯🇵 Japan (JP)' },
    { code: 'Australia', name: '🇦🇺 Australia (AU)' },
    { code: 'Brazil', name: '🇧🇷 Brazil (BR)' },
    { code: 'Mexico', name: '🇲🇽 Mexico (MX)' },
    { code: 'China', name: '🇨🇳 China (CN)' },
    { code: 'South Korea', name: '🇰🇷 South Korea (KR)' },
    { code: 'Poland', name: '🇵🇱 Poland (PL)' },
    { code: 'Sweden', name: '🇸🇪 Sweden (SE)' },
    { code: 'Norway', name: '🇳🇴 Norway (NO)' },
    { code: 'Denmark', name: '🇩🇰 Denmark (DK)' },
    { code: 'Turkey', name: '🇹🇷 Turkey (TR)' },
    { code: 'Vietnam', name: '🇻🇳 Vietnam (VN)' },
    { code: 'Chile', name: '🇨🇱 Chile (CL)' },
    { code: 'Colombia', name: '🇨🇴 Colombia (CO)' },
    { code: 'Indonesia', name: '🇮🇩 Indonesia (ID)' },
  ];

  // Robust country matcher supporting ISO codes & full names
  const matchCountry = (accountCountry: string, filter: string) => {
    if (!filter || filter === 'ALL') return true;
    const f = filter.toLowerCase().trim();
    const ac = (accountCountry || '').toLowerCase().trim();
    if (ac === f) return true;
    if ((f === 'us' || f === 'usa') && (ac.includes('united states') || ac === 'us')) return true;
    if ((f === 'uk' || f === 'gb') && (ac.includes('united kingdom') || ac === 'uk' || ac === 'gb')) return true;
    if (f === 'ca' && (ac.includes('canada') || ac === 'ca')) return true;
    if (f === 'de' && (ac.includes('germany') || ac === 'de')) return true;
    if (f === 'fr' && (ac.includes('france') || ac === 'fr')) return true;
    if (f === 'it' && (ac.includes('italy') || ac === 'it')) return true;
    if (f === 'es' && (ac.includes('spain') || ac === 'es')) return true;
    if (f === 'in' && (ac.includes('india') || ac === 'in')) return true;
    if (f === 'jp' && (ac.includes('japan') || ac === 'jp')) return true;
    if (f === 'au' && (ac.includes('australia') || ac === 'au')) return true;
    if (f === 'br' && (ac.includes('brazil') || ac === 'br')) return true;
    if (f === 'mx' && (ac.includes('mexico') || ac === 'mx')) return true;
    if (f === 'cn' && (ac.includes('china') || ac === 'cn')) return true;
    if (f === 'kr' && (ac.includes('korea') || ac === 'kr')) return true;
    if (f === 'pl' && (ac.includes('poland') || ac === 'pl')) return true;
    if (f === 'se' && (ac.includes('sweden') || ac === 'se')) return true;
    if (f === 'no' && (ac.includes('norway') || ac === 'no')) return true;
    if (f === 'dk' && (ac.includes('denmark') || ac === 'dk')) return true;
    if (f === 'tr' && (ac.includes('turkey') || ac === 'tr')) return true;
    if (f === 'vn' && (ac.includes('vietnam') || ac === 'vn')) return true;
    if (f === 'cl' && (ac.includes('chile') || ac === 'cl')) return true;
    if (f === 'co' && (ac.includes('colombia') || ac === 'co')) return true;
    if (f === 'id' && (ac.includes('indonesia') || ac === 'id')) return true;
    return false;
  };

  const filteredAccounts = scorecardAccounts.filter((a) => matchCountry(a.country, selectedCountry));

  return (
    <div className="w-full sticky top-0 z-40 bg-white border-b border-slate-200 shadow-xs">
      {/* ⚠️ Live Production Data Banner */}
      <div className="bg-slate-900 text-white px-4 py-1.5 text-xs flex flex-wrap items-center justify-between gap-2 border-b border-slate-800">
        <div className="flex items-center space-x-2.5">
          <span className="px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono font-bold text-[10px] border border-emerald-500/40 uppercase tracking-wider flex items-center gap-1">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            LIVE PRODUCTION DATA
          </span>
          <span className="font-medium text-slate-200 flex items-center gap-2">
            <span>Source: <strong className="text-intel-cyan font-semibold">Render Backend + Neon DB</strong></span>
            <span className="text-slate-500">&bull;</span>
            <span>Last Updated: <span className="font-mono text-slate-300">{lastUpdated ? new Date(lastUpdated).toLocaleString() : 'Live'}</span></span>
          </span>
        </div>

        <div className="flex items-center space-x-4 text-[11px] font-mono text-slate-300">
          <div className="flex items-center space-x-1.5">
            <Database className="w-3 h-3 text-emerald-400" />
            <span>DB: <strong className="text-white font-bold">{backendStatus}</strong></span>
          </div>
          <div className="flex items-center space-x-1.5">
            <span className="w-2 h-2 rounded-full bg-intel-blue"></span>
            <span>Live SKUs: <strong className="text-white font-bold">{isLoading ? '...' : overviewKpis.totalSkus}</strong></span>
          </div>
          <button
            onClick={() => refetchData()}
            title="Refresh Live Data"
            className="p-1 rounded hover:bg-slate-800 text-slate-300 hover:text-white transition-colors"
          >
            <RefreshCw className={`w-3 h-3 ${isLoading ? 'animate-spin text-intel-cyan' : ''}`} />
          </button>
        </div>
      </div>

      {/* Global Control Bar */}
      <div className="px-6 py-2.5 flex flex-wrap items-center justify-between gap-3">
        {/* Brand & Global Search */}
        <div className="flex items-center space-x-4 flex-1 min-w-[320px]">
          <div className="flex items-center space-x-2 shrink-0">
            <div className="w-7 h-7 rounded-lg bg-intel-navy text-white flex items-center justify-center font-bold text-xs shadow-sm">
              CI
            </div>
            <div>
              <div className="font-bold text-xs text-intel-navy leading-none">
                Intel <span className="text-intel-blue">Intelligence</span>
              </div>
              <div className="text-[10px] text-slate-600 font-medium">{overviewKpis.totalAccounts} Retailers &bull; {overviewKpis.totalCountries} Countries</div>
            </div>
          </div>

          <div className="relative flex-1 max-w-md">
            <Search className="w-3.5 h-3.5 text-slate-600 absolute left-3 top-2.5" />
            <input
              type="text"
              placeholder={`Search SKU, processor, OEM, or retailer across ${overviewKpis.totalAccounts} sites...`}
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full bg-slate-50 border border-slate-200 rounded-lg pl-8 pr-3 py-1.5 text-xs text-slate-900 placeholder-slate-600 focus:bg-white focus:outline-none focus:border-intel-blue transition-colors"
            />
          </div>
        </div>

        {/* Global Selectors */}
        <div className="flex flex-wrap items-center gap-2 text-xs">
          {/* Country Selector */}
          <div className="flex items-center space-x-1 bg-slate-50 border border-slate-200 rounded-lg px-2.5 py-1">
            <Globe className="w-3.5 h-3.5 text-slate-600" />
            <select
              value={selectedCountry}
              onChange={(e) => {
                setSelectedCountry(e.target.value);
                setSelectedRetailer('ALL');
              }}
              className="bg-transparent text-slate-800 font-medium text-xs focus:outline-none cursor-pointer max-w-[200px]"
            >
              {countriesList.map((c) => (
                <option key={c.code} value={c.code}>
                  {c.name}
                </option>
              ))}
            </select>
          </div>

          {/* Full Retailers Selector */}
          <div className="flex items-center space-x-1 bg-slate-50 border border-slate-200 rounded-lg px-2.5 py-1">
            <Store className="w-3.5 h-3.5 text-slate-600" />
            <select
              value={selectedRetailer}
              onChange={(e) => setSelectedRetailer(e.target.value)}
              className="bg-transparent text-slate-800 font-medium text-xs focus:outline-none cursor-pointer max-w-[230px]"
            >
              <option value="ALL">
                {selectedCountry === 'ALL'
                  ? `All Retailers (${filteredAccounts.length} Sites)`
                  : `All ${selectedCountry} Sites (${filteredAccounts.length} Sites)`}
              </option>
              {filteredAccounts.map((a) => (
                <option key={a.account} value={a.account}>
                  {a.account} ({a.account_type})
                </option>
              ))}
            </select>
          </div>

          {/* Category Selector */}
          <div className="flex items-center space-x-1 bg-slate-50 border border-slate-200 rounded-lg px-2.5 py-1">
            <Layers className="w-3.5 h-3.5 text-slate-600" />
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="bg-transparent text-slate-800 font-medium text-xs focus:outline-none cursor-pointer"
            >
              <option value="ALL">All Categories</option>
              <option value="Laptops">Laptops &amp; 2-in-1s</option>
              <option value="Desktops">Desktop Towers &amp; AIOs</option>
            </select>
          </div>

          {/* Date Range Selector */}
          <div className="flex items-center space-x-1 bg-slate-50 border border-slate-200 rounded-lg px-2.5 py-1 text-slate-700">
            <Calendar className="w-3.5 h-3.5 text-slate-600" />
            <span className="font-medium text-xs">{dateRange}</span>
          </div>

          {/* Settings / Guardrails Button */}
          <button
            onClick={() => setSettingsModalOpen(true)}
            className="p-1.5 rounded-lg border border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-600 hover:text-slate-900 transition-colors"
            title="Cost Guardrails & Settings"
          >
            <SlidersHorizontal className="w-4 h-4" />
          </button>

          {/* User Profile */}
          <div className="flex items-center space-x-2 pl-2 border-l border-slate-200">
            <div className="w-7 h-7 rounded-full bg-intel-light border border-intel-blue/30 text-intel-navy flex items-center justify-center font-bold text-xs">
              IE
            </div>
            <span className="text-xs font-semibold text-slate-800 hidden md:inline">
              Intel Executive
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
