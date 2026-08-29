export const CURRENCY_SYMBOLS: Record<string, string> = {
  USD: '$',
  EUR: '€',
  GBP: '£',
  CAD: 'CA$',
  AUD: 'A$',
  INR: '₹',
  BRL: 'R$',
  MXN: 'MX$',
  PLN: 'zł',
  TRY: '₺',
  VND: '₫',
  NOK: 'kr',
  DKK: 'kr',
};

export const getCurrencySymbol = (currency?: string): string => {
  if (!currency) return '$';
  return CURRENCY_SYMBOLS[currency.toUpperCase()] || '$';
};

export const formatLocalPrice = (price?: number | null, currency?: string): string => {
  if (price === undefined || price === null) return '—';
  const sym = getCurrencySymbol(currency);
  const curr = (currency || 'USD').toUpperCase();
  return `${sym}${price.toLocaleString()} ${curr}`;
};

export const formatUsdPrice = (price?: number | null): string => {
  if (price === undefined || price === null) return '—';
  return `$${price.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} USD`;
};

export const formatDualPrice = (sellingPrice?: number | null, usdSellingPrice?: number | null, currency?: string): string => {
  const curr = (currency || 'USD').toUpperCase();
  const raw = formatLocalPrice(sellingPrice, curr);
  if (curr === 'USD') {
    return raw;
  }
  const usd = formatUsdPrice(usdSellingPrice);
  return `${raw} (${usd})`;
};
