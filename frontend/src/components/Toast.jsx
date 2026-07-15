function Toast({message, type = "error", onClose}){
    const icon = type === "error" ? "X" : "✓";

    return(
        <div className = {`toast ${type}`} >
            <span className=" toast-icon">{icon}</span>
            <span className="toast-message">{message}</span>
            <button className="toast-close" onClick={onClose} aria-label = "Dismiss">X</button>
        </div>
    );
}

export default Toast;