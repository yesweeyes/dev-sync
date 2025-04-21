export interface HLDTech {
    id: string;
    project_id: string;
    original_name: string;
    stored_name: string;
    file_path: string;
    created_at: Date;
}
    

export interface HLDTechCreate {
    project_id: string;
    original_name: string;
    stored_name: string;
    file_path: string;
}

export interface HLDTechUpdate {
    original_name: string;
}