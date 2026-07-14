function ScoreCard({ score }) {
    return (
        <div className="card">
            <h2>Overall Score</h2>
            <h1>{score.score}/100</h1>
            <h3>Grade: {score.grade}</h3>
        </div>
    );
}

export default ScoreCard;