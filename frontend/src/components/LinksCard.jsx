function LinksCard({links}) {
    return(
    <div className="card">
      <p className="card-title">Links</p>
      <ul className="kv-list">
        <li className="kv-row">
          <span className="kv-label">Total links</span>
          <span className="kv-value">{links.total_links}</span>
        </li>
        <li className="kv-row">
          <span className="kv-label">Internal</span>
          <span className="kv-value">{links.internal_links}</span>
        </li>
        <li className="kv-row">
          <span className="kv-label">External</span>
          <span className="kv-value">{links.external_links}</span>
        </li>
        <li className="kv-row">
          <span className="kv-label">Empty links</span>
          <span className={`badge ${links.empty_links === 0 ? "pass" : "warn"}`}>
            {links.empty_links}
          </span>
        </li>
        <li className="kv-row">
          <span className="kv-label">Mailto links</span>
          <span className="kv-value">{links.mailto_links}</span>
        </li>
        <li className="kv-row">
          <span className="kv-label">Tel links</span>
          <span className="kv-value">{links.tel_links}</span>
        </li>
      </ul>
    </div>
    );
}

export default LinksCard;