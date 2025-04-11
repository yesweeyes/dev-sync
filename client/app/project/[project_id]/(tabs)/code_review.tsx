import NoRecordsFound from "@/components/Common/NoRecordsFound";
import ProjectCodeReviewListView from "@/components/Project/CodeReview/ProjectCodeReviewListView";
import { Box } from "@/components/ui/box";
import { useAppStore } from "@/store/store";
import React, { useEffect } from "react";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import ProjectGenerateCodeReviewPromptModal from "@/components/Project/CodeReview/ProjectGenerateCodeReviewPromptModal";

function ProjectCodeReviewPage() {
  const { fetchProjectDocuments, addDocument, project, project_id } =
    useAppStore();

  useEffect(() => {
    fetchProjectDocuments(project_id as string);
  }, [project_id]);

  const handleDocumentSelect = async () => {};

  return (
    <Box className="p-2 h-full w-full">
      <ProjectCodeReviewListView />
      <ProjectGenerateCodeReviewPromptModal />
    </Box>
  );
}

export default ProjectCodeReviewPage;
