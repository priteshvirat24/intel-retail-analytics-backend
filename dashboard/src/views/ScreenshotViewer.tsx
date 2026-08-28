import React, { useState } from 'react';
import { Camera, Image, Monitor, ExternalLink, X, Eye } from 'lucide-react';

interface ScreenshotViewerProps {
  screenshotIndex: any;
}

export const ScreenshotViewer: React.FC<ScreenshotViewerProps> = ({ screenshotIndex }) => {
  const [activeType, setActiveType] = useState<'all' | 'pdp' | 'banner'>('all');
  const [selectedImage, setSelectedImage] = useState<any | null>(null);

  const pdpScreenshots = screenshotIndex?.pdp_screenshots || [];
  const bannerScreenshots = screenshotIndex?.banner_screenshots || [];

  const combined = [
    ...bannerScreenshots.map((b: any) => ({ ...b, type: 'banner', title: `${b.retailer} - ${b.brand} Hero Banner` })),
    ...pdpScreenshots.map((p: any) => ({ ...p, type: 'pdp', title: `${p.retailer} - ${p.oem} ${p.model_series} PDP` })),
  ];

  const filtered = activeType === 'all'
    ? combined
    : combined.filter((i) => i.type === activeType);

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* View Header */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-intel-blue/20 border border-intel-cyan/30 text-intel-cyan">
              <Camera className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">Reference Screenshot Index &amp; Viewer</h2>
              <p className="text-xs text-slate-400">
                Visual audit evidence for SOS &amp; SOV entries (PDP product pages and homepage hero placements)
              </p>
            </div>
          </div>

          {/* Type Filter Buttons */}
          <div className="flex items-center space-x-2 bg-slate-900/90 border border-slate-700/80 p-1.5 rounded-2xl text-xs">
            <button
              onClick={() => setActiveType('all')}
              className={`px-3 py-1.5 rounded-xl font-medium transition-all ${
                activeType === 'all' ? 'bg-intel-blue text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              All Assets ({combined.length})
            </button>
            <button
              onClick={() => setActiveType('pdp')}
              className={`px-3 py-1.5 rounded-xl font-medium transition-all ${
                activeType === 'pdp' ? 'bg-intel-blue text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              PDP Pages ({pdpScreenshots.length})
            </button>
            <button
              onClick={() => setActiveType('banner')}
              className={`px-3 py-1.5 rounded-xl font-medium transition-all ${
                activeType === 'banner' ? 'bg-intel-blue text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              Banners ({bannerScreenshots.length})
            </button>
          </div>
        </div>
      </div>

      {/* Screenshot Thumbnail Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {filtered.map((item, idx) => {
          const filename = item.file?.split('/').pop() || '';
          return (
            <div
              key={idx}
              onClick={() => setSelectedImage(item)}
              className="glass-panel rounded-2xl overflow-hidden border border-slate-800 hover:border-intel-cyan/60 transition-all cursor-pointer group flex flex-col justify-between shadow-lg"
            >
              <div className="bg-slate-950 p-2 border-b border-slate-800 flex items-center justify-center min-h-[160px] relative overflow-hidden">
                <img
                  src={item.file ? (item.file.startsWith('/') ? item.file : `/evidence/screenshots/${item.file}`) : `/screenshots/${filename}`}
                  alt={item.title}
                  className="w-full h-auto rounded-lg object-contain max-h-[180px] group-hover:scale-105 transition-transform duration-300"
                  onError={(e: any) => {
                    e.target.style.display = 'none';
                    if (e.target.parentElement) {
                      e.target.parentElement.innerHTML = '<div class="p-6 text-center text-xs text-slate-500 font-mono flex flex-col items-center gap-1"><span class="text-slate-400 font-bold">Screenshot Unavailable</span><span>Archive asset pending</span></div>';
                    }
                  }}
                />
                <div className="absolute inset-0 bg-intel-blue/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                  <span className="px-3 py-1.5 rounded-xl bg-slate-900/90 text-intel-cyan text-xs font-bold flex items-center gap-1.5 shadow-xl">
                    <Eye className="w-3.5 h-3.5" /> Click to Inspect
                  </span>
                </div>
              </div>

              <div className="p-3.5">
                <div className="flex items-center justify-between text-[11px] mb-1">
                  <span className="font-bold text-slate-300">{item.retailer}</span>
                  <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-800 text-intel-cyan uppercase font-mono">
                    {item.type}
                  </span>
                </div>
                <h4 className="text-xs font-bold text-white group-hover:text-intel-cyan transition-colors line-clamp-1">
                  {item.title}
                </h4>
              </div>
            </div>
          );
        })}
      </div>

      {/* Modal Inspector */}
      {selectedImage && (
        <div className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-4xl max-h-[90vh] overflow-hidden flex flex-col shadow-2xl">
            <div className="px-6 py-4 bg-slate-800/90 border-b border-slate-700 flex items-center justify-between">
              <div>
                <h3 className="text-sm font-bold text-white">{selectedImage.title}</h3>
                <p className="text-xs text-slate-400 font-mono">
                  File: {selectedImage.file?.split('/').pop()}
                </p>
              </div>
              <button
                onClick={() => setSelectedImage(null)}
                className="p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="p-6 overflow-y-auto bg-slate-950 flex items-center justify-center">
              <img
                src={selectedImage.file ? (selectedImage.file.startsWith('/') ? selectedImage.file : `/evidence/screenshots/${selectedImage.file}`) : `/screenshots/${selectedImage.file?.split('/').pop()}`}
                alt="Selected reference"
                className="w-full h-auto max-h-[70vh] object-contain rounded-xl"
                onError={(e: any) => {
                  e.target.style.display = 'none';
                  if (e.target.parentElement) {
                    e.target.parentElement.innerHTML = '<div class="p-12 text-center text-sm text-slate-400 font-mono">Image asset unavailable on disk</div>';
                  }
                }}
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
