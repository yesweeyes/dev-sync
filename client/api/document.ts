import { api_form_data } from "./api";

const DOCUMENT_BASE_URL = "/document";
  
export const createProjectDocument = async(data: FormData) => {
    const response  = await api_form_data.post(`${DOCUMENT_BASE_URL}/upload`);
    return response.data;
  }