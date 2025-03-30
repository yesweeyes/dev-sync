import { Box } from "@/components/ui/box";
import React, { useEffect } from "react";
import { useProjectStore } from "@/store/project";
import { useLocalSearchParams, useRouter } from "expo-router";
import ProjectDocumentListView from "@/components/Project/ProjectDocumentListCard";

function ProjectDocumentPage() {
  const { documents, fetchProjectDocuments } = useProjectStore();
  // const router = useRouter();
  const { project_id } = useLocalSearchParams();

  useEffect(() => {
    fetchProjectDocuments(project_id as string);
  }, []);

  return (
    <Box className="p-2">
      <ProjectDocumentListView />
    </Box>
  );
}

export default ProjectDocumentPage;
