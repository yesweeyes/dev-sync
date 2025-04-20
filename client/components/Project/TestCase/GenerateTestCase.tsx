import { View, Text } from "react-native";
import React, { useEffect, useState } from "react";
import { Box } from "@/components/ui/box";
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";
import { Modal } from "@/components/ui/modal";
import { useAppStore } from "@/store/store";

const GenerateTestCase = () => {
  const { project_id, generateTestCase, test_cases, user_stories } =
    useAppStore();

  const handleGenerate = async () => {
    if (!project_id) return;
    generateTestCase(project_id);
  };

  const isDisabled = user_stories.length == 0;

  return (
    <Box>
      <Fab
        size="md"
        placement="bottom left"
        className="bg-gradient-to-r from-blue-500 to-purple-600 hover:scale-105 transition-transform"
        onPress={handleGenerate}
        disabled={isDisabled}
      >
        <FabIcon as={Sparkles} />
        <FabLabel>Bulk Generate</FabLabel>
      </Fab>
    </Box>
  );
};

export default GenerateTestCase;
