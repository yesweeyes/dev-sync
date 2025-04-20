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
import { Button } from "@/components/ui/button";
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
      <Fab
        size="md"
        placement="bottom left"
        className="bg-gradient-to-r from-blue-500 to-purple-600 text-white hover:scale-105 transition-transform"
        onPress={() => setIsOpen(true)}
      >
        <FabIcon as={Sparkles} className="text-white" />
        <FabLabel>Custom Code Review</FabLabel>
      </Fab>

      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>
        <ModalBackdrop />
        <ModalContent className="rounded-2xl shadow-2xl bg-white p-6 max-w-lg mx-auto">
          <ModalHeader className="text-xl font-semibold text-gray-800 mb-2">
            🧠 Generate Code Review
          </ModalHeader>
          <ModalCloseButton />
          <ModalBody className="mb-4">
            <Input size="md" className="w-full">
              <InputField
                placeholder="Describe what you want reviewed..."
                value={prompt}
                onChangeText={setPrompt}
                className="text-base px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
            </Input>
          </ModalBody>
          <ModalFooter className="flex justify-end gap-2">
            <Button
              onPress={() => setIsOpen(false)}
              className="bg-red-500 hover:bg-red-600 text-white font-medium px-4 py-2 rounded-lg transition-colors"
            >
              Cancel
            </Button>
            <Button
              onPress={handleGenerate}
              className="bg-green-500 hover:bg-green-600 text-white font-medium px-4 py-2 rounded-lg transition-colors"
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
