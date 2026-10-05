import { chromium } from "playwright";
import fs from "node:fs/promises";

const sites = {
  lendafile: "https://lendafile.com/",
  currency: "https://ta-solutions.netlify.app/",
  miral: "https://miralinterior.com/",
  ewoke: "https://ewokevapes.com/",
  reinziel: "https://reinzielbiotech.com/",
  trademark: "https://trademarketing.netlify.app/",
  amz: "https://amzautomation.netlify.app/",
  spark: "https://4edgesolutions.netlify.app/",
  saxon: "https://saxondigitaltechnologies.netlify.app/"
};

await fs.mkdir("assets/screenshots", { recursive: true });
const browser = await chromium.launch({ headless: true });

for (const [name, url] of Object.entries(sites)) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  try {
    console.log(`Capturing ${name}: ${url}`);
    await page.goto(url, { waitUntil: "networkidle", timeout: 60000 });
    await page.waitForTimeout(2500);
    await page.screenshot({
      path: `assets/screenshots/${name}.png`,
      fullPage: false
    });
  } catch (error) {
    console.warn(`Capture failed for ${name}: ${error.message}`);
  } finally {
    await page.close();
  }
}
await browser.close();
