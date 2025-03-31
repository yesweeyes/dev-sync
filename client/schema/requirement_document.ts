export interface RequirementDocument {
    id: string;
    project_id: string;
    original_name: string;
    stored_name: string;
    file_path: string;
}

export interface RequirementDocumentUpload {
    project_id: string;
    file: any
  }
  