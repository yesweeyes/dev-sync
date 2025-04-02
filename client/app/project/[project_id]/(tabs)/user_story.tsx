import UserStoryListView from "@/components/Project/ProjectUserStoryListView";
import { Box } from "@/components/ui/box";
import React from "react";

function ProjectUserStoryPage() {
  return (
    <Box className="p-2 h-full w-full">
      <UserStoryListView />
    </Box>
  );
}

export default ProjectUserStoryPage;
