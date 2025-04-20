import { Box } from "@/components/ui/box";
import React, { useCallback, useContext, useEffect } from "react";
import ProjectDocumentListView from "@/components/Project/Requirements/ProjectDocumentListView";
import ProjectAddDocumentButton from "@/components/Project/Requirements/ProjectAddDocumentButton";
import { InfoContext } from "@/components/Common/InfoContext";
import { useFocusEffect } from "expo-router";

function ProjectDocumentPage() {
  const { setInfoText } = useContext(InfoContext);
  useFocusEffect(
    useCallback(() => {
      setInfoText("Upload Project Requirement Documents to Knowledge Base");
    }, [setInfoText])
  );
  return (
    <Box className="p-2 h-full w-full">
      <ProjectDocumentListView />
      <ProjectAddDocumentButton />
    </Box>
  );
}

export default ProjectDocumentPage;
