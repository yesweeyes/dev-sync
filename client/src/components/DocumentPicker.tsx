import * as DocumentPicker from "expo-document-picker";
import { Button } from "@/components/ui/button";
import { useState } from "react";
import { View, Text } from "react-native";

function DocumentPickerComponent() {
  const [document, setDocument] =
    useState<DocumentPicker.DocumentPickerAsset>();
  const [uploading, setUploading] = useState<boolean>(false);
  const selectDocument = async () => {
    const result = await DocumentPicker.getDocumentAsync({
      copyToCacheDirectory: true,
      multiple: false,
      type: "*.pdf",
    });

    if (result.canceled === true) {
    } else {
      setDocument(result.assets[0]);
      setUploading(true);
      setUploading(false);
    }
  };

  return (
    <View>
      <Button onPress={selectDocument}>
        <Text>Choose File!</Text>
      </Button>
    </View>
  );
}

export default DocumentPickerComponent;
