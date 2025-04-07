import "@/global.css";
import { Slot } from "expo-router";
import { useRouter } from "expo-router";
import { GluestackUIProvider } from "@/components/ui/gluestack-ui-provider";
import { VStack } from "@/components/ui/vstack";
import { HStack } from "@/components/ui/hstack";
import { Text } from "@/components/ui/text";
import { Box } from "@/components/ui/box";
import { Button, ButtonIcon } from "@/components/ui/button";
import { House } from "lucide-react-native";
import { Pressable, Linking } from "react-native";
import { useAppStore } from "@/store/store";

function RootLayout() {
  const { clearProject } = useAppStore();
  const router = useRouter();

  const openNotion = () => {
    Linking.openURL(
      "https://www.notion.so/yesweeyes/Dev-Sync-Documentation-1ce12c3598cd80b6a68ac447989bf648"
    );
  };

  return (
    <GluestackUIProvider>
      <Box className="flex-1 w-full h-full p-4">
        <VStack space="xl" className="h-full w-full">
          {/* Header Section */}
          <Box className="w-full flex-row items-center justify-between">
            <Text className="text-2xl font-bold text-typography-black">
              DevSync
            </Text>
            <HStack space="md">
              <Pressable onPress={openNotion}>
                <Text className="text-base text-primary underline py-2">
                  Documentation
                </Text>
              </Pressable>
              <Button
                onPress={() => {
                  clearProject();
                  router.push(`/`);
                }}
              >
                <ButtonIcon as={House} variant="outline" size="xl" />
              </Button>
            </HStack>
          </Box>

          {/* Main Content */}
          <Box className="flex-1 w-full justify-center">
            <Slot />
          </Box>
        </VStack>
      </Box>
    </GluestackUIProvider>
  );
}

export default RootLayout;
