import axios from "axios";

// const BASE_URL = process.env.BACKEND_API_BASE_URL;
const BASE_URL = "http://127.0.0.1:8000/api";

console.log("Checking URL: ",BASE_URL);

const api = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Content-Type': 'application/json',
      },
});

export default api;

