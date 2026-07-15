import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError,
)


TIMEOUT = 15000

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


class RenderError(Exception):
    pass


@dataclass
class RenderResult:
    url: str
    status_code: int
    html: str
    screenshot: str
    response_time: float
    headers: dict



def render(url: str) -> RenderResult:
    start = time.time()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True
            )
            context = browser.new_context(
                viewport={
                    "width": 1440,
                    "height": 900,
                },
                permissions=[],
            )
            page = context.new_page()
            page.add_init_script("""
            Object.defineProperty(Notification, 'permission', {
                get: () => 'denied'
            });
            """)
            response = page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=TIMEOUT,
            )

            html = page.content()
            title = page.title().lower()
            challenger_markers = [
                "__cf_chl_rt_tk",
                "cf-browser-verification",
                "Just a moment".lower(),
                "attention required".lower(),
                "checking your browser".lower(),
            ]

            if(
                any(marker in html.lower() for marker in challenger_markers) 
                or any(marker in page.url.lower()for marker in challenger_markers) 
                or title in [
                    "just a moment...",
                    "attention required!",
                    "checking your browser",
                ]
            ):
                browser.close()
                raise RenderError(
                    "This website is protected by anti-bot service and cannot be analyzed directly by SiteSense."
                )
            result_url = page.url
            parsed = urlparse(page.url)
            filename = (
                parsed.netloc +parsed.path
            ).replace("/","_").replace(":","_")
            if not filename:
                filename = "homepage"
            screenshot_path = (
                SCREENSHOT_DIR /
                f"{filename}.png")

            page.screenshot(
                path=str(screenshot_path),
                full_page=True,
            )

            status_code = (
                response.status
                if response
                else 200
            )

            headers = (
                response.headers
                if response
                else {}
            )
            browser.close()

    except PlaywrightTimeoutError:
        raise RenderError(
            "The site took too long to respond"
        )

    except Exception as e:
        raise RenderError(str(e))


    return RenderResult(
        url=result_url,
        status_code=status_code,
        html=html,
        screenshot=str(screenshot_path),
        response_time=round(
            time.time() - start,
            3
        ),
        headers=headers,
    )