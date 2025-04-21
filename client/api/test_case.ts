import { TestCaseCreate, TestCaseUpdate } from "@/schema/test_case";
import { api } from "./api";

const TEST_CASE_BASE_URL = "/testcase";

export const createTestCase = async (data: TestCaseCreate) => {
  const response = await api.post(`${TEST_CASE_BASE_URL}`, data);
  return response.data;
};

export const getTestCase = async (test_case_id: string) => {
  const response = await api.get(`${TEST_CASE_BASE_URL}/${test_case_id}`);
  return response.data;
};

export const updateTestCase = async (
  test_case_id: string,
  data: TestCaseUpdate
) => {
  const response = await api.put(`${TEST_CASE_BASE_URL}/${test_case_id}`, data);
  return response.data;
};

export const deleteTestCase = async (test_case_id: string) => {
  const response = await api.delete(`${TEST_CASE_BASE_URL}/${test_case_id}`);
  return response.data;
};

export const generateTestCase = async (project_id: string) => {
  const response = await api.post(
    `${TEST_CASE_BASE_URL}/${project_id}/generate`
  );
  return response.data;
};

export const pushTestCaseToJira = async (test_case_id: string) => {
  const response = await api.get(`${TEST_CASE_BASE_URL}/${test_case_id}/push`);
  return response.data;
};
