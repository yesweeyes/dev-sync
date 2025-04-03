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
import { useStore } from "@/store/store";
import { UserStory, UserStoryUpdate } from "@/schema/user_story";

interface EditUserStoryModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUpdate: (userStory: any) => void;
  userStory: UserStory;
}

function EditUserStoryModal({
  isOpen,
  onClose,
  onUpdate,
  userStory,
}: EditUserStoryModalProps) {
  const [formData, setFormData] = useState<UserStoryUpdate>({
    title: userStory.title ? userStory.title : "",
    description: userStory.description ? userStory.description : "",
    acceptance_criteria: userStory.acceptance_criteria
      ? userStory.acceptance_criteria
      : "",
    storyPoints: userStory.storyPoints ? userStory.storyPoints : 0,
    issueType: userStory.issueType ? userStory.issueType : "",
  });

  useEffect(() => {
    if (userStory) {
      setFormData(userStory);
    }
  }, [userStory]);

  const handleChange = (field: keyof UserStoryUpdate, value: string) => {
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
                  placeholder="Title"
                  value={formData.title}
                  onChangeText={(text) => handleChange("title", text)}
                />
              </Input>
            </FormControl>
          </Box>
          <Box className="mt-6 mb-2 space-y-4">
            <Heading size="sm">User Story Details</Heading>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Description"
                  value={formData.description}
                  onChangeText={(text) => handleChange("description", text)}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Acceptance Criteria"
                  value={formData.acceptance_criteria}
                  onChangeText={(text) =>
                    handleChange("acceptance_criteria", text)
                  }
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Story Points"
                  value={String(formData.storyPoints ?? 0)}
                  onChangeText={(text) => handleChange("storyPoints", text)}
                />
              </Input>
            </FormControl>
            <FormControl>
              <Input variant="underlined" size="md">
                <InputField
                  placeholder="Issue Type"
                  value={formData.issueType}
                  onChangeText={(text) => handleChange("issueType", text)}
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

export default EditUserStoryModal;
