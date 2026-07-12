from unittest.mock import Mock

import pytest
import requests

from auditor.fetcher import fetch, FetchError, FetchResult

def make_mock_response(url="https://example.com", status_code =200, text = "<html></html>", headers = None):
    mock = Mock()
    mock.url = url
    mock.status_code = status_code
    mock.text = text
    mock.headers = headers or {"Content-Type": "text/html"}
    return mock

def test_fetch_returns_fetch_result(mocker):
    mock_get = mocker.patch("requests.get", return_value = make_mock_response())
    result = fetch("https://example.com")
    assert isinstance(result, FetchResult)

    mock_get.assert_called_once_with(
        "https://example.com",
        headers={"User-Agent": "Mozilla/5.0 (compatible; SiteSense/1.0)"},
        timeout= 10,
        allow_redirects = True,
    )

def test_fetch_result_fields(mocker):
    mocker.patch("requests.get", return_value = make_mock_response(
        url="https://example.com/final",
        status_code = 200,
        text = "<html><body>hello</body></html>",
    ))
    result = fetch("https://example.com")
    assert result.url == "https://example.com/final"
    assert result.status_code == 200
    assert "hello" in result.html
    assert isinstance(result.response_time, float)
    assert result.response_time >=0
    assert result.headers["Content-Type"] == "text/html"

def test_fetch_follows_redirects(mocker):
    mocker.patch("requests.get", return_value = make_mock_response(
        url="https://www.example.com/"
    ))
    result = fetch("https://example.com")
    assert result.url == "https://www.example.com/"

def test_ssl_error(mocker):
    mocker.patch("requests.get", side_effect = requests.exceptions.SSLError)
    with pytest.raises(FetchError, match="SSL"):
        fetch("https://bad-cert.example.com")

def test_connect_timeout(mocker):
    mocker.patch("requests.get", side_effect= requests.exceptions.ConnectTimeout)
    with pytest.raises(FetchError, match="timed out"):
        fetch("https://slow.example.com")

def test_read_timeout(mocker):
    mocker.patch("requests.get", side_effect = requests.exceptions.ReadTimeout)
    with pytest.raises(FetchError, match="too long"):
        fetch("https://slow.example.com")

def test_connection_error(mocker):
    mocker.patch("requests.get", side_effect= requests.exceptions.ConnectionError)
    with pytest.raises(FetchError, match="connect"):
        fetch("https://unreachable.example.com")

def test_too_many_redirects(mocker):
    mocker.patch("requests.get", side_effect = requests.exceptions.TooManyRedirects)
    with pytest.raises(FetchError, match = "redirects"):
        fetch("https://redirect-loop.example.com")

def test_generic_request_exception(mocker):
    mocker.patch("requests.get", side_effect = requests.exceptions.RequestException("boom"))
    with pytest.raises(FetchError, match="Request failed"):
        fetch("https://example.com")