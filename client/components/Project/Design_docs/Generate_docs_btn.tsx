import React from "react";
import { Box } from "@/components/ui/box";
import { Fab, FabIcon, FabLabel } from "@/components/ui/fab";
import { Sparkles } from "lucide-react-native";


const GenerateDesignDocs = () => {
  

  return (
    <Box>
      <Fab
        size="md"
        placement="bottom left"
       
      >
        <FabIcon as={Sparkles} />
        <FabLabel>Generate Design Documents </FabLabel>
      </Fab>
      <text> </text>
    </Box>
  );
};

export default GenerateDesignDocs;
