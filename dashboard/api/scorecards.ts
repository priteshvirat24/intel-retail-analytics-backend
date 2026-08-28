import { SCORECARD_PRODUCTS, SCORECARD_ACCOUNTS, SCORECARD_KEYWORDS, SCORECARD_BANNERS } from '../src/data/scorecardsData.js';

export default function handler(req: any, res: any) {
  const { country, account, type } = req.query || {};

  let products = SCORECARD_PRODUCTS;
  let accounts = SCORECARD_ACCOUNTS;

  if (country && country !== 'ALL') {
    accounts = accounts.filter(a => a.country.toLowerCase().includes(String(country).toLowerCase()));
    products = products.filter(p => p.country.toLowerCase().includes(String(country).toLowerCase()));
  }

  if (account && account !== 'ALL') {
    accounts = accounts.filter(a => a.account.toLowerCase() === String(account).toLowerCase());
    products = products.filter(p => p.account.toLowerCase() === String(account).toLowerCase());
  }

  res.status(200).json({
    success: true,
    total_accounts: accounts.length,
    total_products: products.length,
    accounts,
    products,
    keywords: SCORECARD_KEYWORDS,
    banners: SCORECARD_BANNERS,
    timestamp: new Date().toISOString()
  });
}
