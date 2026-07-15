function TechnicalCard({technical}) {
    return(
        <div
            style= {{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
            }}
        >
            <h2>Technical Analysis</h2>
            <p> 
                <strong>HTTPS:</strong>{" "}
                {technical.has_https? "Yes": "No"}
            </p>

            <p>
                <strong>Language Attribute:</strong>{" "}
                {technical.has_lang ? "Yes" : "No"}
            </p>

            <p>
                <strong>Charset:</strong>{" "}
                {technical.has_charset? "Yes": "No"}
            </p>

            <p>
                <strong>Viewport:</strong>{" "}
                {technical.has_viewport ? "Yes": "No"}
            </p>

            <p>
                <strong>Canonical URL:</strong>{" "}
                {technical.has_canonical ? "Yes": "No"}
            </p>

            <p>
                <strong>Robots Tag:</strong> {" "}
                {technical.has_robots ? "Yes" : "No"}
            </p>
        </div>
    );
}

export default TechnicalCard;