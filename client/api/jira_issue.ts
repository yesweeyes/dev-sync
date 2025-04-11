import { JiraIssue, JiraIssueCreate } from "@/schema/jira_issue";
import { api } from "./api";

const JIRA_ISSUE_BASE_URL = "/issue";

export const postIssueStories = async (project_id: string) => {
  const response = await api.get(`${JIRA_ISSUE_BASE_URL}/${project_id}/story`);
  return response.data;
};

export const postIssueByStoryId = async (story_id: string) => {
  const response = await api.get(`${JIRA_ISSUE_BASE_URL}/${story_id}/push`);
  return response.data;
};

export const postIssueTestCases = async (project_id: string) => {
  const response = await api.get(
    `${JIRA_ISSUE_BASE_URL}/${project_id}/testcase`
  );
  return response.data;
};

export const postIssueByTestcaseId = async (testcase_id: string) => {
  const response = await api.get(
    `${JIRA_ISSUE_BASE_URL}/${testcase_id}/testcase/push`
  );
  return response.data;
};
