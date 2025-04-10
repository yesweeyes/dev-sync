import { View, Text } from "react-native";
import React, { useState } from "react";
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { Plus } from "lucide-react-native";
import {
  Modal,
  ModalBackdrop,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
} from "@/components/ui/modal";
import { Button, ButtonText } from "@/components/ui/button";
import { FormControl } from "@/components/ui/form-control";
import { Input, InputField } from "@/components/ui/input";
import { Heading } from "@/components/ui/heading";
import { useAppStore } from "@/store/store";
import { TestCaseCreate } from "@/schema/test_case";
import { Box } from "@/components/ui/box";

const CreateTestCase = () => {
  const { project_id, createTestCase } = useAppStore();
  const [isOpen, setisOpen] = useState(false);
  const [module, setmodule] = useState("");
  const [title, settitle] = useState("");
  const [description, setdescription] = useState("");
  const [preConditions, setpreConditions] = useState("");
  const [TestSteps, setTestSteps] = useState<string[]>([]);
  const [postCondition, setpostCondition] = useState("");
  const [priority, setpriority] = useState<"LOW" | "MEDIUM" | "HIGH">("LOW");
  const [TestType, setTestType] = useState("");
  const [errors, setErrors] = useState<{
    [K in keyof TestCaseCreate]?: string;
  }>({});

  const handleChange = (val: string) => {
    setTestSteps(val.split(",").map((step) => step.trim()));
  };

  const handleSubmit = () => {
    const newErrors: { [K in keyof TestCaseCreate]?: string } = {};
    if (!module.trim()) newErrors.module_name = "This field is required";
    if (!title.trim()) newErrors.title = "This field is required";
    if (!description.trim()) newErrors.description = "This field is required";
    if (!preConditions.trim())
      newErrors.preconditions = "This field is required";
    if (
      TestSteps.length === 0 ||
      TestSteps.every((step) => step.trim() === "")
    ) {
      newErrors.test_steps = "At least one valid test step is required";
    }
    if (!postCondition.trim())
      newErrors.post_condition = "This field is required";
    if (!priority.trim()) newErrors.priority = "This field is required";
    if (!TestType.trim()) newErrors.test_type = "This field is required";

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    const data = {
      project_id: project_id!,
      module_name: module,
      title: title,
      description: description,
      preconditions: preConditions,
      test_steps: TestSteps,
      post_condition: postCondition,
      priority: priority,
      test_type: TestType,
    };

    createTestCase(data);
    setmodule("");
    settitle("");
    setdescription("");
    setpreConditions("");
    setTestSteps([]);
    setpostCondition("");
    setpriority("LOW");
    setTestType("");
    setisOpen(false);
  };

  return (
    <Box>
      <Fab
        size="md"
        placement="bottom right"
        onPress={() => {
          setisOpen(true);
        }}
      >
        <FabIcon as={Plus} />
        <FabLabel>Create Test Case</FabLabel>
      </Fab>
      <Modal
        isOpen={isOpen}
        onClose={() => setisOpen(false)}
        closeOnOverlayClick
      >
        <ModalBackdrop />
        <ModalContent>
          <ModalHeader>
            <ModalCloseButton />
          </ModalHeader>
          <ModalBody>
            <Box className="mb-2">
              <FormControl isInvalid={!!errors.module_name}>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Module Name"
                    value={module}
                    onChangeText={setmodule}
                  />
                </Input>
              </FormControl>
            </Box>
            <Box className="mt-6 mb-2 space-y-4">
              <Heading size="sm">Test Case Details</Heading>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Test Case title"
                    value={title}
                    onChangeText={settitle}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Description"
                    value={description}
                    onChangeText={setdescription}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Pre Conditions"
                    value={preConditions}
                    onChangeText={setpreConditions}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Test Steps"
                    multiline
                    value={TestSteps.join(" ,")}
                    onChangeText={handleChange}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Post Condition"
                    value={postCondition}
                    onChangeText={setpostCondition}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Priority(HIGH | LOW | MEDIUM)"
                    value={priority}
                    onChangeText={(text) => {
                      if (text == "LOW" || text == "MEDIUM" || text == "HIGH") {
                        setpriority(text);
                      }
                    }}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Test Type"
                    value={TestType}
                    onChangeText={setTestType}
                  />
                </Input>
              </FormControl>
            </Box>
          </ModalBody>
          <ModalFooter>
            <Button
              onPress={() => {
                setisOpen(false);
              }}
              className="bg-red-600 w-20"
            >
              <ButtonText>Cancel</ButtonText>
            </Button>
            <Button onPress={handleSubmit} className="bg-blue-600 w-20">
              <ButtonText>Submit</ButtonText>
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Box>
  );
};

export default CreateTestCase;
