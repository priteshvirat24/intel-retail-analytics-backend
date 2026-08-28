import categoryUrlsData from '../src/data/canonical_sos_category_urls.json' with { type: 'json' };

export default function handler(req: any, res: any) {
  const { year, form_factor, search } = req.query || {};

  let urls2024 = categoryUrlsData.category_urls.y2024;
  let urls2025 = categoryUrlsData.category_urls.y2025;

  if (form_factor) {
    urls2024 = urls2024.filter(u => u.form_factor.toLowerCase() === String(form_factor).toLowerCase());
    urls2025 = urls2025.filter(u => u.form_factor.toLowerCase() === String(form_factor).toLowerCase());
  }

  if (search) {
    const q = String(search).toLowerCase();
    urls2024 = urls2024.filter(u => u.url.toLowerCase().includes(q) || u.domain.toLowerCase().includes(q));
    urls2025 = urls2025.filter(u => u.url.toLowerCase().includes(q) || u.domain.toLowerCase().includes(q));
  }

  res.status(200).json({
    success: true,
    total_2024: urls2024.length,
    total_2025: urls2025.length,
    y2024_urls: urls2024,
    y2025_urls: urls2025,
    summary: categoryUrlsData.category_urls.summary,
    timestamp: new Date().toISOString()
  });
}
