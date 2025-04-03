// TODO: add story points number gt 0 validation
export interface UserStory {
    id: string;
    project_id: string;
    title: string;
    description: string;
    acceptance_criteria: string;
    storyPoints: number;
    priority: string;
    labels: string[];
    issueType: string;
    created_at: Date
}

export interface UserStoryCreate {
    project_id: string;
    title: string;
    description: string;
    acceptance_criteria: string;
    storyPoints: number;
    priority: string;
    labels: string[];
    issueType: string;
}

export interface UserStoryUpdate {
    title?: string;
    description?: string;
    acceptance_criteria?: string;
    storyPoints?: number;
    labels?: string[];
    priority?: string;
    issueType?: string;
}

export interface UserStoryGenerate {
    project_id: string;
    user_prompt: string;
}