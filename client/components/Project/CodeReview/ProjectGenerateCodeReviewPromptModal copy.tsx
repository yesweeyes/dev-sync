import React, { useState } from "react";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";
import { useAppStore } from "@/store/store";
import { Box } from "@/components/ui/box";

function ProjectGenerateE2ECodeReviewButton() {
  const { project_id, generateCodeReviewFile } = useAppStore();

  const handleGenerate = async () => {
    if (!project_id) return;

    generateCodeReviewFile({
      project_id: project_id,
      user_prompt: "Generate a detailed end-to-end code review",
    });
  };

  return (
    <Box>
      <Fab
        size="md"
        placement="bottom right"
        className="bg-gradient-to-r from-blue-500 to-purple-600 text-white hover:scale-105 transition-transform"
        onPress={() => handleGenerate()}
      >
        <FabIcon as={Sparkles} className="text-white" />
        <FabLabel>E2E Code Review</FabLabel>
      </Fab>
    </Box>
  );
}

export default ProjectGenerateE2ECodeReviewButton;
