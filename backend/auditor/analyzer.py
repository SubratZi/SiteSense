from dataclasses import dataclass
from auditor.fetcher import fetch, FetchResult
from auditor.seo import analyze_seo, SEOResult
from auditor.images import analyze_images, ImageResult
from auditor.links  import analyze_links, LinkResult
from auditor.technical import analyze_technical, TechnicalResult
from auditor.opengraph import analyze_opengraph, OpenGraphResult
from auditor.scorer import calculate_score, ScoreResult

@dataclass
class AuditResult:
    fetch: FetchResult
    seo: SEOResult
    images: ImageResult
    links: LinkResult
    technical: TechnicalResult
    opengraph: OpenGraphResult
    score: ScoreResult

def analyze(url: str) -> AuditResult:
    fetch_result = fetch(url)
    html = fetch_result.html
    seo_result = analyze_seo(html)
    images_result = analyze_images(html)
    links_result = analyze_links(html, fetch_result.url)
    technical_result = analyze_technical(
        html,
        fetch_result.url,
    )

    opengraph_result = analyze_opengraph(html)
    score_result = calculate_score(
        seo = seo_result,
        images = images_result,
        links = links_result,
        technical=technical_result,
        opengraph = opengraph_result,
    )
    return AuditResult(
        fetch = fetch_result,
        seo = seo_result,
        images = images_result,
        links=links_result,
        technical=technical_result,
        opengraph=opengraph_result,
        score= score_result,
    )