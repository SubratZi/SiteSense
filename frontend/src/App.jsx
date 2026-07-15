import "./App.css";
import { useState } from "react";
import api from "./api/api";
import AnalyzeForm from "./components/AnalyzeForm";
import ScoreCard from "./components/ScoreCard";
import RecommendationList from "./components/RecommendationList";
import ScreenshotCard from "./components/ScreenshotCard";
import SEOCard from "./components/SEOCard";
import TechnicalCard from "./components/TechnicalCard";
import OpenGraphCard from "./components/OpenGraphCard";
import ImagesCard from "./components/ImagesCard";
import LinksCard from "./components/LinksCard";
import Toast from "./components/Toast";

const FEATURES = [
  {title: "SEO ANALYSIS", desc: "Title, meta description, headings and word count checked instantly."},
  {title:"Performance", desc:"Response time measured and scored."},
  {title:"Image Audit",desc:"Finds images, missing alt text that affect SEO"},
  {title:"Link Analysis",desc:"Counts internal, external, empty and mailto links"},
  {title:"Technical Analysis",desc:"HTTPS, Viewport, Charset, Canonical URL, and robot tags are verified"},
  {title:"Open Graph",desc:"og:title, og:description, og: image and Twitter Card all are checked"},
  {title:"Screenshot",desc:"Full page screenshot of the analyzed page is captured"},
  {title:"Health Score",desc:"0-100 score is given along with letter grading as well as recommendations"},
]

function App(){
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [toasts, setToasts] = useState([]);

  function addToast(message, type = "error"){
    const id = Date.now();
    setToasts(prev => [...prev, {id, message, type}]);
    setTimeout(() => removeToast(id),5000);
  }

  function removeToast(id) {
    setToasts(prev => prev.filter(t => t.id !== id));
  }

  async function analyzeWebsite(url){
    try{
      setLoading(true);
      const response = await api.post("/analyze", {
        url,
      });
      setResult(response.data);
    } catch(error){
      addToast(
        error.response?.data?.detail ?? "Failed to analyze website",
        "error"
      );
    } finally{
      setLoading(false);
    }
  }
  return(
    <div className="app">
      <div className = "toast-container">
        {toasts.map(t => (
          <Toast 
          key = {t.id}
          message = {t.message}
          type = {t.type}
          onClose = {() => removeToast(t.id)}
          />
        ))}
      </div>
      <div className="header">
        <h1>SiteSense</h1>
        <p>
          Analyzes websites's SEO as well as issues in them, scores the performance and more.
        </p>
      </div>
      <AnalyzeForm 
        onAnalyze = {analyzeWebsite}
        loading = {loading}
      />
      {!result && !loading &&(
        <div className="landing">
          <div className="landing-left">
            <h2>Everything you need to audit a website</h2>
            <p>Paste URL and get Websites SEO Analayis in few seconds.</p>
            <p>Get Health Score of the Website and Recommendations.</p>
          </div>
          <div className="landing-right">
            <div classNam="feature-grid">
              {FEATURES.map((f,i)=> (
                <div className="feature-item" key = {i}>
                  <div>
                    <p className="feature-title">{f.title}</p>
                    <p className="feature-desc">{f.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      
      {result && (
        <div className= "results">
          <div className = "results-top">
            <ScoreCard score = {result.score} />
            <ScreenshotCard screenshot = {result.render.screenshot} />
          </div>

          <RecommendationList recommendations = {result.score.recommendations} />

          <div className = "results-grid">
            <SEOCard seo = {result.seo} />
            <TechnicalCard technical = {result.technical} />
            <OpenGraphCard opengraph = {result.opengraph} />
            <ImagesCard images = {result.images} />
            <LinksCard links = {result.links} />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;