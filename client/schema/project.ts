export interface Project {
    id: string,
    name: string, 
    jira_project_key: string, 
    jira_auth_key: string, 
    jira_project_endpoint: string,
    jira_project_email: string, 
    created_at: Date
}

export interface ProjectCreate {
    name: string, 
    jira_project_key: string, 
    jira_project_auth: string, 
    jira_project_endpoint: string,
    jira_project_email: string, 
}

export interface ProjectUpdate {
    name?: string, 
    jira_project_key?: string, 
    jira_auth_key?: string, 
    jira_project_endpoint?: string,
    jira_project_email?: string, 
}