import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL ?? "https://127.0.1:8000",
});

export default api;