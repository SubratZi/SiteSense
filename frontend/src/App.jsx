import { useState } from "react";
import api from "./api/api";
import AnalyzeForm from "./components/AnalyzeForm";
import ScoreCard from "./components/ScoreCard";
import RecommendationList from "./components/RecommendationList";
import ScreenshotCard from "./components/ScreenshotCard";
import SEOCard from "./components/SEOCard";
import TechnicalCard from "./components/TechnicalCard";

function App(){
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function analyzeWebsite(url){
    try{
      setLoading(true);
      const response = await api.post("/analyze", {
        url,
      });
      setResult(response.data);
    } catch(error){
      alert(
        error.response?.data?.detail ??
        "Failed to analyze website."
      );
    } finally{
      setLoading(false);
    }
  }
  return(
    <div style={{padding: "40px"}}>
      <h1>SiteSense</h1>
      <AnalyzeForm 
        onAnalyze = {analyzeWebsite}
        loading = {loading}
      />

      {result && (
        <>
          <ScoreCard score = {result.score} />
          <RecommendationList
            recommendations = {result.score.recommendations}
          />
          <ScreenshotCard
            screenshot={result.screenshot}
          />
          <SEOCard seo={result.seo} />
          <TechnicalCard technical={result.technical} />

          <pre style= {{
            marginTop:30,
            background: "#eee",
            padding:20,
            overflowX: "auto",
          }}
        >
          {JSON.stringify(result, null, 2)}
        </pre>
        </>
      )}
    </div>
  );
}

export default App;