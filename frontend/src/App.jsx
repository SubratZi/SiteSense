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