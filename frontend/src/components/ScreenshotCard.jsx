function ScreenshotCard({screenshot}) {
    const API_URL = import.meta.env.VITE_API_URL;
    if(!screenshot) return null;

    return (
        <div className = "card">
            <p className = "card-title"> Screenshot</p>
            <img 
                className = "screenshot-img" 
                src={`${API_URL}/${screenshot}`}
                alt = "Website Screenshot" 
            />
        </div>
    );
}

export default ScreenshotCard;