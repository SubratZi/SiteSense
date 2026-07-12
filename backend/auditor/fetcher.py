import time
from dataclasses import dataclass

import requests

USER_AGENTS = "Mozilla/5.0 (compatible; SiteSense/1.0)"
TIMEOUT = 10

class FetchError(Exception):
    """Raised when a URL cannot be fetched due to any reason."""
    pass

@dataclass
class FetchResult:
    url:str
    status_code: int
    html: str
    response_time: float
    headers:dict

def fetch(url:str) -> FetchResult:
    """
    Fetch a URL and return a Fetched Result!
    Raises FetchError with a readable message on any failure.
    """
    try:
        start = time.time()
        resp = requests.get(
            url,
            headers={"User-Agent": USER_AGENTS},
            timeout=TIMEOUT,
            allow_redirects=True,
        )
        response_time = round(time.time()-start, 3)
    except requests.exceptions.SSLError:
        raise FetchError("SSL error: Site's HTTPS certificate couldnt be verified")
    except requests.exceptions.ConnectTimeout:
        raise FetchError("connection timed out")
    except requests.exceptions.ReadTimeout:
        raise FetchError("The site took too long to respond")
    except requests.exceptions.ConnectionError:
        raise FetchError("Couldnt connect. Check the URL and try again.")
    except requests.exceptions.TooManyRedirects:
        raise FetchError("Too many redirects")
    except requests.exceptions.RequestException as e:
        raise FetchError(f"Request failed: {e}")
    
    return FetchResult(
        url=resp.url,
        status_code=resp.status_code,
        html=resp.text,
        response_time = response_time,
        headers = dict(resp.headers),
    )