import "@/global.css";
import { Slot } from "expo-router";
import { GluestackUIProvider } from "@/components/ui/gluestack-ui-provider";
import { useFonts } from "expo-font";
import { Inter_400Regular, Inter_700Bold } from "@expo-google-fonts/inter";
import { ActivityIndicator } from "react-native";
import { VStack } from "@/components/ui/vstack";
import { Text } from "@/components/ui/text";
import { Box } from "@/components/ui/box";

function RootLayout() {
  const [fontsLoaded] = useFonts({
    InterRegular: Inter_400Regular,
    InterBold: Inter_700Bold,
  });

  if (!fontsLoaded) {
    return <ActivityIndicator size="large" />;
  }

  return (
    <GluestackUIProvider>
      <Box className="p-2 flex-1 w-full">
        <VStack space="xl" className="h-full w-full justify-start items-center">
          <VStack className="w-full items-start">
            <Text className="text-2xl text-typography-black font-extrabold font-roboto">
              DevSync
            </Text>
          </VStack>
          <Slot />
        </VStack>
      </Box>
    </GluestackUIProvider>
  );
}

export default RootLayout;
