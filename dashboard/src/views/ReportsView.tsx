import React from 'react';
import {
  FileText,
  Download,
  Eye,
  FileSpreadsheet,
  File,
  ShieldCheck,
  Layers,
  Search,
  Image,
  Award,
  Cpu,
  Globe,
  Sparkles
} from 'lucide-react';
import { useApp } from '../context/AppContext';

export const ReportsView: React.FC = () => {
  const {
    sosData,
    sovData,
    auditData,
    evoData,
    pricingData,
    cpuData,
    regionalData,
    setReportPreviewTarget,
  } = useApp() as any;

  const reportsList = [
    {
      id: 'retailer-audit',
      title: 'Retailer Brand Audit & Compliance Report',
      description: 'S1, S2, P1, P2, P3, P4, P5 compliance matrix with 85% Laptop / 15% Desktop weighted program rollup.',
      icon: ShieldCheck,
      iconColor: 'text-emerald-600',
      badge: 'Weekly Audit',
      data: auditData,
    },
    {
      id: 'share-of-shelf',
      title: 'Processor Share of Shelf (SOS) Report',
      description: 'Intel Core/Ultra SKU volume share vs AMD Ryzen, Apple Silicon, and Qualcomm Snapdragon with OEM rankings.',
      icon: Layers,
      iconColor: 'text-intel-blue',
      badge: 'Shelf Analytics',
      data: sosData,
    },
    {
      id: 'share-of-voice',
      title: 'Search Share of Voice (SOV) & SERP Audit',
      description: 'Keyword-ranked share for 10 focus search queries with sponsored placement rate and top-2 page audit pass rates.',
      icon: Search,
      iconColor: 'text-intel-navy',
      badge: 'Search Intelligence',
      data: sovData,
    },
    {
      id: 'banner-tracking',
      title: 'Homepage Hero Banner Tracking Report',
      description: 'Visual placement audit tracking hero banners, promotional $-off discounts, and destination link fidelity.',
      icon: Image,
      iconColor: 'text-intel-cyan',
      badge: 'Visual Audit',
      data: pricingData,
    },
    {
      id: 'evo-tracking',
      title: 'Intel EVO Badge & Platform Adoption Report',
      description: 'Intel EVO / Evo Edition certification penetration rates by channel with EVO vs Non-EVO price premium analysis.',
      icon: Award,
      iconColor: 'text-purple-600',
      badge: 'Badge Tracking',
      data: evoData,
    },
    {
      id: 'processor-comparison',
      title: 'CPU Architecture & MoM Velocity Report',
      description: 'Volume breakdown of Intel Core Ultra Meteor Lake vs Raptor Lake vs AMD Ryzen 8000 with simulated MoM trend deltas.',
      icon: Cpu,
      iconColor: 'text-intel-navy',
      badge: 'Architecture Report',
      data: cpuData,
    },
    {
      id: 'regional-us',
      title: 'United States Domestic Intelligence Report',
      description: 'North America domestic pricing corridors, retail channel distribution, and active POC crawl dataset.',
      icon: Globe,
      iconColor: 'text-emerald-600',
      badge: 'US Market (Active)',
      data: regionalData?.regions?.united_states,
    },
    {
      id: 'regional-latam',
      title: 'LATAM Regional Expansion Architecture Report',
      description: 'Multi-market schema for Brazil, Mexico, Chile, and Colombia ready for production scale-up to 23 countries.',
      icon: Globe,
      iconColor: 'text-amber-600',
      badge: 'LATAM Architecture',
      data: regionalData?.regions?.latam,
    },
  ];

  const handleExport = (report: any, format: string) => {
    const jsonString = `data:text/json;charset=utf-8,${encodeURIComponent(JSON.stringify(report.data, null, 2))}`;
    const link = document.createElement('a');
    link.href = jsonString;
    link.download = `${report.id}_${format.toLowerCase()}.${format === 'PDF' ? 'json' : format.toLowerCase()}`;
    link.click();
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <FileText className="w-5 h-5 text-intel-navy" />
            <span>Program Deliverables &amp; Recurring Reports</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            On-demand report generation with interactive preview and multi-format export (CSV, XLSX, PDF)
          </p>
        </div>

        <div className="flex items-center space-x-2 bg-white p-3 rounded-xl border border-slate-200 shadow-2xs font-mono text-xs">
          <span className="text-slate-500">Available Reports:</span>
          <span className="text-xl font-extrabold text-intel-navy">8 Reports</span>
        </div>
      </div>

      {/* Reports Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {reportsList.map((r) => {
          const Icon = r.icon;
          return (
            <div
              key={r.id}
              className="ent-card ent-card-hover p-5 rounded-2xl flex flex-col justify-between space-y-4"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2.5">
                    <div className="p-2 rounded-xl bg-slate-50 border border-slate-200">
                      <Icon className={`w-5 h-5 ${r.iconColor}`} />
                    </div>
                    <span className="text-[10px] px-2 py-0.5 rounded-full font-bold bg-slate-100 text-slate-700 font-mono">
                      {r.badge}
                    </span>
                  </div>
                </div>

                <h3 className="text-sm font-bold text-slate-900">{r.title}</h3>
                <p className="text-xs text-slate-500 line-clamp-2">{r.description}</p>
              </div>

              {/* Action Buttons */}
              <div className="pt-3 border-t border-slate-100 flex items-center justify-between flex-wrap gap-2 text-xs">
                <button
                  onClick={() => setReportPreviewTarget({ title: r.title, type: r.id, data: r.data })}
                  className="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold flex items-center space-x-1"
                >
                  <Eye className="w-3.5 h-3.5" />
                  <span>Preview Data</span>
                </button>

                <div className="flex items-center space-x-1.5">
                  <button
                    onClick={() => handleExport(r, 'CSV')}
                    className="px-2.5 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 font-semibold text-[11px] flex items-center space-x-1"
                  >
                    <FileSpreadsheet className="w-3 h-3 text-emerald-600" />
                    <span>CSV</span>
                  </button>
                  <button
                    onClick={() => handleExport(r, 'XLSX')}
                    className="px-2.5 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 font-semibold text-[11px] flex items-center space-x-1"
                  >
                    <FileSpreadsheet className="w-3 h-3 text-intel-blue" />
                    <span>XLSX</span>
                  </button>
                  <button
                    onClick={() => handleExport(r, 'PDF')}
                    className="px-2.5 py-1.5 rounded-lg bg-intel-navy hover:bg-intel-blue text-white font-semibold text-[11px] flex items-center space-x-1 shadow-2xs"
                  >
                    <File className="w-3 h-3 text-white" />
                    <span>PDF</span>
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
