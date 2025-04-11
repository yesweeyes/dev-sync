import { api, api_form_data } from "./api";
import { CodeReviewFileUpdate, CodeReviewGenerate } from "@/schema/code_review";

const CODE_REVIEW_BASE_URL = "/code_review";

export const getCodeReviewFile = async(code_review_file_id: string) => {
  const response = await api.get(`${CODE_REVIEW_BASE_URL}/${code_review_file_id}`);
  return response.data
}

export const updateCodeReviewFile = async(code_review_file_id: string, data: CodeReviewFileUpdate) => {
  const response = await api.put(`${CODE_REVIEW_BASE_URL}/${code_review_file_id}`, data);
  return response.data
}

export const deleteCodeReviewFile = async(code_review_file_id: string) => {
  const response = await api.delete(`${CODE_REVIEW_BASE_URL}/${code_review_file_id}`);
  return response.data
}

export const generateCodeReviewFile = async (data: CodeReviewGenerate) => {
    const response = await api.post(`${CODE_REVIEW_BASE_URL}/generate`, data);
    return response.data;
}