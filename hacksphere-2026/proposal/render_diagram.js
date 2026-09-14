// Renders diagram HTML files to crisp PNGs via pre-installed Chromium.
// Usage: node render_diagram.js <input.html> <output.png> [selector]
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, output, selector = '#stage'] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ deviceScaleFactor: 3 });
  await page.goto('file://' + path.resolve(input));
  await page.waitForTimeout(400);
  const el = await page.$(selector);
  await el.screenshot({ path: output });
  await browser.close();
  console.log('rendered', output);
})();
