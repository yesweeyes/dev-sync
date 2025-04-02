import { RequirementDocumentUpdate } from "@/schema/requirement_document";
import { api, api_form_data } from "./api";

const DOCUMENT_BASE_URL = "/document";
 
// TODO: add interface for form data type to match backend
export const createProjectDocument = async(data: FormData) => {
    const response  = await api_form_data.post(`${DOCUMENT_BASE_URL}/upload`, data);
    return response.data;
}

export const getProjectDocument = async(document_id: string) => {
  const response = await api.get(`${DOCUMENT_BASE_URL}/${document_id}`);
  return response.data
}

export const updateProjectDocument = async(document_id: string, data: RequirementDocumentUpdate) => {
  const response = await api.put(`${DOCUMENT_BASE_URL}/${document_id}`, data);
  return response.data
}

export const deleteProjectDocument = async(document_id: string) => {
  const response = await api.delete(`${DOCUMENT_BASE_URL}/${document_id}`);
  return response.data
}