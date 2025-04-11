export interface CodeReviewFile {
    id: string;
    project_id: string;
    original_name: string;
    stored_name: string;
    file_path: string;
    created_at: Date;
}

export interface CodeReviewFileUpdate {
    original_name: string;
}

export interface CodeReviewGenerate {
    project_id: string;
    user_prompt: string;
}