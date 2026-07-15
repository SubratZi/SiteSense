function Bool({value}){
    return(
        <span className = {`badge ${value ? "pass": "fail"}`}>
            {value ? "Yes": "No"}
        </span>
    );
}

function TechnicalCard({technical}) {
    return(
        <div className="card">
      <p className="card-title">Technical</p>
      <ul className="kv-list">
        <li className="kv-row">
          <span className="kv-label">HTTPS</span>
          <Bool value={technical.has_https} />
        </li>
        <li className="kv-row">
          <span className="kv-label">Language attribute</span>
          <Bool value={technical.has_lang} />
        </li>
        <li className="kv-row">
          <span className="kv-label">Charset</span>
          <Bool value={technical.has_charset} />
        </li>
        <li className="kv-row">
          <span className="kv-label">Viewport</span>
          <Bool value={technical.has_viewport} />
        </li>
        <li className="kv-row">
          <span className="kv-label">Canonical URL</span>
          <Bool value={technical.has_canonical} />
        </li>
        <li className="kv-row">
          <span className="kv-label">Robots tag</span>
          <Bool value={technical.has_robots} />
        </li>
      </ul>
    </div>
    );
}

export default TechnicalCard;