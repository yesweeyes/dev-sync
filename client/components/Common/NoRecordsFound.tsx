import React from "react";
import { Image } from "react-native";
import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";

const NoRecordsFound = () => {
  return (
    <Box className="flex-1 items-center justify-center h160-full">
      <Image
        source={require("@/assets/src/no-data-found.jpg")}
        style={{ width: 400, height: 600, marginBottom: 12 }}
        resizeMode="contain"
      />
    </Box>
  );
};

export default NoRecordsFound;
