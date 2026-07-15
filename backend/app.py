from fastapi import FastAPI, HTTPException
from schemas import AuditRequest
from auditor.analyzer import analyze
from auditor.renderer import RenderError
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app =  FastAPI(
    title="SiteSense API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173",
        "sitesenseseo.vercel.app",
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

app.mount("/screenshots",
          StaticFiles(directory="screenshots"),
          name="screenshots",
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
    except RenderError as e:
        raise HTTPException(
            status_code = 400,
            detail = str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail =  str(e),
        )