function RecommendationList ({ recommendations }) {
    return (
        <div className = "card">
            <p className= "card-title">Recommendations</p>
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