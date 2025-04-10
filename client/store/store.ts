import { create } from "zustand";
import { Project, ProjectCreate, ProjectUpdate } from "@/schema/project";
import {
  RequirementDocument,
  RequirementDocumentUpdate,
  RequirementDocumentUpload,
} from "@/schema/requirement_document";
import {
  UserStory,
  UserStoryCreate,
  UserStoryGenerate,
  UserStoryUpdate,
} from "@/schema/user_story";
import { TestCase, TestCaseCreate, TestCaseUpdate } from "@/schema/test_case";
import { JiraIssue, JiraIssueCreate } from "@/schema/jira_issue";

import {
  getAllProjects,
  getProject,
  createProject,
  updateProject,
  deleteProject,
  getProjectDocuments,
  getProjectUserStories,
  getProjectTestCases,
  getProjectJiraIssues,
} from "@/api/project";

import {
  createProjectDocument,
  deleteProjectDocument,
  updateProjectDocument,
} from "@/api/document";

import {
  generateUserStory,
  deleteUserStory,
  updateUserStory,
  createUserStory,
} from "@/api/user_story";

import {
  createTestCase,
  getTestCase,
  updateTestCase,
  deleteTestCase,
  generateTestCase,
} from "@/api/test_case";

import {
  postIssueStories,
  postIssueByStoryId,
  postIssueTestCases,
  postIssueByTestcaseId,
} from "@/api/jira_issue";

interface AppStoreInterface {
  loading: boolean;
  error: string | null;

  projects: Project[];
  fetchProjects: () => Promise<void>;

  project_id: string | null;

  project: Project | null;
  fetchProject: (projectId: string) => Promise<void>;
  addProject: (data: ProjectCreate) => Promise<void>;
  updateProject: (projectId: string, data: ProjectUpdate) => Promise<void>;
  deleteProject: (projectId: string) => Promise<void>;
  clearProject: () => void;

  documents: RequirementDocument[];
  fetchProjectDocuments: (projectId: string) => Promise<void>;
  addDocument: (data: RequirementDocumentUpload) => Promise<void>;
  updateDocument: (
    documentId: string,
    data: RequirementDocumentUpdate
  ) => Promise<void>;
  deleteDocument: (documentId: string) => Promise<void>;

  user_stories: UserStory[];
  fetchUserStories: (projectId: string) => Promise<void>;
  generateUserStories: (data: UserStoryGenerate) => Promise<void>;
  createUserStory: (data: UserStoryCreate) => Promise<void>;
  updateUserStory: (
    userStoryId: string,
    data: UserStoryUpdate
  ) => Promise<void>;
  deleteUserStory: (userStoryId: string) => Promise<void>;

  test_cases: TestCase[];
  fetchTestCases: (projectId: string) => Promise<void>;
  createTestCase: (data: TestCaseCreate) => Promise<void>;
  updateTestCase: (testCaseId: string, data: TestCaseUpdate) => Promise<void>;
  deleteTestCase: (TestCaseId: string) => Promise<void>;
  generateTestCase: (projectId: string) => Promise<void>;

  jira_issues: JiraIssue[];
  fetchJiraIssues: (projectId: string) => Promise<void>;
  postIssueStories: (projectId: string) => Promise<void>;
  postIssueByStoryId: (storyId: string) => Promise<void>;
  postIssueTestCases: (projectId: string) => Promise<void>;
  postIssueByTestcaseId: (testCaseId: string) => Promise<void>;
}

