import React, { useCallback, useContext, useEffect, useState } from "react";
import { Box } from "@/components/ui/box";
import UserStoryListView from "@/components/Project/UserStory/ProjectUserStoryListView";
import ProjectGenerateUserStoryPromptModal from "@/components/Project/UserStory/ProjectGenerateUserStoryPromptModal";
import CreateUserStoryModal from "@/components/Project/UserStory/CreateUserStoryModal";
import { InfoContext } from "@/components/Common/InfoContext";
import { useFocusEffect } from "expo-router";

function ProjectUserStoryPage() {
  const { setInfoText } = useContext(InfoContext);
  useFocusEffect(
    useCallback(() => {
      setInfoText(
        "Generate/Create User Stories using Knowledge Base - Custom Prompt, Bulk or Granular"
      );
    }, [setInfoText])
  );
  return (
    <Box className="p-2 h-full w-full">
      <UserStoryListView />
      <CreateUserStoryModal />
      <ProjectGenerateUserStoryPromptModal />
    </Box>
  );
}

export default ProjectUserStoryPage;
