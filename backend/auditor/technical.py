from dataclasses import dataclass
import re
from bs4 import BeautifulSoup 

@dataclass

class TechnicalResult:
    has_https: bool
    has_lang: bool
    has_charset: bool
    has_viewport: bool
    has_canonical: bool
    has_robots: bool

def analyze_technical(html:str, url: str = "") -> TechnicalResult:
    soup = BeautifulSoup(html, "lxml")
    has_https = url.lower().startswith("https://")
    html_tag = soup.find("html")

    has_lang = (
        html_tag is not None
        and html_tag.has_attr("lang")
        and html_tag['lang'].strip() != ""
    )
    has_charset = soup.find("meta", charset = True) is not None

    has_viewport = (
        soup.find("meta", attrs = {"name": re.compile(r"^viewport$",re.I)}) is not None
    )

    has_canonical= (
        soup.find("link", attrs = {"rel":re.compile(r"^canonical$",re.I)}) is not None
    )
    has_robots = (
        soup.find("meta", attrs= {"name": re.compile(r"^robots$", re.I)}) is not None
    )

    return TechnicalResult(
        has_https = has_https,
        has_lang = has_lang,
        has_charset = has_charset,
        has_viewport = has_viewport,
        has_canonical = has_canonical,
        has_robots = has_robots,
    )
