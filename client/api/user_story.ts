import {
  UserStoryCreate,
  UserStoryGenerate,
  UserStoryUpdate,
} from "@/schema/user_story";
import { api, api_form_data } from "./api";

const USER_STORY_BASE_URL = "/user_story";

export const createUserStory = async (data: UserStoryCreate) => {
  const response = await api.post(USER_STORY_BASE_URL, data);
  return response.data;
};

export const getUserStory = async (user_story_id: string) => {
  const response = await api.get(`${USER_STORY_BASE_URL}/${user_story_id}`);
  return response.data;
};

export const updateUserStory = async (
  user_story_id: string,
  data: UserStoryUpdate
) => {
  const response = await api.put(
    `${USER_STORY_BASE_URL}/${user_story_id}`,
    data
  );
  return response.data;
};

export const deleteUserStory = async (user_story_id: string) => {
  const response = await api.delete(`${USER_STORY_BASE_URL}/${user_story_id}`);
  return response.data;
};

export const generateUserStory = async (data: UserStoryGenerate) => {
  const response = await api.post(`${USER_STORY_BASE_URL}/generate`, data);
  return response.data;
};

export const pushUserStoryToJIRA = async (user_story_id: string) => {
  const response = await api.post(
    `${USER_STORY_BASE_URL}/${user_story_id}/push`
  );
  return response.data;
};

export const getIssuesFromJira = async (project_id: string) => {
  const response = await api.get(`${USER_STORY_BASE_URL}/${project_id}/jira`);
};
