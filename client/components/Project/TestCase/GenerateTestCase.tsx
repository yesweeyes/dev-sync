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
    if (user_stories.length == 0) {
      alert("No user stories generated");
      return;
    }
    console.log(project_id);
    generateTestCase(project_id);
  };

  const isDisabled =
    test_cases.length >= user_stories.length && user_stories.length != 0;

  return (
    <Box>
      <Fab
        size="md"
        placement="bottom left"
        onPress={handleGenerate}
        disabled={isDisabled}
      >
        <FabIcon as={Sparkles} />
        <FabLabel>Generate Test Cases</FabLabel>
      </Fab>
    </Box>
  );
};

export default GenerateTestCase;
