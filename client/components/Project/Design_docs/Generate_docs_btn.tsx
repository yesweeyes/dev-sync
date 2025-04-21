import React from "react";
import { Box } from "@/components/ui/box";
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";
import { useAppStore } from "@/store/store"


const GenerateDesignDocs = () => {
  const { project_id, generateTechDocs} = useAppStore();

  const handleGenerate = async () => {
    if (project_id) {
      generateTechDocs({project_id});
    }
  };

  return (
    <Box>
      <Fab
        size="md"
        placement="bottom right"
        onPress={handleGenerate}
       >
        <FabIcon as={Sparkles} />
        <FabLabel>Generate Design Documents</FabLabel>
      </Fab>
    </Box>
  );
};

export default GenerateDesignDocs;
