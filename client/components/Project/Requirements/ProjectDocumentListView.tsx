import React from "react";
import { FlatList, ScrollView, Text } from "react-native";
import { ExternalLink, Trash2 } from "lucide-react-native";
import { RequirementDocument } from "@/schema/requirement_document";
import { Linking } from "react-native";
import { Card } from "@/components/ui/card";
import { Button, ButtonText, ButtonIcon } from "@/components/ui/button";
import { HStack } from "@/components/ui/hstack";
import { VStack } from "@/components/ui/vstack";
import { Box } from "@/components/ui/box";
import { useAppStore } from "@/store/store";
import MaterialIcons from "@expo/vector-icons/MaterialIcons";
import NoRecordsFound from "@/components/Common/NoRecordsFound";

function ProjectDocumentListView() {
  const { documents, deleteDocument } = useAppStore();

  function handleDocumentDelete(documentId: string) {
    deleteDocument(documentId);
  }

  return (
    <Box className="flex-1 h-full w-full">
      {documents.length === 0 ? (
        <NoRecordsFound />
      ) : (
        <FlatList
          className="pb-40"
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
                    onPress={() => {
                      const BACKEND_BASE_URL = "http://127.0.0.1:8000/api/v1"; // or from env
                      const fileUrl = `${BACKEND_BASE_URL}/${item.file_path}`;
                      Linking.openURL(fileUrl);
                    }}
                    className="w-14 h-14 bg-blue-600 rounded-full items-center justify-center"
                  >
                    <ButtonIcon as={ExternalLink} size="lg" />
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
      )}
    </Box>
  );
}

export default ProjectDocumentListView;
