import { HldLldGenerate } from "@/schema/design_doc";
import {api, api_form_data}  from "./api";

const TECH_DOCS_BASE_URL = "/tech_docs";


export const GenerateTechDoc = async (data: HldLldGenerate) => {
    const response = await api.post(`${TECH_DOCS_BASE_URL}/generate`, data);
    return response.data;
}

export const DeleteTechDoc=async (design_docs_file_id: string)=> {
    const response = await api.delete(`${TECH_DOCS_BASE_URL}/${design_docs_file_id}`);
    return response.data;
}

