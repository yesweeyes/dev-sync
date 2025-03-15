import { StatusBar } from "expo-status-bar";
import "@/global.css";
import { GluestackUIProvider } from "@/components/ui/gluestack-ui-provider";
import { StyleSheet, Text, View } from "react-native";
import "./global.css";
import Home from "./src/screens/Home/page";

export default function App() {
  return (
    <GluestackUIProvider mode="dark">
      <View style={styles.container}>
        <StatusBar style="auto" />
        <Home />
      </View>
    </GluestackUIProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
