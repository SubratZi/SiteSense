from dataclasses import dataclass

from auditor.renderer import render, RenderResult
from auditor.seo import analyze_seo, SEOResult
from auditor.images import analyze_images, ImageResult
from auditor.links import analyze_links, LinkResult
from auditor.technical import analyze_technical, TechnicalResult
from auditor.opengraph import analyze_opengraph, OpenGraphResult
from auditor.scorer import calculate_score, ScoreResult


@dataclass
class AuditResult:
    render: RenderResult
    seo: SEOResult
    images: ImageResult
    links: LinkResult
    technical: TechnicalResult
    opengraph: OpenGraphResult
    score: ScoreResult


def analyze(url: str) -> AuditResult:

    render_result = render(url)

    html = render_result.html

    seo_result = analyze_seo(html)

    images_result = analyze_images(html)

    links_result = analyze_links(
        html,
        render_result.url,
    )

    technical_result = analyze_technical(
        html,
        render_result.url,
    )

    opengraph_result = analyze_opengraph(html)


    score_result = calculate_score(
        seo=seo_result,
        images=images_result,
        links=links_result,
        technical=technical_result,
        opengraph=opengraph_result,
    )


    return AuditResult(
        render=render_result,
        seo=seo_result,
        images=images_result,
        links=links_result,
        technical=technical_result,
        opengraph=opengraph_result,
        score=score_result,
    )