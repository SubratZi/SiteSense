from dataclasses import dataclass

from auditor.seo import SEOResult
from auditor.images import ImageResult
from auditor.links import LinkResult
from auditor.links import TechnicalResult
from auditor.technical import OpenGraphResult

@dataclass
class ScoreResult:
    score:int
    grade:str
    recommendations:list[str]

def calculate_score(
        seo:SEOResult,
        images: ImageResult,
        links: LinkResult,
        technical:TechnicalResult,
        opengraph: OpenGraphResult,
) -> ScoreResult:
    score = 100
    recommendations = []

    if seo.title is None:
        score -=10
        recommendations.append("Add a page title.")
    
    elif not (30  <= seo.title_length <=60):
        score -=5
        recommendations.append(
            "Keep the title between 30 and 60 characters."
        )
    
    if seo.meta_description is None:
        score -=10
        recommendations.append("Add a meta description")

    elif not(120<= seo.meta_description_length <= 160):
        score -= 5
        recommendations.append(
            "Keep the meta description between 120 and 160 characters."
        )
    
    if seo.h1_count ==0:
        score -=5
        recommendations.append(
            "Add an H1 heading."
        )
    elif seo.h1_count > 1:
        score -=3
        recommendations.append("Use only one H1 heading.")
    
    if seo.word_count < 300:
        score -=5
        recommendations.append(
            "Increase page content to at least 300 words."
        )

    if images.missing_alt > 0:
        score -= min(images.missing_alt *2, 10)
        recommendations.append(
            f"Add alt text to {images.missing_alt} image(s) ."
        )
    
    if not technical.has_https:
        score -=10
        recommendations.append("Use HTTPS.")
    
    if not technical.has_lang:
        score -=3
        recommendations.append("Add a language attribute to the HTML tag.")
    
    if not technical.has_charset:
        score -=3
        recommendations.append("Add a charset meta tag.")

    if not technical.has_viewport:
        score -=5
        recommendations.append("Add a viewport meta tag.")
    
    if not technical.has_canonical:
        score -=5
        recommendations.append("Add a canonical URL.")
    
    if not technical.has_robots:
        score -=2
        recommendations.append("Add a robots meta tag.")

    if opengraph.og_title is None:
        score -=2 
        recommendations.append("Add og:title.")
    
    if opengraph.og_description is None:
        score -=2
        recommendations.append("Add og:description.")
    
    if opengraph.og_image is None:
        score -=2
        recommendations.append("Add og:image.")
    
    if opengraph.twitter_card is None:
        score -=2
        recommendations.append("Add a Twitter Card.")
    
    score = max(score, 0)

    if score >= 90:
        grade = "A"
    
    elif score >= 80:
        grade = "B"
    
    elif score >=70:
        grade = "C"
    
    elif score >=60:
        grade = "D"

    else:
        grade = "E"
    
    return ScoreResult(
        score = score,
        grade = grade,
        recommendations =recommendations,
    )