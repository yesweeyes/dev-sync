import ProjectCodeReviewListView from "@/components/Project/CodeReview/ProjectCodeReviewListView";
import { Box } from "@/components/ui/box";
import ProjectGenerateCodeReviewPromptModal from "@/components/Project/CodeReview/ProjectGenerateCodeReviewPromptModal";
import { useCallback, useContext } from "react";
import { InfoContext } from "@/components/Common/InfoContext";
import { useFocusEffect } from "expo-router";

function ProjectCodeReviewPage() {
  const { setInfoText } = useContext(InfoContext);
  useFocusEffect(
    useCallback(() => {
      setInfoText("Generate Code Review from Github Repository");
    }, [setInfoText])
  );
  return (
    <Box className="p-2 h-full w-full">
      <ProjectCodeReviewListView />
      <ProjectGenerateCodeReviewPromptModal />
    </Box>
  );
}

export default ProjectCodeReviewPage;
