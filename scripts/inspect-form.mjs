/**
 * Open a job URL, take a screenshot, dump the form DOM, save artifacts so we can inspect.
 *
 * Usage:
 *   node scripts/inspect-form.mjs <URL>
 */
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let puppeteer;
try { puppeteer = (await import('puppeteer')).default; }
catch (e) {
    const fb = 'c:/Projects/soiqet/content-calendar/assets/node_modules/puppeteer/lib/esm/puppeteer/puppeteer.js';
    puppeteer = (await import(pathToFileURL(fb).href)).default;
}

const url = process.argv[2];
if (!url) { console.error('Usage: node scripts/inspect-form.mjs <URL>'); process.exit(1); }

const ARTIFACTS = path.resolve(__dirname, '..', 'form-artifacts');
await fs.mkdir(ARTIFACTS, { recursive: true });

const PROFILE_DIR = path.resolve(__dirname, '..', '.puppeteer-profile');

const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
    userDataDir: PROFILE_DIR,
    args: [
        '--start-maximized',
        '--no-sandbox',
        '--disable-blink-features=AutomationControlled',
    ],
});

const page = await browser.newPage();
console.log(`Navigating: ${url}`);
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
await new Promise(r => setTimeout(r, 5000));

// Try to find an "Apply" button and click it
const appliedClicked = await page.evaluate(() => {
    const els = [...document.querySelectorAll('a, button')];
    const target = els.find(e => /^\s*apply( for this job| now)?\s*$/i.test((e.textContent || '').trim()));
    if (target) { target.click(); return true; }
    return false;
});
if (appliedClicked) {
    console.log('Clicked Apply button. Waiting for form...');
    await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 15000 }).catch(() => {});
    await new Promise(r => setTimeout(r, 2000));
}

// Screenshot
const shot = path.join(ARTIFACTS, 'sellpy-form.png');
await page.screenshot({ path: shot, fullPage: true });
console.log(`Screenshot: ${shot}`);

// Dump all form fields with their identifying attributes
const dump = await page.evaluate(() => {
    const out = [];
    const inputs = [...document.querySelectorAll('input, textarea, select')];
    for (const el of inputs) {
        const id = el.id;
        const name = el.getAttribute('name') || '';
        const type = el.getAttribute('type') || el.tagName.toLowerCase();
        const aria = el.getAttribute('aria-label') || '';
        const placeholder = el.getAttribute('placeholder') || '';
        let labelText = '';
        if (id) {
            const lbl = document.querySelector(`label[for="${id}"]`);
            if (lbl) labelText = (lbl.textContent || '').trim().slice(0, 120);
        }
        if (!labelText) {
            const parent = el.closest('label');
            if (parent) labelText = (parent.textContent || '').trim().slice(0, 120);
        }
        let options = '';
        if (el.tagName === 'SELECT') {
            options = [...el.options].map(o => o.textContent.trim()).filter(Boolean).join(' | ').slice(0, 200);
        }
        out.push({ type, name, id, aria, placeholder, label: labelText, options, required: el.required });
    }
    // Also dump labels that aren't tied to inputs by for=
    const orphanLabels = [...document.querySelectorAll('label')]
        .filter(l => !l.htmlFor || !document.getElementById(l.htmlFor))
        .map(l => (l.textContent || '').trim().slice(0, 120))
        .filter(Boolean);
    return { inputs: out, orphanLabels };
});

const dumpPath = path.join(ARTIFACTS, 'sellpy-form-dump.json');
await fs.writeFile(dumpPath, JSON.stringify(dump, null, 2), 'utf-8');
console.log(`Form dump: ${dumpPath}`);
console.log(`\nFound ${dump.inputs.length} input/textarea/select elements:`);
for (const f of dump.inputs) {
    console.log(`  [${f.type}] name="${f.name}" id="${f.id}" aria="${f.aria.slice(0,40)}" label="${f.label.slice(0,60)}" placeholder="${f.placeholder.slice(0,40)}"`);
}

const url2 = page.url();
console.log(`\nCurrent URL: ${url2}`);
console.log('Browser stays open. Use Ctrl+C in this shell when done.');

// Keep browser open
await new Promise(() => {});
