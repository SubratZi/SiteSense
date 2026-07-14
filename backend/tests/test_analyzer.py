from auditor.analyzer import analyze, AuditResult
from auditor.fetcher import FetchResult

def make_fetch_result():
    html = """
    <html lang="en">
    <head>
            <title>Example Site</title>

            <meta name="description"
                  content="This is an example description that is comfortably over 120 characters. Lorem ipsum dolor sit amet, consectetur adipiscing elitumai kumaiwd.. SEO analyzer! This is just for the test of the characters.">

            <meta charset="UTF-8">

            <meta name="viewport"
                  content="width=device-width, initial-scale=1">

            <meta property="og:title"
                  content="Example Site">

            <meta property="og:description"
                  content="Example Description">

            <meta property="og:image"
                  content="image.jpg">

            <meta property="og:url"
                  content="https://example.com">

            <meta name="twitter:card"
                  content="summary_large_image">

            <link rel="canonical"
                  href="https://example.com">

            <meta name="robots"
                  content="index,follow">
        </head>

        <body>
            <h1>Hello</h1>

            <img src="dog.jpg" alt="Dog">

            <a href="/about">About</a>

            <p>
                {}
            </p>
        </body>
    </html>

    """.format("word "*400)
    return FetchResult(
        url="https://example.com",
        status_code=200,
        html=html,
        response_time=0.25,
        headers={"Content-Type": "text/html"},
    )

def mock_dependencies(mocker):
    mocker.patch(
        "auditor.analyzer.fetch",
        return_value = make_fetch_result(),
    )
    mocker.patch(
        "auditor.analyzer.take_screenshot",
        return_value = "screenshots/example.png",
    )


def test_returns_audit_result(mocker):
    mock_dependencies(mocker)

    result = analyze("https://example.com")
    assert isinstance(result, AuditResult)

def test_fetch_information(mocker):
    mock_dependencies(mocker)
    result = analyze("https://example.com")
    assert result.fetch.status_code == 200
    assert result.fetch.url =="https://example.com"
    assert result.fetch.response_time == 0.25
    assert result.fetch.headers["Content-Type"] == "text/html"
    

def test_contains_all_results(mocker):
    mock_dependencies(mocker)
    result = analyze("https://example.com")

    assert result.seo.title == "Example Site"
    assert result.images.total_images ==1
    assert result.links.total_links ==1
    assert result.technical.has_https is True
    assert result.opengraph.og_title == "Example Site"

def test_score_is_generated(mocker):
    mock_dependencies(mocker)
    result = analyze("https://example.com")
    assert result.score.score >=0
    assert result.score.score <=100
    assert result.score.grade in ["A", "B", "C", "D", "E"]

def test_fetch_called_once(mocker):
    mocked = mocker.patch(
        "auditor.analyzer.fetch",
        return_value = make_fetch_result(),
        )
    
    mocker.patch(
        "auditor.analyzer.take_screenshot",
        return_value = "screenshots/example.png",
    )
    
    analyze("https://example.com")
    mocked.assert_called_once_with("https://example.com")

def test_screenshot_is_generated(mocker):
    mock_dependencies(mocker)
    result = analyze("https://example.com")
    assert result.screenshot == "screenshots/example.png"