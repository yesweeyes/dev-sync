import React from "react";
import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";
import MaterialIcons from "@expo/vector-icons/MaterialIcons";

const NoRecordsFound = ({ message = "No records found" }) => {
  return (
    <Box className="flex-1 items-center justify-center h-full w-full">
      <MaterialIcons name="hourglass-empty" size={24} color="black" />
      <Text className="text-gray-500 mt-2 text-lg">{message}</Text>
    </Box>
  );
};

export default NoRecordsFound;
