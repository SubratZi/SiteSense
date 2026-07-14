function ImagesCard({ images }) {
    return (
        <div
            style = {{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
            }}
        >
            <h2>Images</h2>
            <p><strong>Total Images:</strong>{images.total_images}</p>
            <p><strong>Images with Alt:</strong>{images.images_with_alt}</p>
            <p><strong>Missing Alt:</strong>{images.missing_alt}</p>
            <p><strong>Empty Alt:</strong>{images.images_with_alt}</p>
        </div>
    );
}

export default ImagesCard;