import "@/global.css";
import { Slot } from "expo-router";
import { GluestackUIProvider } from "@/components/ui/gluestack-ui-provider";
import { VStack } from "@/components/ui/vstack";
import { Text } from "@/components/ui/text";
import { Box } from "@/components/ui/box";

function RootLayout() {
  return (
    <GluestackUIProvider>
      <Box className="flex-1 w-full h-full p-4">
        <VStack space="xl" className="h-full w-full">
          {/* Header Section */}
          <Box className="w-full items-start">
            <Text className="text-2xl font-bold text-typography-black">
              DevSync
            </Text>
          </Box>

          {/* Main Content */}
          <Box className="flex-1 w-full">
            <Slot />
          </Box>
        </VStack>
      </Box>
    </GluestackUIProvider>
  );
}

export default RootLayout;
