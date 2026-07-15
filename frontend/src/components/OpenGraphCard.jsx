function OGValue ({value}){
    if (!value) return <span className = "badge fail">Missing</span>
    return <span className = "kv-value">{value}</span>;
}

function OpenGraphCard({opengraph}) {
    return(
    <div className="card">
      <p className="card-title">Open Graph</p>
      <ul className="kv-list">
        <li className="kv-row">
          <span className="kv-label">og:title</span>
          <OGValue value={opengraph.og_title} />
        </li>
        <li className="kv-row">
          <span className="kv-label">og:description</span>
          <OGValue value={opengraph.og_description} />
        </li>
        <li className="kv-row">
          <span className="kv-label">og:image</span>
          <OGValue value={opengraph.og_image} />
        </li>
        <li className="kv-row">
          <span className="kv-label">og:url</span>
          <OGValue value={opengraph.og_url} />
        </li>
        <li className="kv-row">
          <span className="kv-label">Twitter card</span>
          <OGValue value={opengraph.twitter_card} />
        </li>
      </ul>
    </div>
    );
}

export default OpenGraphCard;