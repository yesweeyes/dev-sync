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
import { Button, ButtonText } from "@/components/ui/button";
import { Input, InputField } from "@/components/ui/input";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";
import { useAppStore } from "@/store/store";
import { Box } from "@/components/ui/box";

function ProjectGenerateCodeReviewPromptModal() {
  const [isOpen, setIsOpen] = useState(false);
  const [prompt, setPrompt] = useState("");
  const { project_id, generateCodeReviewFile } = useAppStore();

  const handleGenerate = async () => {
    if (!prompt.trim() || !project_id) return;

    generateCodeReviewFile({
      project_id: project_id,
      user_prompt: prompt,
    });

    setIsOpen(false);
    setPrompt("");
  };

  return (
    <Box>
      <Fab size="md" placement="bottom left" onPress={() => setIsOpen(true)}>
        <FabIcon as={Sparkles} />
        <FabLabel>Generate Code Review</FabLabel>
      </Fab>
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

export default ProjectGenerateCodeReviewPromptModal;
