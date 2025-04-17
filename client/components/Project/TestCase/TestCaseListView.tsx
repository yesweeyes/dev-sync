import { View, Text, FlatList, TouchableOpacity } from "react-native";
import React, { useEffect, useState } from "react";
import { Box } from "@/components/ui/box";
import { useAppStore } from "@/store/store";
import { Card } from "@/components/ui/card";
import { VStack } from "@/components/ui/vstack";
import { HStack } from "@/components/ui/hstack";
import {
  ChevronDown,
  ChevronUp,
  Edit,
  Send,
  Trash2,
} from "lucide-react-native";
import { Button, ButtonIcon } from "@/components/ui/button";
import LabeledText from "./LabeledText";
import NoRecordsFound from "@/components/Common/NoRecordsFound";
import { TestCase, TestCaseUpdate } from "@/schema/test_case";
import EditTestCaseModal from "./EditTestCaseModal";
import { updateTestCase } from "@/api/test_case";
import { postIssueByTestcaseId } from "@/api/jira_issue";

const TestCaseListView = () => {
  const {
    test_cases,
    project_id,
    fetchTestCases,
    deleteTestCase,
    getTestCase,
    updateTestCase,
  } = useAppStore();
  const [expanded, setExpanded] = useState<{ [key: string]: boolean }>({});
  const [isEditModalOpen, setisEditModalOpen] = useState(false);
  const [selectedTestcase, setselectedTestcase] = useState<TestCase>();

  const toggleExpand = (id: string) => {
    setExpanded((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  async function handleDelete(testcase_id: string) {
    if (testcase_id && project_id) {
      await deleteTestCase(testcase_id);
      fetchTestCases(project_id);
    }
  }
  const handleEdit = (test_case: TestCase) => {
    setselectedTestcase(test_case);
    setisEditModalOpen(true);
  };
  async function handleUpdate(updatedTestCase: TestCaseUpdate) {
    if (selectedTestcase && project_id) {
      await updateTestCase(selectedTestcase.id, updatedTestCase);
      fetchTestCases(project_id);
    }
    setisEditModalOpen(false);
  }

  async function handlePushToJira(testcase_id: string) {
    if (testcase_id) {
      await postIssueByTestcaseId(testcase_id);
    }
    let testcase = await getTestCase(testcase_id);
    testcase.jiraPush = true;
    await updateTestCase(testcase_id, { jiraPush: true });
  }
  return (
    <Box className="h-full w-full">
      {selectedTestcase && (
        <EditTestCaseModal
          isOpen={isEditModalOpen}
          onClose={() => setisEditModalOpen(false)}
          onUpdate={handleUpdate}
          testCase={selectedTestcase}
        />
      )}

      {test_cases.length == 0 ? (
        <>
          <NoRecordsFound />
        </>
      ) : (
        <FlatList
          data={test_cases}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <Card className="p-2 m-2 rounded-xl bg-white">
              <VStack className="md">
                <HStack className="flex justify-between items-center">
                  <TouchableOpacity
                    className="basis-4/5"
                    onPress={() => toggleExpand(item.id)}
                  >
                    <HStack className="items-center space-x-2">
                      {expanded[item.id] ? (
                        <ChevronUp size={20} color="black" />
                      ) : (
                        <ChevronDown size={20} color="black" />
                      )}
                      <Text className="text-base font-roboto text-typography-black">
                        {item.title} - {item.module_name}
                      </Text>
                    </HStack>
                  </TouchableOpacity>
                  <HStack className="basis-1/5 justify-end" space="sm">
                    <Button
                      className={`rounded-full w-14 h-14 items-center justify-center ${
                        item.jiraPush
                          ? "bg-gray-600 cursor-not-allowed"
                          : "bg-blue-600"
                      }`}
                      disabled={item.jiraPush}
                      onPress={() => {
                        handlePushToJira(item.id);
                      }}
                    >
                      <ButtonIcon as={Send} size="lg" />
                    </Button>
                    <Button
                      className="bg-yellow-600 rounded-full w-14 h-14 items-center justify-center"
                      onPress={() => {
                        handleEdit(item);
                      }}
                    >
                      <ButtonIcon as={Edit} size="lg" />
                    </Button>
                    <Button
                      className="bg-red-600 rounded-full w-14 h-14 items-center justify-center"
                      onPress={() => {
                        handleDelete(item.id);
                      }}
                    >
                      <ButtonIcon as={Trash2} size="lg" />
                    </Button>
                  </HStack>
                </HStack>
                {expanded[item.id] && (
                  <VStack className="p-2 bg-gray-100 rounded-lg" space="sm">
                    <LabeledText label="Module Name" value={item.module_name} />
                    <LabeledText label="Description" value={item.description} />
                    <LabeledText
                      label="Pre Conditions"
                      value={item.preconditions}
                    />
                    <LabeledText label="Test Steps" value={item.test_steps} />
                    <LabeledText
                      label="Post Condition"
                      value={item.post_condition}
                    />
                    <LabeledText label="Priority" value={item.priority} />
                    <LabeledText label="Test Type" value={item.test_type} />
                  </VStack>
                )}
              </VStack>
            </Card>
          )}
        />
      )}
    </Box>
  );
};

export default TestCaseListView;
