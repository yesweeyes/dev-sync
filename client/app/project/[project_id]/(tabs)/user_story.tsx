import React, { useState } from "react";
import UserStoryListView from "@/components/Project/ProjectUserStoryListView";
import { Box } from "@/components/ui/box";
import { Button, ButtonText } from "@/components/ui/button";
import { Input, InputField } from "@/components/ui/input";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import {
  Modal,
  ModalBackdrop,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
} from "@/components/ui/modal";
import { Sparkles } from "lucide-react-native";
import { useProjectStore } from "@/store/project";

function ProjectUserStoryPage() {
  const [isOpen, setIsOpen] = useState(false);
  const [prompt, setPrompt] = useState("");
  const { project, generateUserStories } = useProjectStore();

  const handleGenerate = async () => {
    if (!prompt.trim() || !project) return;

    generateUserStories({
      project_id: project?.id,
      user_prompt: prompt,
    });

    setIsOpen(false);
    setPrompt("");
  };

  return (
    <Box className="p-2 h-full w-full">
      <UserStoryListView />

      {/* Floating Action Button */}
      <Fab size="md" placement="bottom right" onPress={() => setIsOpen(true)}>
        <FabIcon as={Sparkles} />
        <FabLabel>Generate User Story</FabLabel>
      </Fab>

      {/* Modal */}
      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>
        <ModalBackdrop />
        <ModalContent>
          <ModalBody>
            <Input size="md">
              <InputField
                placeholder="Enter your prompt..."
                value={prompt}
                onChangeText={setPrompt}
              />
            </Input>
          </ModalBody>
          <ModalFooter>
            <Button
              onPress={() => setIsOpen(false)}
              className="bg-red-600 font-roboto text-typography-white"
            >
              Cancel
            </Button>
            <Button
              onPress={handleGenerate}
              className="ml-2 bg-green-500 font-roboto text-typography-white"
            >
              Generate
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Box>
  );
}

export default ProjectUserStoryPage;
