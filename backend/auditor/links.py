from dataclasses import dataclass
from urllib.parse import urlparse

from bs4 import BeautifulSoup

@dataclass
class LinkResult:
    total_links: int
    internal_links: int
    external_links: int
    empty_links: int
    mailto_links: int
    tel_links: int

def analyze_links(html: str, base_url:str ="") -> LinkResult:
    soup = BeautifulSoup(html, "lxml")
    links = soup.find_all("a")
    total_links = len(links)
    internal_links = 0
    external_links = 0
    empty_links = 0
    mailto_links = 0
    tel_links = 0

    base_domain =""
    if base_url:
        base_domain = urlparse(base_url).netloc

    for link in links:
        href = link.get("href")

        if href is None or href.strip() == "":
            empty_links +=1
            continue

        href = href.strip()

        if href.lower().startswith("mailto:"):
            mailto_links +=1
            continue
        
        if href.lower().startswith("tel"):
            tel_links+=1
            continue

        if href.startswith("/"):
            internal_links +=1
            continue

        parsed = urlparse(href)

        if parsed.scheme in ("http","https"):
            if base_domain and parsed.netloc == base_domain:
                internal_links +=1
            else:
                external_links +=1
        else:
            internal_links +=1
    return LinkResult(
        total_links = total_links,
        internal_links = internal_links,
        external_links = external_links,
        empty_links = empty_links,
        mailto_links = mailto_links,
        tel_links = tel_links,
    )