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
  jiraPush: boolean;
  jira_id: number;
  jira_ignored: boolean;
  created_at: Date;
}

export interface UserStoryCreate {
  project_id: string;
  title: string;
  description?: string;
  acceptance_criteria?: string;
  storyPoints?: number;
  priority?: string;
  labels?: string[];
  jiraPush: boolean;
  issueType: string;
  jira_id: number;
  jira_ignored?: boolean;
}

export interface UserStoryUpdate {
  title?: string;
  description?: string;
  acceptance_criteria?: string;
  storyPoints?: number;
  labels?: string[];
  priority?: string;
  jiraPush?: boolean;
  issueType?: string;
  jira_id?: number;
  jira_ignored?: boolean;
}

export interface UserStoryGenerate {
  project_id: string;
  user_prompt: string;
}
