import { InfoContext } from "@/components/Common/InfoContext";
import NoRecordsFound from "@/components/Common/NoRecordsFound";
import CreateTestCase from "@/components/Project/TestCase/CreateTestCase";
import GenerateTestCase from "@/components/Project/TestCase/GenerateTestCase";
import TestCaseListView from "@/components/Project/TestCase/TestCaseListView";
import { Box } from "@/components/ui/box";
import { useFocusEffect } from "expo-router";
import React, { useCallback, useContext } from "react";

function ProjectTestcasePage() {
  const { setInfoText } = useContext(InfoContext);
  useFocusEffect(
    useCallback(() => {
      setInfoText("Generate/Create Test Cases from existing User Stories");
    }, [setInfoText])
  );
  return (
    <Box className="p-2 h-full w-full">
      <TestCaseListView />
      <CreateTestCase />
      <GenerateTestCase />
    </Box>
  );
}

export default ProjectTestcasePage;
