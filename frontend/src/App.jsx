import { useState } from "react";
import api from "./api/api";
import AnalyzeForm from "./components/AnalyzeForm";

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
        <pre style= {{
          marginTop:30,
          background: "#eee",
          padding:20,
          overflowX: "auto",
        }}
        >
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;