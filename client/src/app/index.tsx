import { StyleSheet, Text, View } from "react-native";
import { Button, ButtonText } from "@/components/ui/button";
import { SafeAreaView } from "@/components/ui/safe-area-view";
import { VStack } from "@/components/ui/vstack";
import { router } from "expo-router";
import { Sidebar } from "@/components/Sidebar";

export default function Page() {
  return (
    <SafeAreaView className="md:flex flex-col items-center justify-center md:w-full h-full">
      <Sidebar />
    </SafeAreaView>
  );
}
