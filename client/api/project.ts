import {api, api_form_data}  from "./api";
import { Project, ProjectCreate, ProjectUpdate } from "../schema/project";

const PROJECT_BASE_URL = "/project";

export const getAllProjects = async (): Promise<Project[]> => {
  const response = await api.get(PROJECT_BASE_URL);
  console.log(response);
  return response.data;
};

export const createProject = async (data: ProjectCreate): Promise<Project> => {
  const response = await api.post(PROJECT_BASE_URL, data);
  return response.data;
}

export const getProject = async(project_id: string): Promise<Project>  => {
  const response = await api.get(`${PROJECT_BASE_URL}/${project_id}`);
  return response.data
}

export const updateProject = async(project_id: string, data: ProjectUpdate): Promise<Project> => {
  const response = await api.put(`${PROJECT_BASE_URL}/${project_id}`, data);
  return response.data
}

export const deleteProject = async(project_id: string) => {
  const response = await api.delete(`${PROJECT_BASE_URL}/${project_id}`);
  return response.data
}

export const getProjectDocuments = async(project_id: string) => {
  const response = await api.get(`${PROJECT_BASE_URL}/${project_id}/documents`);
  return response.data
}