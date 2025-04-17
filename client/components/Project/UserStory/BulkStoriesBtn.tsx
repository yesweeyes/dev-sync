import { View, Text } from "react-native";
import React, { useEffect, useState } from "react";
import { Box } from "@/components/ui/box";
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";
import { useAppStore } from "@/store/store";

const BulkStoriesBtn = () => {
  const { project_id, generateUserStories } = useAppStore();
  const handleSubmit = async () => {
    if (!project_id) return;
    await generateUserStories({
      project_id: project_id,
      user_prompt:
        "Generate user stories for all the content including functional and non functional",
    });
  };
  return (
    <Box>
      <Fab size="md" placement="bottom center" onPress={handleSubmit}>
        <FabIcon as={Sparkles} />
        <FabLabel>Bulk User Stories</FabLabel>
      </Fab>
    </Box>
  );
};

export default BulkStoriesBtn;
