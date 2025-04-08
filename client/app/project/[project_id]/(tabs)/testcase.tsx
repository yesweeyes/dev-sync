import NoRecordsFound from "@/components/Common/NoRecordsFound";
import CreateTestCase from "@/components/Project/TestCase/CreateTestCase";
import GenerateTestCase from "@/components/Project/TestCase/GenerateTestCase";
import TestCaseListView from "@/components/Project/TestCase/TestCaseListView";
import { Box } from "@/components/ui/box";
import React from "react";

function ProjectTestcasePage() {
  return (
    <Box className="p-2 h-full w-full">
      <TestCaseListView />
      {/* <CreateTestCase /> */}
      <GenerateTestCase />
    </Box>
  );
}

export default ProjectTestcasePage;
