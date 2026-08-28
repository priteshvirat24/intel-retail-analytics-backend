import React from 'react';
import { Cpu, TrendingUp, TrendingDown, Layers, Sparkles } from 'lucide-react';
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend
} from 'recharts';

interface ProcessorReportViewProps {
  cpuData: any;
}

export const ProcessorReportView: React.FC<ProcessorReportViewProps> = ({ cpuData }) => {
  const seriesList = cpuData?.series_breakdown || [];
  const intelShare = cpuData?.intel_overall_cpu_share_pct || 73.7;
  const netMom = cpuData?.intel_overall_mom_delta_pct || +3.6;

  const COLORS = ['#00C7FD', '#0071C5', '#38BDF8', '#EF4444', '#F87171', '#94A3B8', '#8B5CF6'];

  const pieData = seriesList.map((s: any, idx: number) => ({
    name: s.processor_series,
    value: s.sku_count,
    share: s.share_pct,
    color: COLORS[idx % COLORS.length],
  }));

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* View Header */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-intel-cyan/20 border border-intel-cyan/30 text-intel-cyan">
              <Cpu className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">Processor Comparison &amp; Architecture Report</h2>
              <p className="text-xs text-slate-400">
                Comparing Intel Core Ultra, Core 14th Gen, AMD Ryzen 8000/7000, Apple Silicon M3, and Snapdragon X Elite
              </p>
            </div>
          </div>

          <div className="flex items-center space-x-4 bg-slate-900/90 border border-slate-700/80 px-4 py-2 rounded-2xl">
            <div>
              <span className="text-[11px] text-slate-400 block">Intel Architecture Share</span>
              <span className="text-2xl font-extrabold text-intel-cyan">{intelShare}%</span>
            </div>
            <div className="h-8 w-px bg-slate-700"></div>
            <div>
              <span className="text-[11px] text-slate-400 block">Simulated MoM Net Delta</span>
              <span className="text-2xl font-extrabold text-emerald-400 flex items-center">
                <TrendingUp className="w-5 h-5 mr-1" /> {netMom > 0 ? `+${netMom}%` : `${netMom}%`}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Grid Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Architecture Share Pie */}
        <div className="glass-panel p-6 rounded-2xl">
          <h3 className="text-base font-bold text-white mb-1">Processor Family Distribution</h3>
          <p className="text-xs text-slate-400 mb-4">Sampled SKU distribution across processor series</p>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={90}
                  paddingAngle={3}
                  dataKey="value"
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{ backgroundColor: '#0F172A', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* MoM Trend Breakdown Bar */}
        <div className="glass-panel p-6 rounded-2xl">
          <h3 className="text-base font-bold text-white mb-1">Month-over-Month (MoM) Share Velocity</h3>
          <p className="text-xs text-slate-400 mb-4">Simulated monthly trajectory of CPU architectures</p>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={seriesList} layout="vertical" margin={{ top: 5, right: 20, left: 40, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.5} />
                <XAxis type="number" stroke="#94A3B8" fontSize={11} tickFormatter={(val) => `${val}%`} />
                <YAxis dataKey="processor_series" type="category" stroke="#94A3B8" fontSize={10} width={110} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#0F172A', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                />
                <Bar dataKey="mom_delta_pct" name="MoM Change (%)" fill="#00C7FD" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Series Detail Table */}
      <div className="glass-panel rounded-2xl overflow-hidden">
        <div className="p-4 border-b border-slate-800">
          <h3 className="text-base font-bold text-white">Processor Series Intelligence Matrix</h3>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-950/80 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
              <tr>
                <th className="py-3 px-4">Processor Series</th>
                <th className="py-3 px-4">Platform Vendor</th>
                <th className="py-3 px-4">Sampled SKUs</th>
                <th className="py-3 px-4">Share of Volume %</th>
                <th className="py-3 px-4 text-right">MoM Velocity</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800 text-slate-300">
              {seriesList.map((s: any) => (
                <tr key={s.processor_series} className="hover:bg-slate-800/50 transition-colors">
                  <td className="py-3 px-4 font-bold text-white text-sm">{s.processor_series}</td>
                  <td className="py-3 px-4">
                    <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      s.is_intel ? 'bg-intel-blue/20 text-intel-cyan border border-intel-cyan/30' : 'bg-slate-800 text-slate-400'
                    }`}>
                      {s.is_intel ? 'Intel' : 'Competitor'}
                    </span>
                  </td>
                  <td className="py-3 px-4 font-mono">{s.sku_count}</td>
                  <td className="py-3 px-4 font-mono font-bold text-white">{s.share_pct}%</td>
                  <td className="py-3 px-4 text-right font-mono font-bold">
                    <span className={s.mom_delta_pct > 0 ? 'text-emerald-400' : s.mom_delta_pct < 0 ? 'text-rose-400' : 'text-slate-400'}>
                      {s.mom_delta_pct > 0 ? `+${s.mom_delta_pct}%` : `${s.mom_delta_pct}%`}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
