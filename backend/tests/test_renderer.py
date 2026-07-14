import pytest

from auditor.renderer import(
    render,
    RenderResult,
    RenderError,
)

def test_render_returns_render_result():
    result = render("https://example.com")
    assert isinstance(result, RenderResult)
    assert result.status_code == 200
    assert result.url.startswith("https://example.com")
    assert isinstance(result.html, str)
    assert len(result.html) > 0
    assert isinstance(result.response_time, float)
    assert isinstance(result.headers, dict)
    assert result.screenshot.endswith(".png")

def test_render_result_fields():
    result = render("https://example.com")

    assert result.url.startswith("https://example.com")
    assert result.status_code == 200
    assert "<html" in result.html.lower()
    assert result.screenshot.endswith(".png")

def test_render_follows_redirects():
    result = render("https://google.com")

    assert result.url.startswith("https://")
    assert result.status_code == 200

def test_invalid_domain():
    with pytest.raises(RenderError):
        render("https://this-domain-does-not-exist-123456789.com")

def test_timeout_error():
    with pytest.raises(RenderError):
        render("https://10.255.255.1")

def test_cloudfare_protected_site():
    with pytest.raises(
        RenderError,
        match = "anti-bot",
    ):
        render("https://openai.com")