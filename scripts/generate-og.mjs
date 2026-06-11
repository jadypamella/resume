/**
 * Generate Open Graph PNG images from HTML templates at 1200x630 (LinkedIn, X, Facebook standard).
 *
 * Usage:
 *   node scripts/generate-og.mjs                  # generate all templates
 *   node scripts/generate-og.mjs home             # generate only home.html
 *   node scripts/generate-og.mjs home,badges      # generate selected templates
 *
 * Output: ./og/<template>.png
 *
 * Requires: puppeteer
 *   npm i -D puppeteer
 *
 * If you don't want Puppeteer installed locally, the existing
 * c:/Projects/tools/job-tracker/scripts/generate-pdf.mjs already has Puppeteer wired up
 * and can be adapted by changing pdf() to screenshot({type: 'png', clip: {x:0,y:0,width:1200,height:630}}).
 */
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';
import { createRequire } from 'node:module';

// Resolve Puppeteer: prefer local install, fall back to SoiQet content-calendar's puppeteer.
const _r = createRequire(import.meta.url);
let puppeteer;
try {
    puppeteer = (await import('puppeteer')).default;
} catch (e1) {
    const fallback = 'c:/Projects/soiqet/content-calendar/assets/node_modules/puppeteer/lib/esm/puppeteer/puppeteer.js';
    try {
        puppeteer = (await import(pathToFileURL(fallback).href)).default;
    } catch (e2) {
        console.error('Puppeteer not found locally and SoiQet fallback failed.');
        console.error('Install: cd c:/Projects/jadypamella/resume && npm init -y && npm i -D puppeteer');
        throw e2;
    }
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');
const TEMPLATES_DIR = path.join(ROOT, 'og-templates');
const OUT_DIR = path.join(ROOT, 'og');

const DEFAULT_SIZE = { width: 1200, height: 630 };
// Per-template overrides. LinkedIn banner is 1584x396 (4:1), not the OG default 1200x630.
const SIZES = {
    'linkedin-banner': { width: 1584, height: 396 },
};

async function listTemplates() {
    const entries = await fs.readdir(TEMPLATES_DIR, { withFileTypes: true });
    return entries
        .filter(e => e.isFile() && e.name.endsWith('.html'))
        .map(e => e.name.replace(/\.html$/, ''));
}

async function renderTemplate(browser, name) {
    const { width, height } = SIZES[name] ?? DEFAULT_SIZE;
    const htmlPath = path.join(TEMPLATES_DIR, `${name}.html`);
    const fileUrl = `file://${htmlPath.replace(/\\/g, '/')}`;
    const page = await browser.newPage();
    await page.setViewport({ width, height, deviceScaleFactor: 2 });
    await page.goto(fileUrl, { waitUntil: 'networkidle0' });
    await page.evaluateHandle('document.fonts.ready');
    const outPath = path.join(OUT_DIR, `${name}.png`);
    await page.screenshot({
        path: outPath,
        clip: { x: 0, y: 0, width, height },
        omitBackground: false,
    });
    await page.close();
    return outPath;
}

async function main() {
    await fs.mkdir(OUT_DIR, { recursive: true });
    const argFilter = process.argv[2];
    const requested = argFilter
        ? argFilter.split(',').map(s => s.trim()).filter(Boolean)
        : await listTemplates();

    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });

    try {
        for (const name of requested) {
            const out = await renderTemplate(browser, name);
            console.log(`Wrote: ${out}`);
        }
    } finally {
        await browser.close();
    }
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
