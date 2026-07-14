from pathlib import Path
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok = True)

def take_screenshot(url:str) -> str:
    filename = (
        url.replace("https://","").replace("http://","").replace("/","")
        .replace(":","_")
    ) + ".png"

    filepath = SCREENSHOT_DIR/filename
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= True)
        page = browser.new_page(
            viewport={"width":1440, "height":900}
        )
        page.goto(url, wait_until="networkidle", timeout = 30000)
        page.screenshot(
            path = str(filepath),
            full_page=True,
        )
        browser.close()

    return f"screenshots/{filename}"