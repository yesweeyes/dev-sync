import React, { useState, useEffect } from "react";
import {
  Modal,
  ModalBackdrop,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
} from "@/components/ui/modal";
import { FormControl } from "@/components/ui/form-control";
import { Input, InputField } from "@/components/ui/input";
import { Text } from "@/components/ui/text";
import { Heading } from "@/components/ui/heading";
import { Button, ButtonText } from "@/components/ui/button";
import { Box } from "@/components/ui/box";
import { ProjectUpdate } from "@/schema/project";
import { useAppStore } from "@/store/store";

interface EditProjectModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUpdate: (project: ProjectUpdate) => void;
}

function EditProjectModal({
  isOpen,
  onClose,
  onUpdate,
}: EditProjectModalProps) {
  const { project } = useAppStore();
  const [formData, setFormData] = useState<ProjectUpdate>({
    name: project?.name ? project.name : "",
    jira_project_key: project?.jira_project_key ? project.jira_project_key : "",
    jira_auth_key: project?.jira_auth_key ? project.jira_auth_key : "",
    jira_project_endpoint: project?.jira_project_endpoint
      ? project.jira_project_endpoint
      : "",
    jira_project_email: project?.jira_project_email
      ? project.jira_project_email
      : "",
    github_endpoint: project?.github_endpoint ? project.github_endpoint : "",
  });

  useEffect(() => {
    if (project) {
      setFormData(project);
    }
  }, [project]);

  const handleChange = (field: keyof ProjectUpdate, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = () => {
    onUpdate(formData);
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
                  placeholder="Project Name"
                  value={formData.name}
                  onChangeText={(text) => handleChange("name", text)}
                />
              </Input>
            </FormControl>
          </Box>

          <Box className="mt-6 mb-2 space-y-4">
            <Heading size="sm">Github Integration</Heading>

            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Project URL"
                  value={formData.github_endpoint}
                  onChangeText={(text) => handleChange("github_endpoint", text)}
                />
              </Input>
            </FormControl>
          </Box>

          <Box className="mt-6 mb-2 space-y-4">
            <Heading size="sm">JIRA Integration</Heading>

            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Project Key"
                  value={formData.jira_project_key}
                  onChangeText={(text) =>
                    handleChange("jira_project_key", text)
                  }
                />
              </Input>
            </FormControl>

            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Project URL"
                  value={formData.jira_project_endpoint}
                  onChangeText={(text) =>
                    handleChange("jira_project_endpoint", text)
                  }
                />
              </Input>
            </FormControl>

            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Email"
                  value={formData.jira_project_email}
                  onChangeText={(text) =>
                    handleChange("jira_project_email", text)
                  }
                />
              </Input>
            </FormControl>

            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Auth Key"
                  type="password"
                  value={formData.jira_auth_key}
                  onChangeText={(text) => handleChange("jira_auth_key", text)}
                />
              </Input>
            </FormControl>
          </Box>
        </ModalBody>
        <ModalFooter>
          <Button onPress={onClose} className="bg-red-600 w-20">
            <ButtonText>Cancel</ButtonText>
          </Button>
          <Button onPress={handleSubmit} className="bg-blue-600 w-20">
            <ButtonText>Save</ButtonText>
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
}

export default EditProjectModal;
