import React from "react";
import { FlatList, ScrollView, Text } from "react-native";
import { Download, Trash2 } from "lucide-react-native";
import { RequirementDocument } from "@/schema/requirement_document";
import { Linking } from "react-native";
import { Card } from "@/components/ui/card";
import { Button, ButtonText, ButtonIcon } from "@/components/ui/button";
import { HStack } from "@/components/ui/hstack";
import { VStack } from "@/components/ui/vstack";
import { useStore } from "@/store/store";
import MaterialIcons from "@expo/vector-icons/MaterialIcons";

function ProjectDocumentListView() {
  const { documents, deleteDocument } = useStore();

  function handleDocumentDelete(documentId: string) {
    deleteDocument(documentId);
  }

  return (
    <ScrollView className="flex-1">
      <FlatList
        data={documents}
        keyExtractor={(item) => item.id}
        renderItem={({ item }: { item: RequirementDocument }) => (
          <Card className="p-2 m-2 rounded-xl bg-white">
            <HStack className="justify-between items-center" space="lg">
              <MaterialIcons name="file-present" size={24} color="black" />
              <Text className="text-base font-roboto text-typography-black flex-1">
                {item.original_name}
              </Text>
              <HStack space="sm">
                <Button
                  onPress={() => Linking.openURL(item.file_path)}
                  className="w-14 h-14 bg-blue-600 rounded-full items-center justify-center"
                >
                  <ButtonIcon as={Download} size="lg" />
                </Button>
                <Button
                  className="w-14 h-14 bg-red-600 rounded-full items-center justify-center"
                  onPress={() => handleDocumentDelete(item.id)}
                >
                  <ButtonIcon as={Trash2} size="lg" />
                </Button>
              </HStack>
            </HStack>
          </Card>
        )}
      />
    </ScrollView>
  );
}

export default ProjectDocumentListView;
