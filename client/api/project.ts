import api from "./api";
import { Project, ProjectCreate, ProjectUpdate } from "../schema/project";

export const getAllProjects = async (): Promise<Project[]> => {
  const response = await api.get("/project");
  return response.data;
};

export const createProject = async (data: ProjectCreate): Promise<Project> => {
  const response = await api.post("/project", data);
  return response.data;
}

export const getProject = async(project_id: string): Promise<Project>  => {
  const response = await api.get(`project/${project_id}`);
  return response.data
}

export const updateProject = async(project_id: string, data: ProjectUpdate): Promise<Project> => {
  const response = await api.put(`project/${project_id}`, data);
  return response.data
}

export const deleteProject = async(project_id: string) => {
  const response = await api.delete(`project/${project_id}`);
  return response.data
}
