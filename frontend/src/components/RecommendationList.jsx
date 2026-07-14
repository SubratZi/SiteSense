function RecommendationList ({ recommendations }) {
    return (
        <div style = {{
            border: "1px solid #ddd",
            borderRadius: "10px",
            padding: "20px",
            marginTop: "20px",
        }}
        >
        <h2>Recommendations</h2>
        {recommendations.length === 0 ? (
            <p>All good. Your website's already great</p>
        ): (
            <ul>
                {recommendations.map((item, index) => (
                    <li key = {index}>{item}</li>
                ))}
            </ul>
        )}
    </div>
    );
}

export default RecommendationList;