import re
from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class SEOResult:
    title: str| None
    title_length: int
    meta_description: str|None
    meta_description_length: int
    h1_count: int
    h2_count: int
    word_count: int

def analyze_seo(html: str) -> SEOResult:
    soup = BeautifulSoup(html, "lxml")

    title_tag = soup.find("title")
    title = title_tag.get_text(strip = True) if title_tag else None
    title = title if title else None

    meta_tag = soup.find("meta", attrs={"name":re.compile(r"^description$", re.I)})
    meta_description = None
    if meta_tag:
        content = meta_tag.get("content", "").strip()
        meta_description = content if content else None

    h1_count = len(soup.find_all("h1"))
    h2_count = len(soup.find_all("h2"))

    for tag in soup (["script", "style", "noscript"]):
        tag.decompose()
        
    words = re.findall(r"[A-Za-z0-9']+", soup.get_text(separator=" "))
    word_count = len(words)

    return SEOResult(
        title = title,
        title_length = len(title) if title else 0,
        meta_description = meta_description,
        meta_description_length = len(meta_description) if meta_description else 0,
        h1_count = h1_count,
        h2_count = h2_count,
        word_count = word_count,
    )