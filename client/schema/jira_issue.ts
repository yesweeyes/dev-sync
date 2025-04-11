export interface JiraIssue {
  id: string;
  project_id: string;
  issue_id: Number;
  key: string;
  end_point: string;
  issue_type: string;
  parent_id: string;
}

export interface JiraIssueCreate {
  project_id: string;
  issue_id: Number;
  key: string;
  end_point: string;
  issue_type: string;
  parent_id: string;
}
