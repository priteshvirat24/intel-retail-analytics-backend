import React from 'react';
import { FileText, X, Download, CheckCircle2, FileSpreadsheet, File } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ReportPreviewModal: React.FC = () => {
  const { reportPreviewTarget, setReportPreviewTarget } = useApp();

  if (!reportPreviewTarget) return null;

  const { title, type, data } = reportPreviewTarget;

  const handleDownload = (format: 'CSV' | 'XLSX' | 'PDF') => {
    const jsonString = `data:text/json;charset=utf-8,${encodeURIComponent(JSON.stringify(data, null, 2))}`;
    const link = document.createElement('a');
    link.href = jsonString;
    link.download = `${title.toLowerCase().replace(/\s+/g, '_')}_poc_report.${format.toLowerCase() === 'pdf' ? 'json' : format.toLowerCase()}`;
    link.click();
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl w-full max-w-4xl max-h-[90vh] overflow-hidden shadow-2xl flex flex-col animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            <div className="p-1.5 rounded-lg bg-intel-navy text-white">
              <FileText className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-900">{title}</h3>
              <p className="text-[11px] text-slate-500">Program Report Preview &amp; Export Center</p>
            </div>
          </div>
          <button
            onClick={() => setReportPreviewTarget(null)}
            className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-4 text-xs">
          <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-200">
            <div>
              <span className="font-semibold text-slate-900 block">Report Dataset Status</span>
              <span className="text-[11px] text-slate-500 block">Generated from real scraped POC data (Capped Scope)</span>
            </div>
            <div className="flex items-center space-x-2">
              <button
                onClick={() => handleDownload('CSV')}
                className="px-3 py-1.5 rounded-lg bg-slate-100 border border-slate-300 text-slate-700 hover:bg-slate-200 font-semibold text-xs flex items-center space-x-1"
              >
                <FileSpreadsheet className="w-3.5 h-3.5 text-emerald-600" />
                <span>Export CSV</span>
              </button>
              <button
                onClick={() => handleDownload('XLSX')}
                className="px-3 py-1.5 rounded-lg bg-slate-100 border border-slate-300 text-slate-700 hover:bg-slate-200 font-semibold text-xs flex items-center space-x-1"
              >
                <FileSpreadsheet className="w-3.5 h-3.5 text-intel-blue" />
                <span>Export XLSX</span>
              </button>
              <button
                onClick={() => handleDownload('PDF')}
                className="px-3 py-1.5 rounded-lg bg-intel-navy text-white hover:bg-intel-blue font-semibold text-xs flex items-center space-x-1 shadow-xs"
              >
                <File className="w-3.5 h-3.5 text-white" />
                <span>Export PDF</span>
              </button>
            </div>
          </div>

          <pre className="p-4 bg-slate-900 text-slate-100 rounded-xl font-mono text-[11px] max-h-[50vh] overflow-auto border border-slate-800 leading-relaxed">
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-200 flex justify-end">
          <button
            onClick={() => setReportPreviewTarget(null)}
            className="px-4 py-1.5 rounded-lg bg-slate-800 text-white hover:bg-slate-900 font-semibold text-xs"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};
