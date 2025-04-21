import { InfoContext } from "@/components/Common/InfoContext";
import NoRecordsFound from "@/components/Common/NoRecordsFound";
import GenerateDesignDocs from "@/components/Project/Design_docs/Generate_docs_btn";
import DesignDocumenntListView from "@/components/Project/Design_docs/DesignDocumentListView";

import { Box } from "@/components/ui/box";
import { useFocusEffect } from "expo-router";
import React, { useCallback, useContext } from "react";

function ProjectDesginPage() {
  const { setInfoText } = useContext(InfoContext);
  useFocusEffect(
    useCallback(() => {
      setInfoText(
        "Generate High-Level and Low-Level Design Documentation from Knowledge Base"
      );
    }, [setInfoText])
  );
  return (
    <Box className="p-2 h-full w-full " >
      <DesignDocumenntListView />
      <GenerateDesignDocs />
    </Box>
  );
}

export default ProjectDesginPage;