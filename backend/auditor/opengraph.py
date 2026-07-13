from dataclasses import dataclass
import re

from bs4 import BeautifulSoup

@dataclass
class OpenGraphResult:
    og_title: str | None
    og_description: str | None
    og_image: str| None
    og_url: str | None
    twitter_card: str | None

def analyze_opengraph(html:str) -> OpenGraphResult:
    soup = BeautifulSoup(html, "lxml")
    def get_meta(attr: str, value: str):
        tag = soup.find(
            "meta",
            attrs = {
                attr: re.compile(f"^{re.escape(value)}$", re.I)
            }
        )

        if not tag:
            return None
        content = tag.get("content", "").strip()
        return content if content else None
    
    return OpenGraphResult(
        og_title = get_meta("property", "og:title"),
        og_description = get_meta("property", "og:description"),
        og_image = get_meta("property", "og:image"),
        og_url = get_meta("property", "og:url"),
        twitter_card = get_meta("name", "twitter:card"),
    )