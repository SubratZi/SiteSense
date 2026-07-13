from fastapi import FastAPI, HTTPException
from schemas import AuditRequest
from auditor.analyzer import analyze
from auditor.fetcher import FetchError

app =  FastAPI(
    title="SiteSense API",
    version="1.0.0",
)

@app.get("/")
def root():
    return{
        "message": "Welcome to SiteSense API!"
    }

@app.post("/analyze")
def analyze_site(request: AuditRequest):
    try:
        result = analyze(str(request.url))
        return result
    except FetchError as e:
        raise HTTPException(
            status_code = 400,
            detail = str(e),
        )
    except Exception:
        raise HTTPException(
            status_code = 500,
            detail = "Internal Server Error",
        )