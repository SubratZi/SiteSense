from auditor.links import analyze_links, LinkResult

def test_returns_link_result():
    result = analyze_links("<html></html>")
    assert isinstance(result, LinkResult)

def test_no_link():
    result = analyze_links("<html><body><p>Hello</p></body></html>")

    assert result.total_links == 0
    assert result.internal_links ==0
    assert result.external_links ==0
    assert result.empty_links ==0
    assert result.mailto_links ==0
    assert result.tel_links ==0

def test_no_links():
    result = analyze_links("<html><body><p>Hello</p></body></html>")

    assert result.total_links ==0
    assert result.internal_links ==0
    assert result.external_links ==0
    assert result.empty_links ==0
    assert result.mailto_links ==0
    assert result.tel_links ==0


def test_internal_relative_link():
    html = '<a href ="/about">About</a>'

    result = analyze_links(html)

    assert result.total_links == 1
    assert result.internal_links ==1

def test_internal_absoulute_link():
    html = '<a href="https://example.com/about">About</a>'

    result = analyze_links(html, base_url = "https://example.com")

    assert result.internal_links ==1
    assert result.external_links ==0

def test_external_link():
    html = '<a href="https://google.com">Google</a>'c

    result = analyze_links(html, base_url = "https:// example.com")

    assert result.external_links ==1 
    assert result.internal_links ==0

def test_empty_href():
    html = '<a href="">Empty</a>'

    result = analyze_links(html)

    assert result.empty_links == 1


def test_missing_href():
    html = "<a>Home</a>"

    result = analyze_links(html)

    assert result.empty_links == 1


def test_mailto_link():
    html = '<a href="mailto:test@example.com">Email</a>'

    result = analyze_links(html)

    assert result.mailto_links == 1


def test_tel_link():
    html = '<a href="tel:+9779800000000">Call</a>'

    result = analyze_links(html)

    assert result.tel_links == 1


def test_multiple_links():
    html = """
    <a href="/home">Home</a>
    <a href="https://google.com">Google</a>
    <a href="">Empty</a>
    <a>Email</a>
    <a href="mailto:test@example.com">Mail</a>
    <a href="tel:+123456789">Phone</a>
    """

    result = analyze_links(html, base_url="https://example.com")

    assert result.total_links == 6
    assert result.internal_links == 1
    assert result.external_links == 1
    assert result.empty_links == 2
    assert result.mailto_links == 1
    assert result.tel_links == 1


def test_empty_html():
    result = analyze_links("")

    assert result.total_links == 0
    assert result.internal_links == 0
    assert result.external_links == 0
    assert result.empty_links == 0