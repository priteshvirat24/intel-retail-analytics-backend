import React from 'react';
import { renderToString } from 'react-dom/server';
import App from './src/App.js';

try {
  const html = renderToString(React.createElement(App));
  console.log('RENDER SUCCESS! HTML length:', html.length);
} catch (err) {
  console.error('RENDER ERROR CAUGHT:', err);
}
