import React, { useState } from "react";
import { Box } from "@/components/ui/box";
import UserStoryListView from "@/components/Project/UserStory/ProjectUserStoryListView";
import ProjectGenerateUserStoryPromptModal from "@/components/Project/UserStory/ProjectGenerateUserStoryPromptModal";
import CreateUserStoryModal from "@/components/Project/UserStory/CreateUserStoryModal";
import BulkStoriesBtn from "@/components/Project/UserStory/BulkStoriesBtn";

function ProjectUserStoryPage() {
  return (
    <Box className="p-2 h-full w-full">
      <UserStoryListView />
      <CreateUserStoryModal />
      <ProjectGenerateUserStoryPromptModal />
      <BulkStoriesBtn />
    </Box>
  );
}

export default ProjectUserStoryPage;
