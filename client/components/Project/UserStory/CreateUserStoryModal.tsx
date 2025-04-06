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
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { UserStoryCreate } from "@/schema/user_story";
import { Plus } from "lucide-react-native";
import { useAppStore } from "@/store/store";

function CreateUserStoryModal() {
  const { project_id, createUserStory } = useAppStore();
  const [isOpen, setIsOpen] = useState(false);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [acceptanceCriteria, setAcceptanceCriteria] = useState("");
  const [storyPoints, setStoryPoints] = useState(0);
  const [issueType, setIssueType] = useState("");
  const [priority, setPriority] = useState("LOW");
  const [labels, setLabels] = useState<string[]>([]);
  const [errors, setErrors] = useState<{
    [K in keyof UserStoryCreate]?: string;
  }>({});

  const handleLabelsChange = (value: string) => {
    setLabels(value.split(",").map((label) => label.trim()));
  };

  const handleSubmit = () => {
    const newErrors: { [K in keyof UserStoryCreate]?: string } = {};
    if (!title.trim()) newErrors.title = "This field is required";
    if (!description.trim()) newErrors.description = "This field is required";
    if (!acceptanceCriteria.trim())
      newErrors.acceptance_criteria = "This field is required";
    if (!issueType.trim()) newErrors.issueType = "This field is required";

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    const data = {
      project_id: project_id!,
      title: title,
      description: description,
      priority: priority,
      acceptance_criteria: acceptanceCriteria,
      storyPoints: storyPoints,
      issueType: issueType,
      labels: labels,
    };

    createUserStory(data);

    setTitle("");
    setDescription("");
    setAcceptanceCriteria("");
    setStoryPoints(0);
    setIssueType("");
    setLabels([]);

    setIsOpen(false);
  };

  return (
    <Box>
      <Fab size="md" placement="bottom right" onPress={() => setIsOpen(true)}>
        <FabIcon as={Plus} />
        <FabLabel>Create User Story</FabLabel>
      </Fab>
      <Modal
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        closeOnOverlayClick
      >
        <ModalBackdrop />
        <ModalContent>
          <ModalHeader>
            <ModalCloseButton />
          </ModalHeader>
          <ModalBody>
            <Box className="mb-2">
              <FormControl isInvalid={!!errors.title}>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Title"
                    value={title}
                    onChangeText={setTitle}
                  />
                </Input>
                {errors.title && (
                  <FormControlError>
                    <FormControlErrorText>{errors.title}</FormControlErrorText>
                  </FormControlError>
                )}
              </FormControl>
            </Box>
            <Box className="mt-6 mb-2 space-y-4">
              <Heading size="sm">User Story Details</Heading>
              <FormControl isInvalid={!!errors.description}>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Description"
                    value={description}
                    onChangeText={setDescription}
                  />
                </Input>
              </FormControl>
              <FormControl isInvalid={!!errors.acceptance_criteria}>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Acceptance Criteria"
                    value={acceptanceCriteria}
                    onChangeText={setAcceptanceCriteria}
                  />
                </Input>
              </FormControl>
              <FormControl isInvalid={!!errors.storyPoints}>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Story Points"
                    value={String(storyPoints)}
                    onChangeText={(text) => setStoryPoints(Number(text) || 0)}
                  />
                </Input>
              </FormControl>
              <FormControl isInvalid={!!errors.issueType}>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Issue Type"
                    value={issueType}
                    onChangeText={setIssueType}
                  />
                </Input>
              </FormControl>
              <FormControl>
                <Input variant="underlined" size="md">
                  <InputField
                    placeholder="Labels (comma separated)"
                    value={labels.join(", ")}
                    onChangeText={handleLabelsChange}
                  />
                </Input>
              </FormControl>
            </Box>
          </ModalBody>
          <ModalFooter>
            <Button
              onPress={() => setIsOpen(false)}
              className="bg-red-600 w-20"
            >
              <ButtonText>Cancel</ButtonText>
            </Button>
            <Button onPress={handleSubmit} className="bg-blue-600 w-20">
              <ButtonText>Create</ButtonText>
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Box>
  );
}

export default CreateUserStoryModal;
