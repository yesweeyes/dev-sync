export interface TestCase {
  id: string;
  project_id: string;
  module_name: string;
  title: string;
  description: string;
  preconditions: string;
  test_steps: string[];
  post_condition: string;
  priority: "HIGH" | "MEDIUM" | "LOW";
  test_type: string;
  jiraPush: boolean;
  created_at: Date;
}

export interface TestCaseCreate {
  project_id: string;
  module_name: string;
  title: string;
  description: string;
  preconditions: string;
  test_steps: string[];
  post_condition: string;
  priority: "HIGH" | "MEDIUM" | "LOW";
  jiraPush: boolean;
  test_type: string;
}

export interface TestCaseUpdate {
  module_name?: string;
  description?: string;
  preconditions?: string;
  test_steps?: string[];
  post_condition?: string;
  priority?: "HIGH" | "MEDIUM" | "LOW";
  test_type?: string;
  jiraPush?: boolean;
}
