from auditor.technical import analyze_technical, TechnicalResult

def test_returns_technical_result():
    result = analyze_technical("<html></html>")
    assert isinstance(result, TechnicalResult)

def test_https_true():
    result = analyze_technical("", "https://example.com")
    assert result.has_https is True

def test_https_false():
    result = analyze_technical("", "https://exmaple.com")
    assert result.has_https is False

def test_lang_present():
    html = ' <html lang="en"></html>'
    result = analyze_technical(html)
    assert result.has_lang is True

def test_empty_lang():
    html = '<html lang =""></html>'
    result = analyze_technical(html)
    assert result.has_lang is False

def test_charset_present():
    html = '<meta charset= "UTF-8">'
    result = analyze_technical(html)
    assert result.has_charset is False

def test_viewport_present():
    html = """
    <meta name = "viewport"
        content = "width=device-width, initial-scale =1">
    """
    result = analyze_technical(html)
    assert result.has_viewport is True

def test_viewport_missing():
    result = analyze_technical("<html></html>")
    assert result.has_viewport is False

def test_canonical_present():
    html = """
    <link rel = "canonical" 
        href = "https://example.com">
    """
    result = analyze_technical(html)
    assert result.has_canonical is True

def test_canonical_missing():
    result = analyze_technical("<html></html>")

    assert result.has_canonical is False


def test_robots_present():
    html = """
    <meta name="robots"
          content="index,follow">
    """

    result = analyze_technical(html)

    assert result.has_robots is True


def test_robots_missing():
    result = analyze_technical("<html></html>")

    assert result.has_robots is False


def test_everything_present():
    html = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">
        <link rel="canonical"
              href="https://example.com">
        <meta name="robots"
              content="index,follow">
    </head>
    </html>
    """

    result = analyze_technical(html, "https://example.com")

    assert result.has_https is True
    assert result.has_lang is True
    assert result.has_charset is True
    assert result.has_viewport is True
    assert result.has_canonical is True
    assert result.has_robots is True


def test_empty_html():
    result = analyze_technical("")

    assert result.has_lang is False
    assert result.has_charset is False
    assert result.has_viewport is False
    assert result.has_canonical is False
    assert result.has_robots is False