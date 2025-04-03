import React, { useState } from "react";
import { Box } from "@/components/ui/box";
import UserStoryListView from "@/components/Project/UserStory/ProjectUserStoryListView";
import ProjectGenerateUserStoryPromptModal from "@/components/Project/UserStory/ProjectGenerateUserStoryPromptModal";

function ProjectUserStoryPage() {
  return (
    <Box className="p-2 h-full w-full">
      <UserStoryListView />
      <ProjectGenerateUserStoryPromptModal />
    </Box>
  );
}

export default ProjectUserStoryPage;
