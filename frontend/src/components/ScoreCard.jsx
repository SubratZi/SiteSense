const RADIUS = 54;
const CIRCUMFERENCE = 2* Math.PI * RADIUS;

function gradeColor(grade){
    return{
        A: "var(--green)",
        B: "#22c55e",
        C: "var(--amber)",
        D: "#f97316",
        E: "var(--red)",
    } [grade] ?? "var(--text-soft)";
}



function ScoreCard({ score }) {
    const pct = score.score /100;
    const offset = CIRCUMFERENCE * (1- pct);
    const color = gradeColor(score.grade);
    return (
        <div className="card score-card">
            <p className="card-title">Health Score</p>
            <div className = "score-ring-wrap">
                <svg className = "score-ring" viewBox= "0 0 120 120">
                    <circle
                        className = "score-ring-fill"
                        cx = "60" cy = "60" r= {RADIUS}
                        stroke = {color}
                        strokeDasharray = {CIRCUMFERENCE}
                        strokeDashoffset={offset}
                    />
                </svg>
                <div className="score-ring-text">
                    <span className="score-number">{score.score}</span>
                    <span className="score-label">/100</span>
                </div>
            </div>
            <span
             className = "score-grade"
             style = {{
                background: color + "20",
                color: color,
             }}
            >
                Grade {score.grade}
            </span>
        </div>
    );
}

export default ScoreCard;