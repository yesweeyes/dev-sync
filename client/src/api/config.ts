import axios from "axios";

const BASE_URL = process.env.BACKEND_API_BASE_URL;
const api = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Content-Type': 'application/json',
      },
});

export default api;

