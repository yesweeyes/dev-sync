export interface LLDTech {
    id: string;
    project_id: string;
    original_name: string;
    stored_name: string;
    file_path: string;
    created_at: Date;
}
    

export interface LLDTechCreate {
    project_id: string;
    original_name: string;
    stored_name: string;
    file_path: string;
}

export interface LLDTechUpdate {
    original_name: string;
}