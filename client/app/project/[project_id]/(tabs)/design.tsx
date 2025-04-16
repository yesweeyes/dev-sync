import NoRecordsFound from "@/components/Common/NoRecordsFound";
import GenerateDesignDocs from "@/components/Project/Design_docs/Generate_docs_btn";
import { Box } from "@/components/ui/box";
import React from "react";

function ProjectDesginPage() {
  return (
    <Box className="p-2 h-full w-full">
      <GenerateDesignDocs/>
    
    </Box>
  );
}

export default ProjectDesginPage;