import React from 'react';
import { Tag, TrendingDown, ArrowRight, Sparkles, CheckCircle2, DollarSign, Inbox } from 'lucide-react';
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

export const PricingIntelligenceView: React.FC = () => {
  const { setSelectedSkuDetail, filteredScorecardProducts, pricingMetrics } = useApp() as any;
  const products = filteredScorecardProducts || [];

  // Dynamic Segment Summaries from actual product records
  const segments = ['AI PC (Core Ultra)', 'Gaming', 'Mainstream', 'Premium'];
  const segmentChartData = segments.map((seg) => {
    let segProducts: any[] = [];
    if (seg === 'AI PC (Core Ultra)') {
      segProducts = products.filter((p: any) => /ultra/i.test(p.processor_model || '') || p.Evo === 'Y');
    } else if (seg === 'Gaming') {
      segProducts = products.filter((p: any) => p.Gaming === 'Y');
    } else if (seg === 'Premium') {
      segProducts = products.filter((p: any) => p.Premium === 'Y' || p.concatenate === 'Y');
    } else {
      segProducts = products.filter((p: any) => !p.Gaming && !p.Evo && !p.Premium);
    }

    const intelProducts = segProducts.filter((p: any) => (p.processor || '').toLowerCase() === 'intel');
    const compProducts = segProducts.filter((p: any) => (p.processor || '').toLowerCase() !== 'intel');

    const avgOf = (arr: any[]) => {
      const prices = arr.map((p: any) => p.usd_selling_price || p.selling_price).filter(Boolean);
      return prices.length > 0 ? Math.round(prices.reduce((a: number, b: number) => a + b, 0) / prices.length) : 0;
    };

    return {
      name: seg,
      intelPrice: avgOf(intelProducts),
      compPrice: avgOf(compProducts),
      count: segProducts.length,
    };
  }).filter((s) => s.intelPrice > 0 || s.compPrice > 0);

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight flex items-center gap-2">
            <Tag className="w-5 h-5 text-intel-navy" />
            <span>Pricing Intelligence &amp; Segment Analytics</span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Normalized price corridor and discount analytics derived from {products.length.toLocaleString()} active SKU records
          </p>
        </div>
      </div>

      {/* ZERO DATA EMPTY STATE */}
      {products.length === 0 ? (
        <div className="ent-card rounded-2xl p-12 text-center space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto text-slate-400">
            <Inbox className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800">No Pricing Data Available</h3>
            <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
              There are no product records with pricing in the active selection.
            </p>
          </div>
        </div>
      ) : (
        <>
          {/* Top Pricing KPI Strip */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Average Selling Price
              </div>
              <div className="text-2xl font-black text-slate-900 mt-1">
                {pricingMetrics.avgPriceUsd !== null ? `$${pricingMetrics.avgPriceUsd.toLocaleString()}` : 'N/A'}
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Normalized USD Market Rate
              </div>
            </div>

            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Price Corridor Range
              </div>
              <div className="text-2xl font-black text-intel-blue mt-1">
                {pricingMetrics.minPriceUsd !== null ? `$${pricingMetrics.minPriceUsd} - $${pricingMetrics.maxPriceUsd?.toLocaleString()}` : 'N/A'}
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Min to Max Range
              </div>
            </div>

            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Average Promotional Discount
              </div>
              <div className="text-2xl font-black text-emerald-600 mt-1">
                {pricingMetrics.avgDiscountPct !== null ? `${pricingMetrics.avgDiscountPct}%` : '0%'}
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Across {pricingMetrics.discountedSkusCount} Discounted Models
              </div>
            </div>

            <div className="ent-card p-4 rounded-xl">
              <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 font-mono">
                Median Price
              </div>
              <div className="text-2xl font-black text-slate-900 mt-1">
                {pricingMetrics.medianPriceUsd !== null ? `$${pricingMetrics.medianPriceUsd.toLocaleString()}` : 'N/A'}
              </div>
              <div className="text-[11px] text-slate-500 mt-1 font-medium">
                Market Midpoint Rate
              </div>
            </div>
          </div>

          {/* Segment Price Distribution Chart */}
          <div className="ent-card p-5 rounded-xl">
            <h3 className="text-sm font-bold text-slate-900 mb-1">
              Average Selling Price (ASP) Comparison by PC Segment
            </h3>
            <p className="text-xs text-slate-500 mb-4">
              Comparing Intel configurations vs Competitor alternatives across PC categories
            </p>

            <div className="h-72 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={segmentChartData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                  <XAxis dataKey="name" stroke="#64748B" fontSize={11} />
                  <YAxis stroke="#64748B" fontSize={11} tickFormatter={(val) => `$${val}`} />
                  <Tooltip formatter={(value: any) => [`$${value}`, 'Avg Price']} />
                  <Legend verticalAlign="top" height={36} />
                  <Bar dataKey="intelPrice" name="Intel Configs" fill="#0071C5" radius={[4, 4, 0, 0]} />
                  <Bar dataKey="compPrice" name="Competitor Alternatives" fill="#94A3B8" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Price Tier Distribution Grid */}
          <div className="ent-card p-5 rounded-xl space-y-4">
            <h3 className="text-sm font-bold text-slate-900">
              Price Tier Catalog Distribution
            </h3>
            <p className="text-xs text-slate-500">
              Breakdown of active SKU volume across global price brackets
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
              {(pricingMetrics.priceTiers || []).map((tier: any) => (
                <div key={tier.tier} className="p-4 rounded-xl bg-slate-50 border border-slate-200/80 space-y-2">
                  <div className="text-xs font-bold text-slate-700">{tier.tier}</div>
                  <div className="text-2xl font-black text-slate-900">{tier.count} <span className="text-xs text-slate-400">SKUs</span></div>
                  <div className="w-full bg-slate-200 rounded-full h-1.5 overflow-hidden">
                    <div className="bg-intel-blue h-1.5 rounded-full" style={{ width: `${tier.percentage}%` }}></div>
                  </div>
                  <div className="text-[10px] text-slate-500 font-semibold">{tier.percentage}% of active catalog</div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
};
