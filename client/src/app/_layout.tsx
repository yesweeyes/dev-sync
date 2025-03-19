import { GluestackUIProvider } from "@/components/ui/gluestack-ui-provider";
import { Slot } from "expo-router";

export default function RootLayout() {
  return (
    <GluestackUIProvider mode="system">
      <Slot />
    </GluestackUIProvider>
  );
}
