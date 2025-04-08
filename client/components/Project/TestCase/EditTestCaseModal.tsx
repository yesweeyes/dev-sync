import React, { useEffect, useState } from "react";
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
import { Box } from "@/components/ui/box";
import { FormControl } from "@/components/ui/form-control";
import { Input, InputField } from "@/components/ui/input";
import { Heading } from "@/components/ui/heading";
import { TestCase, TestCaseUpdate } from "@/schema/test_case";
import LabeledText from "./LabeledText";

interface EditTestCaseModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUpdate: (TestCase: TestCaseUpdate) => void;
  testCase: TestCase;
}

const EditTestCaseModal = ({
  isOpen,
  onClose,
  onUpdate,
  testCase,
}: EditTestCaseModalProps) => {
  const [formData, setFormData] = useState<TestCaseUpdate>({
    module_name: testCase.module_name ?? "",
    description: testCase.description ?? "",
    preconditions: testCase.preconditions ?? "",
    test_steps: testCase.test_steps ?? [],
    post_condition: testCase.post_condition ?? "",
    priority: testCase.priority ?? "LOW",
    test_type: testCase.test_type ?? "",
  });

  useEffect(() => {
    if (testCase) {
      setFormData({
        module_name: testCase.module_name ?? "",
        description: testCase.description ?? "",
        preconditions: testCase.preconditions ?? "",
        test_steps: testCase.test_steps ?? [],
        post_condition: testCase.post_condition ?? "",
        priority: testCase.priority ?? "LOW",
        test_type: testCase.test_type ?? "",
      });
    }
  }, [testCase]);

  const handleChange = (field: keyof TestCaseUpdate, value: string) => {
    if (field === "test_steps") {
      setFormData((prev) => ({
        ...prev,
        [field]: value.split(",").map((item) => item.trim()),
      }));
    } else {
      setFormData((prev) => ({ ...prev, [field]: value }));
    }
  };

  const handleSubmit = () => {
    onUpdate({ ...formData });
    onClose();
  };
  return (
    <Modal isOpen={isOpen} closeOnOverlayClick={true}>
      <ModalBackdrop />
      <ModalContent>
        <ModalHeader>
          <ModalCloseButton />
        </ModalHeader>
        <ModalBody>
          <Box className="mb-2">
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Module Name"
                  value={formData.module_name}
                  onChangeText={(text) => {
                    handleChange("module_name", text);
                  }}
                />
              </Input>
            </FormControl>
          </Box>
          <Box className="mt-5 mb-2 space-y-4">
            <Heading size="sm">Test Case Details</Heading>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Description"
                  value={formData.description}
                  onChangeText={(text) => {
                    handleChange("description", text);
                  }}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Pre Conditions (comma separated)"
                  value={formData.preconditions}
                  onChangeText={(text) => {
                    handleChange("preconditions", text);
                  }}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Test steps (comma separated)"
                  value={
                    formData.test_steps ? formData.test_steps.join(", ") : ""
                  }
                  onChangeText={(text) => {
                    handleChange("test_steps", text);
                  }}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Post Conditions"
                  value={formData.post_condition}
                  onChangeText={(text) => {
                    handleChange("post_condition", text);
                  }}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="priority"
                  value={formData.priority}
                  onChangeText={(text) => {
                    handleChange("priority", text);
                  }}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Test Type"
                  value={formData.test_type}
                  onChangeText={(text) => {
                    handleChange("test_type", text);
                  }}
                />
              </Input>
            </FormControl>
          </Box>
        </ModalBody>
        <ModalFooter>
          <Button className="bg-red-600 w-20" onPress={onClose}>
            <ButtonText>Cancel</ButtonText>
          </Button>
          <Button className="bg-blue-600 w-20" onPress={handleSubmit}>
            <ButtonText>Submit</ButtonText>
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
};

export default EditTestCaseModal;
