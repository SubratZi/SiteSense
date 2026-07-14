function ScreenshotCard({screenshot}) {
    if(!screenshot) return null;

    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
            }}
        >
            <h2>Website Screenshot</h2>
            <img src={`http://127.0.0.1:8000/${screenshot}`}
                alt = "Website Screenshot"
                style={{
                    width: "100%",
                    borderRadius: "8px",
                    border: "1px solid #ccc",
                }} 
            />
        </div>
    );
}

export default ScreenshotCard;