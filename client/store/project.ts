import { create } from "zustand";
import { Project, ProjectCreate, ProjectUpdate } from "@/schema/project";
import { RequirementDocument, RequirementDocumentUpload} from "@/schema/requirement_document";
import { UserStory, UserStoryGenerate } from "@/schema/user_story";
import { getAllProjects, getProject, createProject, updateProject, deleteProject, getProjectDocuments, getProjectUserStories } from "@/api/project";
import { createProjectDocument, deleteProjectDocument } from "@/api/document";
import { generateUserStory, deleteUserStory } from "@/api/user_story";

interface ProjectStore {
  loading: boolean;
  error: string | null;
  
  projects: Project[];
  fetchProjects: () => Promise<void>;
  
  project: Project | null;
  fetchProject: (projectId: string) => Promise<void>;
  addProject: (data: ProjectCreate) => Promise<void>;
  updateProject: (projectId: string, data: ProjectUpdate) => Promise<void>;
  deleteProject: (projectId: string) => Promise<void>;
  clearProject: () => void;
  
  documents: RequirementDocument[];
  fetchProjectDocuments: (projectId: string) => Promise<void>;
  addDocument: (data: RequirementDocumentUpload) => Promise<void>;
  deleteDocument: (documentId: string) => Promise<void>;
  
  user_stories: UserStory[];
  fetchUserStories: (ProjectId: string) => Promise<void>;
  generateUserStories: (data: UserStoryGenerate) => Promise<void>;
}

export const useProjectStore = create<ProjectStore>((set) => ({
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

  project: null,
  fetchProject: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const project = await getProject(projectId);
      const documents = await getProjectDocuments(projectId);
      const user_stories = await getProjectUserStories(projectId);
      set({ project, loading: false });
      set({ project, documents, user_stories, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  addProject: async (data) => {
    set({ loading: true, error: null });
    try {
      await createProject(data);
      await useProjectStore.getState().fetchProjects();
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  updateProject: async (projectId, data) => {
    set({ loading: true, error: null });
    try {
      await updateProject(projectId, data);
      await useProjectStore.getState().fetchProject(projectId);
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  deleteProject: async (projectId) => {
    set({ loading: true, error: null });
    try {
      await deleteProject(projectId);
      await useProjectStore.getState().fetchProjects();
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  clearProject: () => set({ project: null, documents: []}),

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
  //TODO: fix this 
  addDocument: async (data) => {
    set({ loading: true, error: null });
    try {
      const formData = new FormData();
      formData.append("project_id", data.project_id.toString());
      formData.append("file", data.file);
  
      await createProjectDocument(formData);
      await useProjectStore.getState().fetchProjectDocuments(data.project_id);
      set({ loading: false }); 
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  deleteDocument: async (documentId) => {
    set({ loading: true, error: null });
    try {
      await deleteProjectDocument(documentId);
      await useProjectStore.getState().fetchProjectDocuments(documentId);
    } catch (error: any) {
      set({ error: error.message, loading: false });
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
      await useProjectStore.getState().fetchUserStories(data.project_id);
      set({ loading: false }); 
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

}));