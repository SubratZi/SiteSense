# SiteSense

## Folder Structure

```
SiteSense/
│
├── backend/
│   │
│   ├── app.py                    
│   ├── requirements.txt          
│   │
│   ├── auditor/                  
│   │   ├── __init__.py
│   │   ├── analyzer.py           
│   │   ├── fetcher.py            
│   │   ├── seo.py                
│   │   ├── images.py             
│   │   ├── links.py              
│   │   ├── technical.py          
│   │   ├── opengraph.py           
│   │   └── scorer.py             
│   │
│   ├── tests/                    
│   │   ├── test_fetcher.py
│   │   ├── test_seo.py
│   │   ├── test_images.py
│   │   ├── test_links.py
│   │   ├── test_technical.py
│   │   ├── test_opengraph.py
│   │   ├── test_scorer.py
│   │   └── test_analyzer.py
│   │   ├── test_api.py
│   │
│   └── static/  
│   │   ├──index.html
│   │   ├──script.js
│   │   ├──style.css           
│   |
├── .gitignore
├── README.md
└── LICENSE
```