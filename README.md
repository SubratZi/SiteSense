# SiteSense

## Folder Structure

```text
SiteSense/
├── backend/
│   ├── auditor/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   ├── images.py
│   │   ├── links.py
│   │   ├── opengraph.py
│   │   ├── renderer.py
│   │   ├── scorer.py
│   │   ├── seo.py
│   │   └── technical.py
│   ├── screenshots/
│   ├── tests/
│   ├── app.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   │   └── api.js
│   │   ├── components/
│   │   │   ├── AnalyzeForm.jsx
│   │   │   ├── ImagesCard.jsx
│   │   │   ├── LinksCard.jsx
│   │   │   ├── OpenGraphCard.jsx
│   │   │   ├── RecommendationList.jsx
│   │   │   ├── ScoreCard.jsx
│   │   │   ├── ScreenshotCard.jsx
│   │   │   ├── SEOCard.jsx
│   │   │   ├── TechnicalCard.jsx
│   │   │   └── Toast.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── LICENSE
└── README.md
```