function OpenGraphCard({opengraph}) {
    return(
        <div
            style = {{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
            }}
        >
            <h2>Open Graph</h2>
            <p>
                <strong>OG Title:</strong>{" "}
                {opengraph.og_title ?? "Not Found"}
            </p>
            <p>
                <strong>OG Description:</strong>{" "}
                {opengraph.og_description >> "Not Found"}
            </p>
            <p>
                <strong>OG Image:</strong>{" "}
                {opengraph.og_image ?? "Not Found"}
            </p>
            <p>
                <strong>OG URL:</strong>{" "}
                {opengraph.og_url ?? "Not Found"}
            </p>
            <p>
                <strong>Twitter Card:</strong>{" "}
                {opengraph.twitter_card ?? "Not Found"}
            </p>
        </div>
    );
}

export default OpenGraphCard;