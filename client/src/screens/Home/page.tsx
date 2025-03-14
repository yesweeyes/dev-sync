import React, { useState } from "react";
import { Button, ButtonText } from "../../../components/ui/button";
import llmApi from "@/src/api/llmApi";
import { View, Text } from "react-native";

function Home() {
  const [message, setMessage] = useState<string>("");

  async function handleButtonPress() {
    const response = await llmApi.healthcheck();
    setMessage(response.data);
    console.log(response);
  }

  return (
    <View>
      <Button
        action={"primary"}
        variant={"solid"}
        size={"lg"}
        isDisabled={false}
        onPress={handleButtonPress}
      >
        <ButtonText>LLM Healthcheck</ButtonText>
      </Button>
      {message.length > 0 && (
        <View>
          <Text>LLM Says: {message}</Text>
        </View>
      )}
    </View>
  );
}

export default Home;
