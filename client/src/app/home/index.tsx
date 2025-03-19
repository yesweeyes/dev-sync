import React, { useState } from "react";
import { Button, ButtonText } from "@/components/ui/button";
import llmApi from "@/src/api/llmApi";
import { View, Text } from "react-native";
import DocumentPickerComponent from "@/src/components/DocumentPicker";

function Home() {
  const [message, setMessage] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  async function handleButtonPress() {
    setLoading(true);
    try {
      const response = await llmApi.healthcheck();
      setMessage(response.data);
      console.log(response);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <View>
      <Text>Hello World</Text>
      <DocumentPickerComponent />
      <Button
        action={"primary"}
        variant={"solid"}
        size={"lg"}
        isDisabled={loading}
        onPress={handleButtonPress}
      >
        <Text>LLM Healthcheck</Text>
      </Button>
      {message.length > 0 && (
        <View>
          <Text ellipsizeMode="tail" numberOfLines={2}>
            LLM Says: {message}
          </Text>
        </View>
      )}
    </View>
  );
}

export default Home;
