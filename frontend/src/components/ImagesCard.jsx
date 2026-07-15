function ImagesCard({ images }) {
    const total = images.total_images;
    const withAlt = images.images_with_alt;
    const coverage = total > 0 ? Math.round((withAlt / total) * 100) : 100;
    const barColor = coverage === 100
        ? "var(--green)"
        : coverage >= 50
        ? "var(--amber)"
        : "var(--red)";
    return (
    <div className="card">
      <p className="card-title">Images</p>
      <ul className="kv-list">
        <li className="kv-row">
          <span className="kv-label">Total images</span>
          <span className="kv-value">{total}</span>
        </li>
        <li className="kv-row">
          <span className="kv-label">With alt text</span>
          <span className="kv-value">{withAlt}</span>
        </li>
        <li className="kv-row">
          <span className="kv-label">Missing alt</span>
          <span className={`badge ${images.missing_alt === 0 ? "pass" : "fail"}`}>
            {images.missing_alt}
          </span>
        </li>
        <li className="kv-row">
          <span className="kv-label">Empty alt</span>
          <span className="kv-value">{images.empty_alt ?? 0}</span>
        </li>
      </ul>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${coverage}%`, background: barColor }}
        />
      </div>
      <p className="progress-caption">{coverage}% of images have alt text</p>
    </div>
  );
}

export default ImagesCard;