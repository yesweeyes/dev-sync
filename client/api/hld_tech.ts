import { HLDTechCreate, HLDTechUpdate } from "@/schema/hldtech";
import {api, api_form_data}  from "./api";

const TECH_DOCS_BASE_URL = "/tech_docs";


export const createHLD = async (data: HLDTechCreate) => {
    const response = await api.post(`${TECH_DOCS_BASE_URL}/upload`, data);
    return response.data;
}

