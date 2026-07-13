from auditor.scorer import calculate_score, ScoreResult
from auditor.seo import SEOResult
from auditor.images import ImageResult
from auditor.links import LinkResult
from auditor.technical import TechnicalResult
from auditor.opengraph import OpenGraphResult

def make_good_seo():
    return SEOResult(
        title = "A" * 40,
        title_length = 40,
        meta_description = "A" * 140,
        meta_description_length = 140,
        h1_count = 1,
        h2_count = 2,
        word_count = 500,
    )

def make_good_images():
    return ImageResult(
        tota_images = 5,
        images_with_alt=5,
        missing_alt=0,
        empty_alt =0,
    )

def make_good_links():
    return LinkResult(
        total_links = 10,
        internal_links =3,
        external_links =3,
        empty_links =0,
        mailto_links =0,
        tel_links=0,
    )

def make_good_technical():
    return TechnicalResult(
        has_https = True,
        has_lang = True,
        has_charset = True,
        has_viewport = True,
        has_canonical=True,
        has_robots = True,
    )

def make_good_opengraph():
    return OpenGraphResult(
        og_title = "Example",
        og_description = "Description",
        og_image = "image.jpg",
        og_url= "https://example.com",
        twitter_card="summary_large_image",
    )

def test_returns_score_result():
    result = calculate_score(
        make_good_seo(),
        make_good_images(),
        make_good_links(),
        make_good_technical(),
        make_good_opengraph(),
    )

    assert isinstance(result, ScoreResult)

def test_perfect_score():
    result = calculate_score(
        make_good_seo(),
        make_good_images(),
        make_good_links(),
        make_good_technical(),
        make_good_opengraph(),
    )

    assert result.score ==100
    assert result.grade == "A"
    assert result.recommendations == []

def test_missing_title():
    seo = make_good_seo()
    seo.title = None
    seo.title_length = 0

    result = calculate_score(
        seo,
        make_good_images(),
        make_good_links(),
        make_good_technical(),
        make_good_opengraph(),
    )

    assert result.score < 100
    assert "title" in result.recommendations[0].lower()

def test_missing_meta_description():
    seo = make_good_seo()
    seo.meta_description = None
    seo.meta_description_length = 0

    result = calculate_score(
        seo,
        make_good_images(),
        make_good_links(),
        make_good_technical(),
        make_good_opengraph(),
    )

    assert result.score < 100
    assert any("meta description" in r.lower() for r in result.recommendations)


def test_missing_alt_text():
    images = make_good_images()
    images.missing_alt = 3

    result = calculate_score(
        make_good_seo(),
        images,
        make_good_links(),
        make_good_technical(),
        make_good_opengraph(),
    )

    assert result.score < 100
    assert any("alt" in r.lower() for r in result.recommendations)


def test_missing_https():
    technical = make_good_technical()
    technical.has_https = False

    result = calculate_score(
        make_good_seo(),
        make_good_images(),
        make_good_links(),
        technical,
        make_good_opengraph(),
    )

    assert result.score < 100
    assert any("https" in r.lower() for r in result.recommendations)


def test_missing_open_graph():
    og = make_good_opengraph()
    og.og_title = None
    og.og_description = None

    result = calculate_score(
        make_good_seo(),
        make_good_images(),
        make_good_links(),
        make_good_technical(),
        og,
    )

    assert result.score < 100
    assert any("og:title" in r.lower() for r in result.recommendations)


def test_grade_f():
    seo = SEOResult(
        title=None,
        title_length=0,
        meta_description=None,
        meta_description_length=0,
        h1_count=0,
        h2_count=0,
        word_count=10,
    )

    images = ImageResult(
        total_images=10,
        images_with_alt=0,
        missing_alt=10,
        empty_alt=0,
    )

    technical = TechnicalResult(
        has_https=False,
        has_lang=False,
        has_charset=False,
        has_viewport=False,
        has_canonical=False,
        has_robots=False,
    )

    og = OpenGraphResult(
        og_title=None,
        og_description=None,
        og_image=None,
        og_url=None,
        twitter_card=None,
    )

    result = calculate_score(
        seo,
        images,
        make_good_links(),
        technical,
        og,
    )

    assert result.grade == "F"


def test_score_never_negative():
    seo = SEOResult(
        title=None,
        title_length=0,
        meta_description=None,
        meta_description_length=0,
        h1_count=0,
        h2_count=0,
        word_count=0,
    )

    images = ImageResult(
        total_images=100,
        images_with_alt=0,
        missing_alt=100,
        empty_alt=100,
    )

    technical = TechnicalResult(
        has_https=False,
        has_lang=False,
        has_charset=False,
        has_viewport=False,
        has_canonical=False,
        has_robots=False,
    )

    og = OpenGraphResult(
        og_title=None,
        og_description=None,
        og_image=None,
        og_url=None,
        twitter_card=None,
    )

    result = calculate_score(
        seo,
        images,
        make_good_links(),
        technical,
        og,
    )

    assert result.score == 0