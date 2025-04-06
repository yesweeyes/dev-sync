import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
});

export const api_form_data = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  // Don't manually set Content-Type here
  });
