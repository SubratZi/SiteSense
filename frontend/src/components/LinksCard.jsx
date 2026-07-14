function LinksCard({links}) {
    return(
        <div
            style = {{
                border: "1px solid #ddd",
                borderRadius:"10px",
                padding: "20px",
                marginTop: "20px",
            }}
        >
            <h2>Links</h2>
            <p><strong>Total Links:</strong>{links.total_links}</p>
            <p><strong>Internal Links:</strong>{links.internal_links}</p>
            <p><strong>External Links:</strong>{links.external_links}</p>
            <p><strong>Empty Links:</strong>{links.empty_links}</p>
            <p><strong>Mailto Links:</strong>{links.mailto_links}</p>
            <p><strong>Telephone Links:</strong>{links.tel_links}</p>
        </div>
    );
}

export default LinksCard;