import React, { useContext } from "react";
import { InfoContext } from "@/components/Common/InfoContext";
import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";
import { Card } from "@/components/ui/card";
import { Info } from "lucide-react-native";

function InfoContentBox() {
  const { infoText } = useContext(InfoContext);

  return (
    <Card className="bg-sky-100 p-3 rounded-xl">
      <Box className="flex-row items-center justify-between">
        <Info color={"#0284C7"} size={20} />
        <Text className="text-sky-800 text-sm flex-1 p-2 font-roboto">
          {infoText}
        </Text>
      </Box>
    </Card>
  );
}

export default InfoContentBox;
