import React from 'react';
import { AppProvider, useApp } from './context/AppContext';
import { TopBar } from './components/TopBar';
import { Sidebar } from './components/Sidebar';

// 17 Complete Views
import { OverviewView } from './views/OverviewView';
import { LiveExtractionView } from './views/LiveExtractionView';
import { RetailerCoverageView } from './views/RetailerCoverageView';
import { ScorecardsView } from './views/ScorecardsView';
import { ShareOfShelfView } from './views/ShareOfShelfView';
import { ShareOfVoiceView } from './views/ShareOfVoiceView';
import { ProductSkuView } from './views/ProductSkuView';
import { PricingIntelligenceView } from './views/PricingIntelligenceView';
import { BannerTrackingView } from './views/BannerTrackingView';
import { EvoTrackingView } from './views/EvoTrackingView';
import { RetailerExplorerView } from './views/RetailerExplorerView';
import { CountriesView } from './views/CountriesView';
import { OemsView } from './views/OemsView';
import { EvidenceView } from './views/EvidenceView';
import { DataQualityView } from './views/DataQualityView';
import { ScrapeCenterView } from './views/ScrapeCenterView';
import { CostCenterView } from './views/CostCenterView';
import { ReportsView } from './views/ReportsView';
import { ProgramHistoryView } from './views/ProgramHistoryView';

// Modals
import { ProductDetailDrawer } from './components/Modals/ProductDetailDrawer';
import { LiveValidationModal } from './components/Modals/LiveValidationModal';
import { RunSampleModal } from './components/Modals/RunSampleModal';
import { SettingsModal } from './components/Modals/SettingsModal';
import { SourceEvidenceModal } from './components/Modals/SourceEvidenceModal';
import { ReportPreviewModal } from './components/Modals/ReportPreviewModal';

const DashboardContent: React.FC = () => {
  const { activeTab } = useApp();

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 flex flex-col font-sans antialiased">
      {/* Persistent Enterprise Top Bar */}
      <TopBar />

      {/* Main Workspace Area */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Sidebar Navigation & Cost Control Widget */}
        <Sidebar />

        {/* Dynamic Main Content Workspace */}
        <main className="flex-1 p-6 overflow-y-auto max-h-[calc(100vh-88px)]">
          <div className="max-w-7xl mx-auto space-y-6">
            {activeTab === 'overview' && <OverviewView />}
            {activeTab === 'live-extraction' && <LiveExtractionView />}
            {activeTab === 'retailer-coverage' && <RetailerCoverageView />}
            {activeTab === 'scorecards' && <ScorecardsView />}
            {activeTab === 'sos' && <ShareOfShelfView />}
            {activeTab === 'sov' && <ShareOfVoiceView />}
            {activeTab === 'products' && <ProductSkuView />}
            {activeTab === 'pricing' && <PricingIntelligenceView />}
            {activeTab === 'banners' && <BannerTrackingView />}
            {activeTab === 'evo' && <EvoTrackingView />}
            {activeTab === 'retailers' && <RetailerExplorerView />}
            {activeTab === 'countries' && <CountriesView />}
            {activeTab === 'oems' && <OemsView />}
            {activeTab === 'evidence' && <EvidenceView />}
            {activeTab === 'data-quality' && <DataQualityView />}
            {activeTab === 'scrape-center' && <ScrapeCenterView />}
            {activeTab === 'cost-center' && <CostCenterView />}
            {activeTab === 'reports' && <ReportsView />}
            {activeTab === 'program-history' && <ProgramHistoryView />}
          </div>
        </main>
      </div>

      {/* Modals & Interactive Drawers */}
      <ProductDetailDrawer />
      <LiveValidationModal />
      <RunSampleModal />
      <SettingsModal />
      <SourceEvidenceModal />
      <ReportPreviewModal />
    </div>
  );
};

export function App() {
  return (
    <AppProvider>
      <DashboardContent />
    </AppProvider>
  );
}

export default App;
