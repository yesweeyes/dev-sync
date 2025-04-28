import axios from "axios";

const apiUrl = process.env.EXPO_PUBLIC_BACKEND_API_BASE_URL

export const api = axios.create({
  baseURL: apiUrl,
  headers: {
    "Content-Type": "application/json",
  },
});
