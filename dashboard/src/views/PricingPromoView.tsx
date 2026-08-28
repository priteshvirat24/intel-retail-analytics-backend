import React from 'react';
import { Tag, TrendingDown, ArrowRight, Sparkles, CheckCircle2 } from 'lucide-react';
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

interface PricingPromoViewProps {
  pricingData: any;
  onSelectSkuById?: (skuId: string) => void;
}

export const PricingPromoView: React.FC<PricingPromoViewProps> = ({ pricingData }) => {
  const summaries = pricingData?.segment_summaries || {};
  const likeForLike = pricingData?.like_for_like_comparisons || [];

  // Segment Pricing Bar Data
  const segmentChartData = Object.keys(summaries).map((k) => {
    const s = summaries[k];
    return {
      name: k,
      avgPrice: s.avg_price_usd,
      intelPrice: s.avg_intel_price_usd,
      compPrice: s.avg_comp_price_usd,
      discountPct: s.avg_discount_pct,
    };
  });

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* View Header */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex items-center space-x-3 mb-2">
          <div className="p-2 rounded-xl bg-intel-blue/20 border border-intel-cyan/30 text-intel-cyan">
            <Tag className="w-6 h-6" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-white">In-Season Category Management &amp; Segment Pricing</h2>
            <p className="text-xs text-slate-400">
              Live price corridor tracking, promotional depth, and like-for-like hardware configuration benchmarking
            </p>
          </div>
        </div>
      </div>

      {/* Segment Pricing Breakdown Chart */}
      <div className="glass-panel p-6 rounded-2xl">
        <h3 className="text-base font-bold text-white mb-1">
          Average Selling Price (ASP) &amp; Promotional Depth by PC Segment
        </h3>
        <p className="text-xs text-slate-400 mb-4">
          Comparing Intel-powered configurations vs Competitor alternatives in USD
        </p>

        <div className="h-72 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={segmentChartData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.5} />
              <XAxis dataKey="name" stroke="#94A3B8" fontSize={11} />
              <YAxis stroke="#94A3B8" fontSize={11} tickFormatter={(val) => `$${val}`} />
              <Tooltip
                contentStyle={{ backgroundColor: '#0F172A', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                formatter={(value: any) => [`$${value}`, '']}
              />
              <Legend wrapperStyle={{ fontSize: '11px', paddingTop: '8px' }} />
              <Bar dataKey="intelPrice" name="Intel Configurations ASP ($)" fill="#00C7FD" radius={[6, 6, 0, 0]} />
              <Bar dataKey="compPrice" name="Competitor Configurations ASP ($)" fill="#EF4444" radius={[6, 6, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Like-for-Like Configuration Comparisons */}
      <div className="glass-panel p-6 rounded-2xl">
        <h3 className="text-base font-bold text-white mb-1 flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-intel-cyan" />
          <span>Like-for-Like Hardware Configuration Comparisons</span>
        </h3>
        <p className="text-xs text-slate-400 mb-6">
          Direct head-to-head analysis of comparable configurations across OEM, Processor Architecture, Display, and Price Delta
        </p>

        <div className="space-y-4">
          {likeForLike.map((pair: any, idx: number) => (
            <div key={idx} className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-lg">
              <div className="text-xs font-bold uppercase tracking-wider text-intel-cyan mb-3">
                {pair.category}
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
                {/* Intel Side */}
                <div className="p-4 rounded-xl bg-intel-blue/10 border border-intel-cyan/40 relative">
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-intel-blue text-white">
                      Intel Platform
                    </span>
                    <span className="text-xs text-slate-400">{pair.intel_config.retailer}</span>
                  </div>
                  <h4 className="text-sm font-bold text-white mt-1">{pair.intel_config.name}</h4>
                  <div className="flex items-baseline space-x-2 mt-2">
                    <span className="text-lg font-extrabold text-emerald-400">
                      ${pair.intel_config.price_usd?.toLocaleString()}
                    </span>
                    <span className="text-xs text-slate-400 line-through">
                      ${pair.intel_config.orig_price_usd?.toLocaleString()}
                    </span>
                    <span className="text-xs text-amber-400 font-bold">
                      -{pair.intel_config.discount_pct}% Off
                    </span>
                  </div>
                </div>

                {/* Competitor Side */}
                <div className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/80">
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-slate-700 text-slate-300">
                      Competitor Platform
                    </span>
                    <span className="text-xs text-slate-400">{pair.competitor_config.retailer}</span>
                  </div>
                  <h4 className="text-sm font-bold text-white mt-1">{pair.competitor_config.name}</h4>
                  <div className="flex items-baseline space-x-2 mt-2">
                    <span className="text-lg font-extrabold text-slate-200">
                      ${pair.competitor_config.price_usd?.toLocaleString()}
                    </span>
                    <span className="text-xs text-slate-400 line-through">
                      ${pair.competitor_config.orig_price_usd?.toLocaleString()}
                    </span>
                    <span className="text-xs text-amber-400 font-bold">
                      -{pair.competitor_config.discount_pct}% Off
                    </span>
                  </div>
                </div>
              </div>

              {/* Value Proposition Box */}
              <div className="mt-3.5 pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
                <div className="flex items-center space-x-2 text-slate-300">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span><strong>Intel Value Advantage:</strong> {pair.intel_value_proposition}</span>
                </div>
                <div className="font-mono text-[11px] text-intel-cyan shrink-0 ml-2">
                  Price Delta: {pair.delta_price_usd > 0 ? `+$${pair.delta_price_usd}` : `-$${Math.abs(pair.delta_price_usd)}`}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
