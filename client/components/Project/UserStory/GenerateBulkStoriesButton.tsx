import { View, Text } from "react-native";
import React, { useEffect, useState } from "react";
import { Box } from "@/components/ui/box";
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";
import { useAppStore } from "@/store/store";

const GenerateBulkStoriesButton = () => {
  const { project_id, generateUserStories } = useAppStore();
  const handleSubmit = async () => {
    if (!project_id) return;
    generateUserStories({
      project_id: project_id,
      user_prompt:
        "Generate user stories for all the content including functional and non functional",
    });
  };
  return (
    <Box>
      <Fab
        size="md"
        placement="bottom center"
        className="bg-gradient-to-r from-blue-500 to-purple-600 hover:scale-105 transition-transform"
        onPress={handleSubmit}
      >
        <FabIcon as={Sparkles} />
        <FabLabel>Bulk Generate</FabLabel>
      </Fab>
    </Box>
  );
};

export default GenerateBulkStoriesButton;
