import React, { useState } from 'react';
import { Image, ExternalLink, Tag, Award, Gamepad2, Sparkles, CheckCircle2, XCircle, Camera, Calendar, Inbox } from 'lucide-react';
import { useApp } from '../context/AppContext';
import { BannersSubTab, ScorecardBanner } from '../types/scorecards';
import { SCORECARD_BANNERS } from '../data/scorecardsData';

export const BannerTrackingView: React.FC = () => {
  const { banners: appBanners } = useApp() as any;
  const [subTab, setSubTab] = useState<BannersSubTab>('banner-overview');
  const [selectedBanner, setSelectedBanner] = useState<ScorecardBanner | null>(null);

  const activeBanners = appBanners && appBanners.length > 0 ? appBanners : SCORECARD_BANNERS;
  const totalBanners = activeBanners.length;
  const distinctUrls = new Set(activeBanners.map((b: any) => b.destination_url)).size;
  const distinctRetailers = new Set(activeBanners.map((b: any) => b.account || b.retailer)).size;

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header & Sub-Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Image className="w-5 h-5 text-intel-navy" />
            <span>Homepage Hero Banner Intelligence &amp; Visual Placements</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Visual audit tracking brand share, promotional $-off discounts, destination link fidelity, and EVO/Gaming tags
          </p>
        </div>

        {/* 3 Banners SubTabs */}
        <div className="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-slate-200 text-xs font-semibold">
          {[
            { id: 'banner-overview', label: 'Banner Overview' },
            { id: 'banner-explorer', label: 'Banner Explorer' },
            { id: 'banner-evidence', label: 'Banner Evidence' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSubTab(tab.id as BannersSubTab)}
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

      {/* Dynamic Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="ent-card p-4 rounded-xl">
          <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
            Active Harvested Banners
          </div>
          <div className="text-2xl font-black text-slate-900 mt-1">
            {totalBanners}
          </div>
          <div className="text-[11px] text-slate-500 mt-1 font-medium">
            Visual Hero Placements
          </div>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
            Audited Retail Storefronts
          </div>
          <div className="text-2xl font-black text-intel-blue mt-1">
            {distinctRetailers}
          </div>
          <div className="text-[11px] text-slate-500 mt-1 font-medium">
            Active Homepage Trackers
          </div>
        </div>

        <div className="ent-card p-4 rounded-xl">
          <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
            Destination Endpoints
          </div>
          <div className="text-2xl font-black text-emerald-600 mt-1">
            {distinctUrls}
          </div>
          <div className="text-[11px] text-slate-500 mt-1 font-medium">
            Verified Landing URLs
          </div>
        </div>
      </div>

      {/* Banner Grid */}
      {totalBanners === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No Banners Available</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no banner placement records currently loaded.
            </p>
          </div>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {activeBanners.map((b: any) => {
            const isIntel = (b.banner_brand || '').toLowerCase().includes('intel');
            return (
              <div
                key={b.banner_id}
                onClick={() => setSelectedBanner(b)}
                className="ent-card rounded-2xl overflow-hidden hover:shadow-md transition-all cursor-pointer flex flex-col justify-between"
              >
                <div>
                  <div className="h-44 bg-slate-100 relative overflow-hidden flex items-center justify-center border-b border-slate-100">
                    <img
                      src={b.screenshot}
                      alt={b.account}
                      className="w-full h-full object-cover"
                      onError={(e: any) => {
                        e.target.style.display = 'none';
                        if (e.target.parentElement) {
                          e.target.parentElement.innerHTML = '<div class="p-6 text-center text-xs text-slate-400 font-medium">Banner screenshot unavailable</div>';
                        }
                      }}
                    />
                    <div className="absolute top-2 left-2 flex items-center space-x-1">
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                        isIntel ? 'bg-intel-blue text-white' : 'bg-slate-900 text-white'
                      }`}>
                        {b.banner_brand}
                      </span>
                    </div>
                  </div>

                  <div className="p-4 space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-slate-900 text-sm">{b.account}</span>
                      <span className="text-[10px] font-mono text-slate-400">{b.country}</span>
                    </div>
                    <p className="text-xs text-slate-600 line-clamp-2">{b.headline || 'Promotional Campaign Hero Banner'}</p>
                  </div>
                </div>

                <div className="p-4 pt-0 flex items-center justify-between text-xs border-t border-slate-50 mt-2">
                  <span className="text-emerald-700 font-bold font-mono">
                    {b.discount_amount ? `$${b.discount_amount} Off` : 'Promo Placement'}
                  </span>
                  <a
                    href={b.destination_url}
                    target="_blank"
                    rel="noreferrer"
                    onClick={(e) => e.stopPropagation()}
                    className="text-intel-blue hover:underline font-semibold flex items-center gap-1"
                  >
                    <span>Inspect</span>
                    <ExternalLink className="w-3 h-3" />
                  </a>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
