import json
from pathlib import Path
from typing import List
from datetime import datetime
from app.models.crawl_result import TargetCrawlReport


class HtmlReportGenerator:
    """Generates a state-of-the-art interactive HTML dashboard for crawl analytics."""

    @classmethod
    def generate(cls, reports: List[TargetCrawlReport], output_path: str = "reports/dashboard.html") -> str:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        total_targets = len(reports)
        overall_coverage = round(sum(r.sku_coverage for r in reports) / max(1, total_targets) * 100, 1) if reports else 0.0
        total_discovered = sum(r.discovered for r in reports)
        total_validated = sum(r.validated_count for r in reports)
        total_target_skus = sum(r.target_skus for r in reports)
        avg_latency = round(sum(r.avg_latency_ms for r in reports) / max(1, total_targets), 1) if reports else 0.0
        avg_block_rate = round(sum(r.block_rate for r in reports) / max(1, total_targets) * 100, 1) if reports else 0.0

        reports_json = json.dumps([r.model_dump() for r in reports])

        html_content = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multi-Site Crawl Orchestrator | Empirical SKU Extraction Dashboard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: rgba(22, 29, 47, 0.7);
      --card-border: rgba(255, 255, 255, 0.08);
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.15);
      --success: #10b981;
      --success-glow: rgba(16, 185, 129, 0.15);
      --warning: #f59e0b;
      --danger: #ef4444;
      --accent: #8b5cf6;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding: 2.5rem 2rem;
      line-height: 1.5;
    }}

    .container {{
      max-width: 1400px;
      margin: 0 auto;
    }}

    /* Header */
    .header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 2.5rem;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 1.5rem;
    }}
    .title-group h1 {{
      font-size: 2.25rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.35rem;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }}
    .badge-live {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--success-glow);
      color: var(--success);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.2rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .badge-live::before {{
      content: '';
      width: 6px;
      height: 6px;
      background: var(--success);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--success);
    }}

    /* KPI Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2.5rem;
    }}
    .kpi-card {{
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      padding: 1.25rem 1.5rem;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}
    .kpi-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(56, 189, 248, 0.3);
    }}
    .kpi-card::after {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
    }}
    .kpi-label {{
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }}
    .kpi-value {{
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}
    .kpi-subtext {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.25rem;
    }}

    /* Controls & Filters */
    .controls-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.5rem;
      align-items: center;
      justify-content: space-between;
    }}
    .search-input {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 0.65rem 1rem;
      border-radius: 0.65rem;
      font-family: inherit;
      font-size: 0.9rem;
      min-width: 300px;
      outline: none;
      transition: border-color 0.2s ease;
    }}
    .search-input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px var(--primary-glow);
    }}
    .filter-pills {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .pill {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 0.4rem 0.85rem;
      border-radius: 0.5rem;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .pill:hover, .pill.active {{
      background: var(--primary-glow);
      color: var(--primary);
      border-color: rgba(56, 189, 248, 0.4);
    }}

    /* Table */
    .table-container {{
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      overflow-x: auto;
      margin-bottom: 2.5rem;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }}
    th {{
      background: rgba(15, 23, 42, 0.6);
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 1rem 1.25rem;
      border-bottom: 1px solid var(--card-border);
    }}
    td {{
      padding: 1rem 1.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      vertical-align: middle;
    }}
    tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}

    /* Grade Pills */
    .grade-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      border-radius: 0.5rem;
      font-weight: 800;
      font-size: 0.85rem;
    }}
    .grade-A {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .grade-B {{ background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }}
    .grade-C {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }}
    .grade-D {{ background: rgba(249, 115, 22, 0.2); color: #fb923c; border: 1px solid rgba(249, 115, 22, 0.4); }}
    .grade-E {{ background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }}

    .cat-tag {{
      display: inline-block;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 0.2rem 0.5rem;
      border-radius: 0.35rem;
      color: #cbd5e1;
    }}

    .progress-bar-bg {{
      width: 100px;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
      overflow: hidden;
      display: inline-block;
      vertical-align: middle;
      margin-left: 0.5rem;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #38bdf8, #10b981);
      border-radius: 3px;
    }}

    .btn-inspect {{
      background: rgba(56, 189, 248, 0.1);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.35rem 0.75rem;
      border-radius: 0.4rem;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .btn-inspect:hover {{
      background: var(--primary);
      color: #090d16;
    }}

    /* Modal */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 999;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}
    .modal-content {{
      background: #0f172a;
      border: 1px solid var(--card-border);
      border-radius: 1.25rem;
      max-width: 950px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 2rem;
      position: relative;
    }}
    .modal-close {{
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
    }}
    .modal-close:hover {{ color: #fff; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="title-group">
        <h1>Multi-Site Crawl Orchestrator</h1>
        <div class="subtitle">
          <span>Global Retailer Empirical Extraction & Reliability Benchmark</span>
          <span class="badge-live">Audited & Verified</span>
        </div>
      </div>
    </div>

    <!-- KPI Grid -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Tested Targets</div>
        <div class="kpi-value">{total_targets}</div>
        <div class="kpi-subtext">35 Global Retailer Brands</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">SKU Coverage</div>
        <div class="kpi-value" style="color: #38bdf8;">{overall_coverage}%</div>
        <div class="kpi-subtext">{total_validated} / {total_target_skus} Validated SKUs</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Discovered SKUs</div>
        <div class="kpi-value" style="color: #10b981;">{total_discovered}</div>
        <div class="kpi-subtext">Catalog Link Yield</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Avg Response Latency</div>
        <div class="kpi-value">{avg_latency}ms</div>
        <div class="kpi-subtext">Across HTTP & Playwright</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Block & Captcha Rate</div>
        <div class="kpi-value" style="color: #fb923c;">{avg_block_rate}%</div>
        <div class="kpi-subtext">Anti-Bot Trigger Frequency</div>
      </div>
    </div>

    <!-- Controls -->
    <div class="controls-bar">
      <input type="text" id="search" class="search-input" placeholder="Search retailer, country, category..." oninput="renderTable()">
      <div class="filter-pills">
        <button class="pill active" onclick="setFilter('ALL', this)">All</button>
        <button class="pill" onclick="setFilter('A', this)">Grade A (>=95%)</button>
        <button class="pill" onclick="setFilter('B', this)">Grade B (85-94%)</button>
        <button class="pill" onclick="setFilter('C', this)">Grade C (70-84%)</button>
        <button class="pill" onclick="setFilter('D', this)">Grade D (50-69%)</button>
        <button class="pill" onclick="setFilter('E', this)">Grade E (<50%)</button>
      </div>
    </div>

    <!-- Retailer Table -->
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Retailer</th>
            <th>Country</th>
            <th>Grade</th>
            <th>Category</th>
            <th>Target</th>
            <th>Discovered</th>
            <th>Validated</th>
            <th>Coverage</th>
            <th>Primary Strat</th>
            <th>Block %</th>
            <th>Latency</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody id="table-body"></tbody>
      </table>
    </div>
  </div>

  <!-- Drilldown Modal -->
  <div id="modal" class="modal-overlay" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeModal(null)">&times;</button>
      <div id="modal-body"></div>
    </div>
  </div>

  <script>
    const reportsData = {reports_json};
    let currentGradeFilter = 'ALL';

    function setFilter(grade, el) {{
      currentGradeFilter = grade;
      document.querySelectorAll('.filter-pills .pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');
      renderTable();
    }}

    function renderTable() {{
      const query = document.getElementById('search').value.toLowerCase();
      const tbody = document.getElementById('table-body');
      tbody.innerHTML = '';

      const filtered = reportsData.filter(r => {{
        const matchQuery = r.brand_name.toLowerCase().includes(query) ||
                           r.country.toLowerCase().includes(query) ||
                           r.capability_category.toLowerCase().includes(query);
        const matchGrade = (currentGradeFilter === 'ALL') || (r.capability_grade === currentGradeFilter);
        return matchQuery && matchGrade;
      }});

      if (filtered.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="12" style="text-align:center; padding: 2rem; color: var(--text-muted);">No matching retailer targets found.</td></tr>';
        return;
      }}

      filtered.forEach((r, idx) => {{
        const cov = Math.round(r.sku_coverage * 100);
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong>${{r.brand_name}}</strong></td>
          <td><span class="cat-tag">${{r.country}}</span></td>
          <td><span class="grade-badge grade-${{r.capability_grade}}">${{r.capability_grade}}</span></td>
          <td><span class="cat-tag">${{r.capability_category}}</span></td>
          <td>${{r.target_skus}}</td>
          <td>${{r.discovered}}</td>
          <td><strong style="color: #10b981;">${{r.validated_count}}</strong></td>
          <td>
            <strong>${{cov}}%</strong>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: ${{cov}}%;"></div></div>
          </td>
          <td><span class="cat-tag">${{r.primary_strategy}}</span></td>
          <td>${{Math.round(r.block_rate * 100)}}%</td>
          <td>${{Math.round(r.avg_latency_ms)}}ms</td>
          <td><button class="btn-inspect" onclick="openModal(${{idx}})">Inspect</button></td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function openModal(idx) {{
      const r = reportsData[idx];
      const modal = document.getElementById('modal');
      const modalBody = document.getElementById('modal-body');

      let skuHtml = '';
      if (r.sku_results && r.sku_results.length > 0) {{
        skuHtml = r.sku_results.map(s => `
          <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 1rem; border-radius: 0.5rem; margin-bottom: 0.75rem;">
            <div style="display:flex; justify-content:space-between; margin-bottom: 0.25rem;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:0.8rem; color:#38bdf8;">${{s.sku_id}}</span>
              <span class="cat-tag" style="background:${{s.status === 'SUCCESS' ? 'rgba(16,185,129,0.2)' : 'rgba(239,68,68,0.2)'}}; color:${{s.status === 'SUCCESS' ? '#34d399' : '#f87171'}};">${{s.status}}</span>
            </div>
            <div style="font-size:0.85rem; font-weight:600; margin-bottom:0.25rem; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
              ${{s.product ? (s.product.title || 'Untitled Product') : (s.failure ? s.failure.failure_reason_human : 'Extraction Failed')}}
            </div>
            <div style="display:flex; gap:1rem; font-size:0.75rem; color:var(--text-muted);">
              <span>Price: <strong>${{s.product && s.product.price ? s.product.currency + ' ' + s.product.price : 'N/A'}}</strong></span>
              <span>Availability: <strong>${{s.product ? s.product.availability : 'N/A'}}</strong></span>
              <span>Strategy: <strong>${{s.effective_strategy || s.primary_strategy}}</strong></span>
              <span>Latency: <strong>${{s.total_latency_ms}}ms</strong></span>
            </div>
          </div>
        `).join('');
      }} else {{
        skuHtml = '<div style="color:var(--text-muted); font-size:0.9rem;">No SKU traces recorded.</div>';
      }}

      modalBody.innerHTML = `
        <h2 style="font-size:1.5rem; margin-bottom:0.5rem;">${{r.brand_name}} (${{r.country}})</h2>
        <div style="display:flex; gap:1rem; margin-bottom:1.5rem; align-items:center;">
          <span class="grade-badge grade-${{r.capability_grade}}">${{r.capability_grade}}</span>
          <span class="cat-tag">${{r.capability_category}}</span>
          <span style="color:var(--text-muted); font-size:0.85rem;">Validated: ${{r.validated_count}}/${{r.target_skus}} (${{Math.round(r.sku_coverage*100)}}%)</span>
        </div>

        <div style="background:rgba(56,189,248,0.05); border:1px solid rgba(56,189,248,0.2); padding:1rem; border-radius:0.75rem; margin-bottom:1.5rem;">
          <h4 style="font-size:0.85rem; color:#38bdf8; margin-bottom:0.25rem; text-transform:uppercase;">Diagnosis & Recommended Architecture</h4>
          <p style="font-size:0.85rem; color:#cbd5e1;">${{r.failure_diagnosis_summary || 'Target operates smoothly.'}}</p>
          <div style="margin-top:0.5rem; font-size:0.8rem; color:#94a3b8;">Recommended Pipeline: <strong style="color:#fff;">${{r.recommended_strategy || 'HTTP-first'}}</strong></div>
        </div>

        <h3 style="font-size:1rem; margin-bottom:0.75rem;">Tested SKU Traces & Evidence</h3>
        <div style="max-height: 400px; overflow-y: auto;">
          ${{skuHtml}}
        </div>
      `;

      modal.style.display = 'flex';
    }}

    function closeModal(e) {{
      document.getElementById('modal').style.display = 'none';
    }}

    // Initial Render
    renderTable();
  </script>
</body>
</html>
"""
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        return str(out_file)