export const useAppStore = create<AppStoreInterface>((set) => ({
  loading: false,
  error: null,

  projects: [],
  fetchProjects: async () => {
    set({ loading: true, error: null });
    try {
      const projects = await getAllProjects();
      set({ projects, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  project_id: null,

  project: null,
  fetchProject: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const project = await getProject(projectId);
      const documents = await getProjectDocuments(projectId);
      const user_stories = await getProjectUserStories(projectId);
      const test_cases = await getProjectTestCases(projectId);
      const jira_issues = await getProjectJiraIssues(projectId);
      set({
        project,
        project_id: project.id,
        documents,
        user_stories,
        test_cases,
        loading: false,
      });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  addProject: async (data) => {
    set({ loading: true, error: null });
    try {
      await createProject(data);
      await useAppStore.getState().fetchProjects();
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  updateProject: async (projectId, data) => {
    set({ loading: true, error: null });
    try {
      await updateProject(projectId, data);
      await useAppStore.getState().fetchProject(projectId);
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  deleteProject: async (projectId) => {
    set({ loading: true, error: null });
    try {
      await deleteProject(projectId);
      await useAppStore.getState().fetchProjects();
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  clearProject: () =>
    set({ project: null, project_id: null, documents: [], user_stories: [] }),

  documents: [],
  fetchProjectDocuments: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const documents = await getProjectDocuments(projectId);
      set({ documents, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  addDocument: async (data) => {
    set({ loading: true, error: null });
    try {
      const formData = new FormData();
      formData.append("project_id", data.project_id.toString());
      formData.append("file", data.file);

      await createProjectDocument(formData);
      await useAppStore.getState().fetchProjectDocuments(data.project_id);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  updateDocument: async (documentId, data) => {
    set({ loading: true, error: null });
    try {
      await updateProjectDocument(documentId, data);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
      await useAppStore
        .getState()
        .fetchProjectDocuments(useAppStore.getState().project_id!);
      set({ loading: false });
    }
  },

  deleteDocument: async (documentId) => {
    set({ loading: true, error: null });
    try {
      await deleteProjectDocument(documentId);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
      await useAppStore
        .getState()
        .fetchProjectDocuments(useAppStore.getState().project_id!);
      set({ loading: false });
    }
  },

  user_stories: [],
  fetchUserStories: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const user_stories = await getProjectUserStories(projectId);
      set({ user_stories, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  generateUserStories: async (data) => {
    set({ loading: true, error: null });
    try {
      await generateUserStory(data);
      await useAppStore.getState().fetchUserStories(data.project_id);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  createUserStory: async (data) => {
    set({ loading: true, error: null });
    try {
      await createUserStory(data);
      if (useAppStore.getState().project_id) {
        await useAppStore
          .getState()
          .fetchUserStories(useAppStore.getState().project_id!);
      }
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  updateUserStory: async (userStoryId, data) => {
    set({ loading: true, error: null });
    try {
      console.log(userStoryId, data);
      await updateUserStory(userStoryId, data);
      if (useAppStore.getState().project_id) {
        await useAppStore
          .getState()
          .fetchUserStories(useAppStore.getState().project_id!);
      }
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  deleteUserStory: async (userStoryId) => {
    set({ loading: true, error: null });
    try {
      await deleteUserStory(userStoryId);
      if (useAppStore.getState().project_id) {
        await useAppStore
          .getState()
          .fetchUserStories(useAppStore.getState().project_id!);
      }
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  test_cases: [],
  fetchTestCases: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const test_cases = await getProjectTestCases(projectId);
      set({ test_cases, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  createTestCase: async (data) => {
    set({ loading: true, error: null });
    try {
      await createTestCase(data);
      if (useAppStore.getState().project_id) {
        await useAppStore
          .getState()
          .fetchTestCases(useAppStore.getState().project_id!);
      }
      set({ loading: false });
    } catch (error: any) {
      set({ loading: false, error: error.message });
    }
  },

  updateTestCase: async (testCaseId, data) => {
    set({ loading: true, error: null });
    try {
      await updateTestCase(testCaseId, data);
      if (useAppStore.getState().project_id) {
        await useAppStore
          .getState()
          .fetchTestCases(useAppStore.getState().project_id!);
      }
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  deleteTestCase: async (testCaseId) => {
    set({ loading: true, error: null });
    try {
      await deleteTestCase(testCaseId);
      if (useAppStore.getState().project_id) {
        await useAppStore
          .getState()
          .fetchTestCases(useAppStore.getState().project_id!);
      }
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  generateTestCase: async (projectId) => {
    set({ loading: true, error: null });
    try {
      await generateTestCase(projectId);
      await useAppStore.getState().fetchTestCases(projectId);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  jira_issues: [],
  fetchJiraIssues: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const jira_issues = await getProjectJiraIssues(projectId);
      set({ jira_issues, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  postIssueStories: async (projectId) => {
    set({ loading: true, error: null });
    try {
      await postIssueStories(projectId);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  postIssueByStoryId: async (storyId) => {
    set({ loading: true, error: null });
    try {
      await postIssueByStoryId(storyId);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  postIssueTestCases: async (projectId) => {
    set({ loading: true, error: null });
    try {
      await postIssueTestCases(projectId);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  postIssueByTestcaseId: async (testCaseId) => {
    set({ loading: true, error: null });
    try {
      await postIssueByTestcaseId(testCaseId);
      set({ loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
}));
