function ScoreCard({ score }) {
    return (
        <div 
            style = {{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "25px",
            }}
        >
            <h2>Overall Score</h2>
            <h1>{score.score}/100</h1>
            <h3>Grade: {score.grade}</h3>
        </div>
    );
}

export default ScoreCard;