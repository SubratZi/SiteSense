function SEOCard({seo}) {
    return (
        <div 
            style ={{
               border: "1px solid #ddd",
               borderRadius: "10px",
               padding: "20px",
               marginTop: "20px", 
            }}
            >
                <h2> SEO Analysis </h2>
                <p><strong>Title:</strong>{seo.title ?? "Not Found"}</p>
                <p><strong>Title Length:</strong> {seo.title_length}</p>
                <p>
                    <strong>Meta Description:</strong>{" "}
                    {seo.meta_description ?? "Not Found"}
                </p>
                <p>
                    <strong>Meta Description Length:</strong>{" "}
                    {seo.meta_description_length}
                </p>
                <p><strong>H1 Count:</strong> {seo.h1_count}</p>
                <p><strong>H2 Count:</strong> {seo.h2_count}</p>
                <p><strong>Word Count:</strong>{seo.word_count}</p>
            </div>
    );
}

export default SEOCard;