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
import { useEffect } from "react";
import { InfoProvider } from "@/components/Common/InfoContext";
import InfoContentBox from "@/components/Common/InfoContentBox";

function RootLayout() {
  const { clearProject } = useAppStore();
  const router = useRouter();

  useEffect(() => {
    document.title = "DevSync";
  }, []);

  const openNotion = () => {
    Linking.openURL(
      "https://www.notion.so/yesweeyes/Dev-Sync-Documentation-1ce12c3598cd80b6a68ac447989bf648"
    );
  };

  return (
    <GluestackUIProvider>
      <InfoProvider>
        <Box className="flex-1 w-full h-full p-4 font-roboto">
          <VStack space="xl" className="h-full w-full">
            {/* Header Section */}
            <Box className="w-full flex-row items-center justify-between">
              {/* Left side: DevSync + Documentation */}
              <HStack space="md">
                <Text className="text-2xl font-bold text-typography-black">
                  DevSync
                </Text>
                <Pressable onPress={openNotion}>
                  <Text className="text-base text-primary underline py-1">
                    Help
                  </Text>
                </Pressable>
              </HStack>

              <InfoContentBox />

              {/* Right side: Home button */}
              <Button
                onPress={() => {
                  clearProject();
                  router.push(`/`);
                }}
              >
                <ButtonIcon as={House} variant="outline" size="xl" />
              </Button>
            </Box>

            {/* Main Content */}
            <Box className="flex-1 w-full justify-center">
              <Slot />
            </Box>
          </VStack>
        </Box>
      </InfoProvider>
    </GluestackUIProvider>
  );
}

export default RootLayout;
