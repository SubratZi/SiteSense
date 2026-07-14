import { useState } from "react";
function AnalyzeForm({ onAnalyze, loading }){
    const [url, setUrl] = useState("");

    function handleSubmit(e) {
        e.preventDefault();
        if(!url.trim()) return;

        onAnalyze(url);
    }

    return(
        <form onSubmit={handleSubmit}>
            <input
                type="url"
                placeholder="https://example.com"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                required
            />
            <button type="submit" disabled={loading}>
                {loading ? "Analyzing..." : "Analyze"}
            </button>
        </form>
    );
}

export default AnalyzeForm;