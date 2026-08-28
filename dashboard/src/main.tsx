import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// Global error handler to prevent blank white screens
window.addEventListener('error', (event) => {
  console.error('GLOBAL ERROR:', event.error || event.message);
  const root = document.getElementById('root');
  if (root && root.innerHTML.trim() === '') {
    root.innerHTML = `
      <div style="padding: 30px; font-family: system-ui, sans-serif; background: #FFF1F2; color: #9F1239; border: 1px solid #FECDD3; border-radius: 12px; margin: 20px;">
        <h2 style="margin: 0 0 10px 0; font-size: 18px; font-weight: bold;">Application Runtime Error</h2>
        <pre style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #FDA4AF; overflow-x: auto; font-size: 13px; font-family: monospace;">${event.error?.stack || event.message}</pre>
        <button onclick="window.location.reload()" style="margin-top: 15px; padding: 8px 16px; background: #9F1239; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer;">Reload Application</button>
      </div>
    `;
  }
});

window.addEventListener('unhandledrejection', (event) => {
  console.error('UNHANDLED PROMISE REJECTION:', event.reason);
});

class RootErrorBoundary extends React.Component<{ children: React.ReactNode }, { hasError: boolean; error: Error | null }> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('REACT ERROR CAUGHT:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '30px', fontFamily: 'system-ui, sans-serif', background: '#FFF1F2', color: '#9F1239', margin: '20px', borderRadius: '12px', border: '1px solid #FECDD3' }}>
          <h2 style={{ margin: '0 0 10px 0', fontSize: '18px', fontWeight: 'bold' }}>Dashboard Render Error</h2>
          <p style={{ fontSize: '13px', margin: '0 0 10px 0' }}>An error occurred while rendering the Scorecards dashboard component tree:</p>
          <pre style={{ background: 'white', padding: '15px', borderRadius: '8px', border: '1px solid #FDA4AF', overflowX: 'auto', fontSize: '12px', fontFamily: 'monospace' }}>
            {this.state.error?.stack || this.state.error?.message}
          </pre>
          <button
            onClick={() => window.location.reload()}
            style={{ marginTop: '15px', padding: '8px 16px', background: '#9F1239', color: 'white', border: 'none', borderRadius: '6px', fontWeight: 'bold', cursor: 'pointer' }}
          >
            Reload Dashboard
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}

const rootEl = document.getElementById('root');
if (rootEl) {
  ReactDOM.createRoot(rootEl).render(
    <React.StrictMode>
      <RootErrorBoundary>
        <App />
      </RootErrorBoundary>
    </React.StrictMode>
  );
}
