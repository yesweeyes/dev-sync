import React, { useState } from "react";
import {
  Modal,
  ModalBackdrop,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
} from "@/components/ui/modal";
import {
  FormControl,
  FormControlError,
  FormControlErrorText,
} from "@/components/ui/form-control";
import { Input, InputField } from "@/components/ui/input";
import { Text } from "@/components/ui/text";
import { Heading } from "@/components/ui/heading";
import { Button, ButtonText } from "@/components/ui/button";
import { Box } from "@/components/ui/box";
import { ProjectCreate } from "@/schema/project";

interface CreateProjectModalProps {
  isOpen: boolean;
  onClose: () => void;
  onCreate: (project: ProjectCreate) => void;
}

function CreateProjectModal({
  isOpen,
  onClose,
  onCreate,
}: CreateProjectModalProps) {
  const [formData, setFormData] = useState<ProjectCreate>({
    name: "",
    jira_project_key: "",
    jira_project_auth: "",
    jira_project_endpoint: "",
    jira_project_email: "",
  });

  const [errors, setErrors] = useState<Partial<ProjectCreate>>({});

  const handleChange = (field: keyof ProjectCreate, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    setErrors((prev) => ({
      ...prev,
      [field]: value.trim() === "" ? "This field is required" : "",
    }));
  };

  const handleSubmit = () => {
    const newErrors: Partial<ProjectCreate> = {};
    Object.keys(formData).forEach((key) => {
      if (formData[key as keyof ProjectCreate].trim() === "") {
        newErrors[key as keyof ProjectCreate] = "This field is required";
      }
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }
    onCreate(formData);
    onClose();
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} closeOnOverlayClick={true}>
      <ModalBackdrop />
      <ModalContent>
        <ModalHeader>
          <ModalCloseButton />
        </ModalHeader>
        <ModalBody>
          <Box className="mb-2">
            <FormControl isInvalid={!!errors.name}>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Project Name"
                  value={formData.name}
                  onChangeText={(text) => handleChange("name", text)}
                />
              </Input>
              {errors.name && (
                <FormControlError>
                  <FormControlErrorText>{errors.name}</FormControlErrorText>
                </FormControlError>
              )}
            </FormControl>
          </Box>
          <Box className="mt-6 mb-2 space-y-4">
            <Heading size="sm">JIRA Integration</Heading>

            <FormControl isInvalid={!!errors.jira_project_key}>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Project Key"
                  value={formData.jira_project_key}
                  onChangeText={(text) =>
                    handleChange("jira_project_key", text)
                  }
                />
              </Input>
              {errors.jira_project_key && (
                <FormControlError>
                  <FormControlErrorText>
                    {errors.jira_project_key}
                  </FormControlErrorText>
                </FormControlError>
              )}
            </FormControl>

            <FormControl isInvalid={!!errors.jira_project_endpoint}>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Project URL"
                  value={formData.jira_project_endpoint}
                  onChangeText={(text) =>
                    handleChange("jira_project_endpoint", text)
                  }
                />
              </Input>
              {errors.jira_project_endpoint && (
                <FormControlError>
                  <FormControlErrorText>
                    {errors.jira_project_endpoint}
                  </FormControlErrorText>
                </FormControlError>
              )}
            </FormControl>

            <FormControl isInvalid={!!errors.jira_project_email}>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Email"
                  value={formData.jira_project_email}
                  onChangeText={(text) =>
                    handleChange("jira_project_email", text)
                  }
                />
              </Input>
              {errors.jira_project_email && (
                <FormControlError>
                  <FormControlErrorText>
                    {errors.jira_project_email}
                  </FormControlErrorText>
                </FormControlError>
              )}
            </FormControl>

            <FormControl isInvalid={!!errors.jira_project_auth}>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Auth Key"
                  type="password"
                  value={formData.jira_project_auth}
                  onChangeText={(text) =>
                    handleChange("jira_project_auth", text)
                  }
                />
              </Input>
              {errors.jira_project_auth && (
                <FormControlError>
                  <FormControlErrorText>
                    {errors.jira_project_auth}
                  </FormControlErrorText>
                </FormControlError>
              )}
            </FormControl>
          </Box>
        </ModalBody>
        <ModalFooter>
          <Button onPress={handleSubmit} className=" bg-blue-600">
            <ButtonText>Create</ButtonText>
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
}

export default CreateProjectModal;
