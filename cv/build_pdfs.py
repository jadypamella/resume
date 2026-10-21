"""Render the CV HTML sources in this folder to PDF and copy them to the site folders."""
import shutil
import sys
from pathlib import Path

import fitz
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent

TARGETS = [HERE.parent / "assets" / "cv", HERE.parent]
EXPECTED_PAGES = {"Jady_Pamella_CV": 1, "Jady_Pamella_CV_Academic": 2}


def main() -> int:
    out_dir = HERE / "out"
    out_dir.mkdir(exist_ok=True)
    failed = False
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for name, expected in EXPECTED_PAGES.items():
            page.goto((HERE / f"{name}.html").as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            pdf = out_dir / f"{name}.pdf"
            page.pdf(path=str(pdf), format="A4", print_background=True, prefer_css_page_size=True)
            pages = fitz.open(pdf).page_count
            print(f"{name}: {pages} page(s), expected {expected}")
            failed |= pages != expected
        browser.close()
    if failed:
        print("Page count mismatch, nothing copied.")
        return 1
    for target in TARGETS:
        for name in EXPECTED_PAGES:
            shutil.copy2(out_dir / f"{name}.pdf", target / f"{name}.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
