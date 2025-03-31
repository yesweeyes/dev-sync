import { Project, ProjectCreate, ProjectUpdate } from "@/schema/project";
import { RequirementDocument, RequirementDocumentUpload} from "@/schema/requirement_document";
import { getAllProjects, getProject, createProject, updateProject, deleteProject, getProjectDocuments } from "@/api/project";
import {createProjectDocument} from "@/api/document";
import { create } from "zustand";

interface ProjectStore {
  projects: Project[];
  project: Project | null;
  documents: RequirementDocument[];
  loading: boolean;
  error: string | null;
  fetchProjects: () => Promise<void>;
  fetchProject: (projectId: string) => Promise<void>;
  addProject: (data: ProjectCreate) => Promise<void>;
  updateProject: (projectId: string, data: ProjectUpdate) => Promise<void>;
  deleteProject: (projectId: string) => Promise<void>;
  clearProject: () => void;
  fetchProjectDocuments: (projectId: string) => Promise<void>;
  addDocument: (data: RequirementDocumentUpload) => Promise<void>;
  deleteDocument: (documentId: string) => Promise<void>;
}

export const useProjectStore = create<ProjectStore>((set) => ({
  projects: [],
  project: null,
  documents: [],
  loading: false,
  error: null,

  fetchProjects: async () => {
    set({ loading: true, error: null });
    try {
      const projects = await getAllProjects();
      set({ projects, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },

  fetchProject: async (projectId) => {
    set({ loading: true, error: null });
    try {
      const project = await getProject(projectId);
      const documents = await getProjectDocuments(projectId);
      set({ project, loading: false });
      set({ project, documents, loading: false });
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
      await useProjectStore.getState().fetchProjectDocuments(data.project_id);
      set({ loading: false }); // Reset loading state after success
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  
  

  deleteDocument: async (documentId) => {
    set({ loading: true, error: null });
    try {
      // await deleteProjectDocument(documentId);
      await useProjectStore.getState().fetchProjectDocuments(documentId);
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  }

}));