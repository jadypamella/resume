/**
 * Auto-fill job application forms using Jady's profile.
 * Opens Chrome in headful mode (visible window) so Jady can intervene if needed.
 *
 * Usage:
 *   node scripts/auto-fill-form.mjs <URL>
 *
 * Example:
 *   node scripts/auto-fill-form.mjs https://career.sellpy.se/jobs/7582044-machine-learning-engineer
 *
 * Strategy: navigate, identify form fields, fill safe ones, STOP BEFORE SUBMIT.
 */
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let puppeteer;
try {
    puppeteer = (await import('puppeteer')).default;
} catch (e1) {
    const fallback = 'c:/Projects/soiqet/content-calendar/assets/node_modules/puppeteer/lib/esm/puppeteer/puppeteer.js';
    puppeteer = (await import(pathToFileURL(fallback).href)).default;
}

const PROFILE = {
    firstName: 'Jady',
    lastName: 'Pamella',
    fullName: 'Jady Pamella',
    email: 'hello@jadypamella.com',
    phone: '+46 76 436 4451',
    phoneNoPrefix: '0764364451',
    city: 'Stockholm',
    country: 'Sweden',
    countryCode: 'SE',
    linkedin: 'https://linkedin.com/in/jadypamella',
    github: 'https://github.com/jadypamella',
    website: 'https://jadypamella.com',
    cvPath: 'C:\\Projects\\jadypamella\\resume\\Jady_Pamella_CV.pdf',
    pronouns: 'She/Her',
    gender: 'Female',
    yearsExperience: '12',
    visaSponsor: 'Yes',
    workAuthSweden: 'Requires Sponsorship',
    englishLevel: 'C1',
    swedishLevel: 'B1',
    portugueseLevel: 'C2',
    spanishLevel: 'B1',
};

const url = process.argv[2];
if (!url) {
    console.error('Usage: node scripts/auto-fill-form.mjs <URL>');
    process.exit(1);
}

console.log(`Opening: ${url}`);
console.log('Browser will open visibly. DO NOT close it until I finish.');
console.log('I will pause before submitting. Review every field, then click Submit yourself.\n');

const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
    args: [
        '--start-maximized',
        '--no-sandbox',
        '--disable-blink-features=AutomationControlled',
    ],
});

const page = await browser.newPage();
await page.goto(url, { waitUntil: 'networkidle2', timeout: 60000 });
console.log('Page loaded. Inspecting form fields...\n');

// Try Teamtailor pattern: look for the "Apply for this job" button first
async function clickApplyButton() {
    const selectors = [
        'a[href*="/applications/new"]',
        'button:contains("Apply")',
        'a:contains("Apply for this job")',
        'a:contains("Apply now")',
    ];
    for (const sel of selectors) {
        try {
            const handle = await page.$(sel);
            if (handle) {
                await handle.click();
                await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 10000 }).catch(() => {});
                return true;
            }
        } catch (e) { /* try next */ }
    }
    // Fallback: find any link/button with "Apply" text
    const applied = await page.evaluate(() => {
        const els = [...document.querySelectorAll('a, button')];
        const target = els.find(e => /apply/i.test(e.textContent || ''));
        if (target) { target.click(); return true; }
        return false;
    });
    if (applied) {
        await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 10000 }).catch(() => {});
        return true;
    }
    return false;
}

await clickApplyButton();
await new Promise(r => setTimeout(r, 2000));

// Field-mapping rules: aria-label / name / placeholder / label-text -> profile key
const RULES = [
    { keys: ['first name', 'förnamn', 'firstname', 'first-name', 'given name'], val: PROFILE.firstName },
    { keys: ['last name', 'efternamn', 'lastname', 'last-name', 'family name', 'surname'], val: PROFILE.lastName },
    { keys: ['full name', 'name', 'fullname'], val: PROFILE.fullName },
    { keys: ['email', 'e-mail', 'e-post'], val: PROFILE.email },
    { keys: ['phone', 'telefon', 'mobile', 'tel'], val: PROFILE.phone },
    { keys: ['linkedin', 'linkedin profile', 'linkedin url'], val: PROFILE.linkedin },
    { keys: ['github', 'github profile', 'github url'], val: PROFILE.github },
    { keys: ['website', 'portfolio', 'homepage', 'personal website'], val: PROFILE.website },
    { keys: ['city', 'stad'], val: PROFILE.city },
    { keys: ['country', 'land'], val: PROFILE.country },
    { keys: ['pronouns', 'preferred pronouns'], val: PROFILE.pronouns },
    { keys: ['years of experience', 'experience'], val: PROFILE.yearsExperience },
];

function matchKey(text) {
    if (!text) return null;
    const t = text.toLowerCase().trim();
    for (const r of RULES) {
        if (r.keys.some(k => t.includes(k))) return r.val;
    }
    return null;
}

// Find all form inputs and try to fill
const filled = await page.evaluate((rules) => {
    const inputs = [...document.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], input[type="url"], input:not([type]), textarea')];
    const results = [];
    const matchKey = (text, rules) => {
        if (!text) return null;
        const t = text.toLowerCase().trim();
        for (const r of rules) {
            if (r.keys.some(k => t.includes(k))) return r.val;
        }
        return null;
    };
    for (const input of inputs) {
        const aria = input.getAttribute('aria-label') || '';
        const name = input.getAttribute('name') || '';
        const placeholder = input.getAttribute('placeholder') || '';
        let labelText = '';
        const id = input.id;
        if (id) {
            const lbl = document.querySelector(`label[for="${id}"]`);
            if (lbl) labelText = lbl.textContent || '';
        }
        if (!labelText) {
            const parentLabel = input.closest('label');
            if (parentLabel) labelText = parentLabel.textContent || '';
        }
        const combined = [aria, name, placeholder, labelText].join(' ').toLowerCase();
        const val = matchKey(combined, rules);
        if (val) {
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            const nativeTextareaValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            if (input.tagName === 'TEXTAREA') {
                nativeTextareaValueSetter.call(input, val);
            } else {
                nativeInputValueSetter.call(input, val);
            }
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
            results.push({ field: combined.slice(0, 80), value: val });
        }
    }
    return results;
}, RULES);

console.log(`Filled ${filled.length} field(s):`);
for (const f of filled) console.log(`  - ${f.field.padEnd(50)} = ${f.value}`);

console.log('\n=================================================================');
console.log('I will now keep the browser OPEN for 10 minutes so you can:');
console.log('  1. Review every field I filled');
console.log('  2. Manually upload the CV from: C:\\Projects\\jadypamella\\resume\\Jady_Pamella_CV.pdf');
console.log('  3. Fill any free-text fields I could not detect');
console.log('  4. Click Submit yourself');
console.log('=================================================================\n');

await new Promise(r => setTimeout(r, 600000));
await browser.close();
