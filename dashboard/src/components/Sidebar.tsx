import React from 'react';
import {
  LayoutDashboard,
  Store,
  Laptop,
  Tag,
  ShieldCheck,
  Image,
  Layers,
  Search,
  Award,
  Terminal,
  CheckCircle,
  FileText,
  DollarSign,
  Activity,
  SlidersHorizontal,
  Globe,
  Cpu,
  Camera,
  Calendar,
  Zap,
  Grid
} from 'lucide-react';
import { useApp } from '../context/AppContext';
import { NavTabId } from '../types/index';

export const Sidebar: React.FC = () => {
  const {
    activeTab,
    setActiveTab,
    costMetrics,
    setSettingsModalOpen,
  } = useApp();

  const navItems: Array<{ id: NavTabId; label: string; icon: React.FC<{ className?: string }>; badge?: string }> = [
    { id: 'overview', label: 'Overview', icon: LayoutDashboard },
    { id: 'live-extraction' as any, label: 'Live Ingestion POC', icon: Zap, badge: '1,518 SKUs' },
    { id: 'retailer-coverage' as any, label: '52 Retailer Coverage', icon: Grid, badge: '100%' },
    { id: 'scorecards', label: 'Scorecards', icon: ShieldCheck },
    { id: 'sos', label: 'Share of Shelf (SOS)', icon: Layers },
    { id: 'sov', label: 'Share of Voice (SOV)', icon: Search },
    { id: 'products', label: 'Products', icon: Laptop },
    { id: 'retailers', label: 'Retailers', icon: Store },
    { id: 'banners', label: 'Banners', icon: Image },
    { id: 'evo', label: 'EVO', icon: Award },
    { id: 'evidence', label: 'Evidence', icon: Camera },
    { id: 'data-quality', label: 'Data Quality', icon: CheckCircle },
    { id: 'scrape-center', label: 'Scrape Center', icon: Terminal },
    { id: 'cost-center', label: 'Bright Data Usage', icon: DollarSign },
    { id: 'reports', label: 'Reports', icon: FileText },
    { id: 'program-history', label: 'Program History', icon: Calendar },
  ];

  return (
    <aside className="w-64 bg-white border-r border-slate-200 flex flex-col justify-between select-none shrink-0 overflow-y-auto">
      {/* Navigation Links */}
      <div className="p-3 space-y-1">
        <div className="px-3 py-1.5 text-[10px] font-bold uppercase tracking-wider text-slate-400 font-mono">
          Intel Scorecards Tracking
        </div>

        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id as any)}
              className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded-xl text-xs font-semibold transition-all ${
                isActive
                  ? 'bg-intel-navy text-white shadow-xs font-bold'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              <Icon className={`w-4 h-4 shrink-0 ${isActive ? 'text-white' : 'text-slate-400'}`} />
              <span className="truncate flex-1 text-left">{item.label}</span>
              {item.badge && (
                <span className={`text-[9px] px-1.5 py-0.2 rounded-full font-mono font-bold ${
                  isActive ? 'bg-white/20 text-white' : 'bg-intel-blue/10 text-intel-blue'
                }`}>
                  {item.badge}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* Bottom Sticky Widgets: Cost & Settings */}
      <div className="p-3 border-t border-slate-200 bg-slate-50/70 space-y-2.5">
        {/* Bright Data Cost Widget */}
        <div className="p-3 rounded-xl bg-white border border-slate-200 shadow-2xs space-y-1.5">
          <div className="flex items-center justify-between text-[11px]">
            <span className="font-bold text-slate-700 flex items-center gap-1">
              <DollarSign className="w-3.5 h-3.5 text-emerald-600" /> Bright Data Usage
            </span>
            <span className="font-mono font-extrabold text-intel-navy">
              {costMetrics.used_requests} / {costMetrics.total_budget_requests}
            </span>
          </div>

          <div className="w-full bg-slate-100 h-1.5 rounded-full overflow-hidden">
            <div
              className="bg-intel-blue h-full rounded-full transition-all duration-300"
              style={{ width: `${(costMetrics.used_requests / costMetrics.total_budget_requests) * 100}%` }}
            ></div>
          </div>

          <div className="grid grid-cols-2 gap-1 pt-1 text-[10px] text-slate-500 font-mono">
            <div>
              <span>Cache Hit: </span>
              <strong className="text-emerald-700">{costMetrics.cache_hit_rate_pct}%</strong>
            </div>
            <div className="text-right">
              <span>Cost: </span>
              <strong className="text-slate-800">${costMetrics.estimated_cost_usd}</strong>
            </div>
          </div>
        </div>

        {/* System Status & Settings Trigger */}
        <div className="flex items-center justify-between px-1 text-[11px] text-slate-500">
          <div className="flex items-center space-x-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span className="font-medium text-slate-700">Cache Active</span>
          </div>

          <button
            onClick={() => setSettingsModalOpen(true)}
            className="flex items-center space-x-1 text-slate-500 hover:text-intel-navy font-semibold transition-colors"
            title="Configure Cost Guardrails"
          >
            <SlidersHorizontal className="w-3.5 h-3.5" />
            <span>Settings</span>
          </button>
        </div>
      </div>
    </aside>
  );
};
