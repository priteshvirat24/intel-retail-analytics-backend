import React from 'react';
import { Image, ExternalLink, Tag, Award, Gamepad2, Sparkles, CheckCircle2, XCircle } from 'lucide-react';

interface BannerGalleryViewProps {
  bannerData: any;
}

export const BannerGalleryView: React.FC<BannerGalleryViewProps> = ({ bannerData }) => {
  const banners = bannerData?.banner_records || [];
  const flags = bannerData?.flag_breakdown || {};

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* View Header */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-intel-cyan/20 border border-intel-cyan/30 text-intel-cyan">
              <Image className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">Homepage Banner Tracking &amp; Screenshot Gallery</h2>
              <p className="text-xs text-slate-400">
                Visual monitoring of hero placements, promotional $-off discounts, and destination link fidelity
              </p>
            </div>
          </div>

          <div className="flex items-center space-x-4 bg-slate-900/90 border border-slate-700/80 px-4 py-2 rounded-2xl">
            <div>
              <span className="text-[11px] text-slate-400 block">Intel Banner Share</span>
              <span className="text-2xl font-extrabold text-intel-cyan">{bannerData?.intel_banner_share_pct}%</span>
            </div>
            <div className="h-8 w-px bg-slate-700"></div>
            <div>
              <span className="text-[11px] text-slate-400 block">Link Compliance</span>
              <span className="text-2xl font-extrabold text-emerald-400">{bannerData?.destination_link_compliance_pct}%</span>
            </div>
          </div>
        </div>
      </div>

      {/* Flag Summary Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="glass-card p-3.5 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 block">AI PC Banners</span>
            <span className="text-xl font-bold text-intel-cyan mt-0.5 block">{flags.ai_pc_banners} Banners</span>
          </div>
          <Sparkles className="w-6 h-6 text-intel-cyan/80" />
        </div>

        <div className="glass-card p-3.5 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 block">Intel EVO Badged</span>
            <span className="text-xl font-bold text-purple-400 mt-0.5 block">{flags.evo_banners} Banners</span>
          </div>
          <Award className="w-6 h-6 text-purple-400/80" />
        </div>

        <div className="glass-card p-3.5 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 block">Gaming Certified</span>
            <span className="text-xl font-bold text-amber-400 mt-0.5 block">{flags.gaming_banners} Banners</span>
          </div>
          <Gamepad2 className="w-6 h-6 text-amber-400/80" />
        </div>

        <div className="glass-card p-3.5 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 block">Premier SKU Feature</span>
            <span className="text-xl font-bold text-emerald-400 mt-0.5 block">{flags.premier_sku_banners} Banners</span>
          </div>
          <CheckCircle2 className="w-6 h-6 text-emerald-400/80" />
        </div>
      </div>

      {/* Visual Banner Cards Gallery */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {banners.map((b: any) => {
          const isIntel = b.brand.includes('Intel');
          return (
            <div
              key={b.banner_id}
              className="glass-panel rounded-2xl overflow-hidden border border-slate-800 hover:border-slate-700 transition-all flex flex-col justify-between shadow-xl"
            >
              {/* Banner Render / Mock Image */}
              <div className="bg-slate-950 p-2 border-b border-slate-800">
                <img
                  src={`/screenshots/${b.screenshot_file.replace('.png', '.svg')}`}
                  alt={`Banner ${b.banner_id}`}
                  className="w-full h-auto rounded-lg object-contain max-h-[220px]"
                />
              </div>

              {/* Banner Details */}
              <div className="p-5 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <span className="text-xs font-bold text-white px-2 py-0.5 rounded bg-slate-800">
                      {b.retailer}
                    </span>
                    <span className={`text-xs font-bold px-2 py-0.5 rounded ${
                      isIntel ? 'bg-intel-blue text-white' : 'bg-slate-700 text-slate-300'
                    }`}>
                      {b.brand}
                    </span>
                  </div>
                  <span className="text-[10px] text-slate-400 font-mono">{b.position}</span>
                </div>

                <h4 className="text-sm font-bold text-white line-clamp-1">{b.headline}</h4>
                <p className="text-xs text-slate-400 line-clamp-2">{b.subheadline}</p>

                {/* Promo Text & Destination Link */}
                <div className="pt-3 border-t border-slate-800 flex items-center justify-between flex-wrap gap-2 text-xs">
                  <div className="text-amber-400 font-bold flex items-center gap-1">
                    <Tag className="w-3.5 h-3.5" />
                    <span>{b.discount_text}</span>
                  </div>

                  {b.has_destination_link ? (
                    <a
                      href={b.destination_link}
                      target="_blank"
                      rel="noreferrer"
                      className="inline-flex items-center space-x-1 text-intel-cyan hover:underline font-semibold text-xs"
                    >
                      <span>Destination Link Active</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </a>
                  ) : (
                    <span className="text-rose-400 text-xs flex items-center gap-1 font-semibold">
                      <XCircle className="w-3.5 h-3.5" /> No Destination Link
                    </span>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
