function ScreenshotCard({screenshot}) {
    if(!screenshot) return null;

    return (
        <div className = "card">
            <p className = "card-title"> Screenshot</p>
            <img 
                className = "screenshot-img" 
                src={`http://127.0.0.1:8000/${screenshot}`}
                alt = "Website Screenshot" 
            />
        </div>
    );
}

export default ScreenshotCard;