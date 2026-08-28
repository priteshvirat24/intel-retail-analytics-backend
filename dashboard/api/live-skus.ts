import liveDataRaw from '../src/data/live_52_sku_dataset.json' with { type: 'json' };

export default function handler(req: any, res: any) {
  const { country, account, oem, processor, form_factor, limit, offset } = req.query || {};

  let skus = liveDataRaw.live_skus;

  if (country && country !== 'ALL') {
    skus = skus.filter(s => s.country.toLowerCase().includes(String(country).toLowerCase()));
  }

  if (account && account !== 'ALL') {
    skus = skus.filter(s => s.account.toLowerCase() === String(account).toLowerCase() || s.retailer_id === String(account));
  }

  if (oem && oem !== 'ALL') {
    skus = skus.filter(s => s.oem.toLowerCase() === String(oem).toLowerCase());
  }

  if (processor && processor !== 'ALL') {
    skus = skus.filter(s => s.processor.toLowerCase().includes(String(processor).toLowerCase()));
  }

  if (form_factor && form_factor !== 'ALL') {
    skus = skus.filter(s => s.form_factor.toLowerCase() === String(form_factor).toLowerCase());
  }

  const total = skus.length;
  const start = Number(offset) || 0;
  const end = limit ? start + Number(limit) : 100;
  const paginated = skus.slice(start, end);

  res.status(200).json({
    success: true,
    total_matching: total,
    returned_count: paginated.length,
    offset: start,
    limit: Number(limit) || 100,
    skus: paginated,
    timestamp: new Date().toISOString()
  });
}
