function SEOCard({seo}) {
    const titleOk = seo.title && seo.title_length >=30 && seo.length <=60;
    const metaOk = seo.meta_description && seo.meta_description_length >=120 && seo.meta_description_length <=160;
    return (
        <div className= "card">
            <p className = "card-title">SEO</p>
            <ul className = "kv-list">
                <li className = "kv-row">
                    <span className= "kv-label">Title length</span>
                    <span className = "kv-value">{seo.title ?? "-"}</span>
                </li>
                <li className = "kv-row">
                    <span className = "kv-label">Title length</span>
                    <span className = {`badge ${titleOk ? "pass":"fail"}`}>
                        {seo.title_length} chars
                    </span>
                </li>
                <li className = "kv-row">
                    <span className = "kv-label">Meta description</span>
                    <span className = "kv-value">{seo.meta_description ?? "-"}</span>
                </li>
                <li className = "kv-row">
                    <span className = "kv-label">Meta length</span>
                    <span className = {`badge ${metaOk ? "pass" : "fail"}`}>
                        {seo.meta_description_length} chars
                    </span>
                </li>
                <li className = "kv-row">
                    <span className = "kv-row">H1 Count</span>
                    <span className = {`badge ${seo.h1_count === 1 ? "pass" : "fail"}`}>{seo.h1_count}</span>
                </li>
                <li className = "kv-row">
                    <span className = "kv-label">H2 count</span>
                    <span className = {`badge ${seo.word_count >=300 ? "pass" :"warn"}`}>{seo.word_count} words</span>
                </li>
            </ul>
        </div>
    );
}

export default SEOCard;