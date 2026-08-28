import React from 'react';
import { AlertCircle, Cpu, ShieldCheck, Database, RefreshCw } from 'lucide-react';

interface HeaderProps {
  metadata?: any;
}

export const Header: React.FC<HeaderProps> = ({ metadata }) => {
  return (
    <header className="w-full sticky top-0 z-50 bg-intel-darker/90 backdrop-blur-md border-b border-slate-800">
      {/* ⚠️ Mandatory POC Disclaimer Banner */}
      <div className="bg-gradient-to-r from-amber-950/80 via-amber-900/90 to-amber-950/80 border-b border-amber-500/30 px-4 py-2 text-xs text-amber-200 flex items-center justify-between shadow-sm">
        <div className="flex items-center space-x-2">
          <AlertCircle className="w-4 h-4 text-amber-400 shrink-0 animate-pulse" />
          <span className="font-semibold tracking-wide">
            🔬 PROOF OF CONCEPT (POC) DATASET — Strictly Capped Sample Scope:
          </span>
          <span className="text-amber-100/90 hidden md:inline">
            3 1P Retailers (Best Buy, Walmart, Costco), 1 Marketplace (Amazon), 2 OEM Sites (Dell, HP) • 1 Country (US) • 19 Sample SKUs • 10 SOV Keywords
          </span>
          <span className="text-amber-300/80 text-[11px] italic ml-1">
            (Production architecture scales to 173 retailers, 23 countries, and 80 keywords)
          </span>
        </div>
        <div className="flex items-center space-x-2 font-mono text-[11px] text-amber-300/90 shrink-0">
          <span className="inline-block w-2 h-2 rounded-full bg-emerald-400"></span>
          <span>1-Time Batch Cache</span>
        </div>
      </div>

      {/* Main Navigation & Brand Header */}
      <div className="px-6 py-3 flex items-center justify-between">
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-intel-blue to-intel-cyan flex items-center justify-center shadow-lg shadow-intel-cyan/20">
              <Cpu className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h1 className="text-lg font-bold text-white tracking-tight flex items-center gap-1.5">
                  <span>Intel</span>
                  <span className="text-intel-cyan">PC Intelligence</span>
                  <span className="text-xs px-2 py-0.5 rounded-full bg-intel-blue/20 text-intel-cyan border border-intel-cyan/30 font-medium">
                    POC Cockpit
                  </span>
                </h1>
              </div>
              <p className="text-xs text-slate-400">
                In-Season Pricing, Brand Audit Compliance (S1..P5), Share of Shelf &amp; Voice Intelligence
              </p>
            </div>
          </div>
        </div>

        {/* Global Scope Pills */}
        <div className="hidden lg:flex items-center space-x-3 text-xs">
          <div className="px-3 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 flex items-center space-x-2 text-slate-300">
            <Database className="w-3.5 h-3.5 text-intel-cyan" />
            <span>6 Sites Sampled</span>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 flex items-center space-x-2 text-slate-300">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
            <span>19 Tested SKUs</span>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 flex items-center space-x-2 text-slate-300">
            <span className="w-2 h-2 rounded-full bg-intel-cyan animate-pulse"></span>
            <span>US Market (USD)</span>
          </div>
        </div>
      </div>
    </header>
  );
};
