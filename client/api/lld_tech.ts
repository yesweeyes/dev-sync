import { LLDTechCreate, LLDTechUpdate } from "@/schema/lldtech";
import {api, api_form_data}  from "./api";

const TECH_DOCS_BASE_URL = "/tech_docs";


export const createLLD = async (data: LLDTechCreate) => {
    const response = await api.post(`${TECH_DOCS_BASE_URL}/upload`, data);
    return response.data;
}

