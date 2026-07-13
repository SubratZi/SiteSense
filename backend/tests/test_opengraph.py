from auditor.opengraph import analyze_opengraph, OpenGraphResult

def test_returns_opengraph_result():
    result = analyze_opengraph("<html></html>")
    assert isinstance(result, OpenGraphResult)

def test_og_title():
    html = '<meta property="og:title" content= "My Website">'
    result = analyze_opengraph(html)
    assert result.og_title == "My Website"

def test_og_description():
    html = '<meta property= "og:description" content = "Best site ever">'
    result = analyze_opengraph(html)
    assert result.og_description == "Best site ever"

def test_og_image():
    html = '<meta property = "og:image"  content = "image.jpg"'
    result = analyze_opengraph(html)
    assert result.og_image == "image.jpg"

def test_og_url():
    html = '<meta property="og:url" content = "https://example.com">'
    result = analyze_opengraph(html)
    assert result.og_url == "https://example.com"

def test_twitter_card():
    html = '<meta name = "twitter:card" content = "summary_large_image">'
    result = analyze_opengraph(html)
    assert result.twitter_card == "summary_large_image"

def test_case_insensitive():
    html = """
    <meta PROPERTY="OG:TITLE" content = "Hello">
    <meta NAME="TWITTER:CARD" content = "summary">
    """

    result = analyze_opengraph(html)
    assert result.og_title == "Hello"
    assert result.twitter_card == "summary"

def test_empty_content():
    html = '<meta property = "og:title" content="">'
    result = analyze_opengraph(html)
    assert result.og_title is None

def test_missing_tags():
    result = analyze_opengraph("<html></html>")
    assert result.og_title is None
    assert result.og_description is None
    assert result.og_image is None
    assert result.og_url is None
    assert result.twitter_card is None

def test_all_tags():
    html = """
    <meta property="og:title" content="SiteSense">
    <meta property="og:description" content="SEO Tool">
    <meta property="og:image" content="image.png">
    <meta property="og:url" content="https://sitesense.com">
    <meta name="twitter:card" content="summary_large_image">
    """

    result = analyze_opengraph(html)

    assert result.og_title == "SiteSense"
    assert result.og_description == "SEO Tool"
    assert result.og_image == "image.png"
    assert result.og_url == "https://sitesense.com"
    assert result.twitter_card == "summary_large_image"


def test_empty_html():
    result = analyze_opengraph("")

    assert result.og_title is None
    assert result.og_description is None
    assert result.og_image is None
    assert result.og_url is None
    assert result.twitter_card is None