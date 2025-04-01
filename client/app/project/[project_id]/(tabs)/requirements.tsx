import { Box } from "@/components/ui/box";
import React, { useEffect } from "react";
import { useProjectStore } from "@/store/project";
import { useLocalSearchParams } from "expo-router";
import ProjectDocumentListView from "@/components/Project/ProjectDocumentListCard";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import { AddIcon } from "@/components/ui/icon";
import * as DocumentPicker from "expo-document-picker";
import { Alert } from "react-native";

function ProjectDocumentPage() {
  const { fetchProjectDocuments, addDocument, project } = useProjectStore();
  const { project_id } = useLocalSearchParams();

  useEffect(() => {
    fetchProjectDocuments(project_id as string);
  }, [project_id]);

  const handleDocumentSelect = async () => {
    try {
      const result = await DocumentPicker.getDocumentAsync({
        type: "*/*", // Accept all file types
        copyToCacheDirectory: true,
        multiple: false,
      });

      if (result.canceled) return;

      const file = result.assets[0];

      await addDocument({
        project_id: project?.id as string,
        file: file,
      });

      Alert.alert("Success", "Document uploaded successfully!");
    } catch (error) {
      Alert.alert("Error", "Failed to select a document.");
    }
  };

  return (
    <Box className="p-2 h-full w-full">
      <ProjectDocumentListView />
      <Fab size="md" placement="bottom right" onPress={handleDocumentSelect}>
        <FabIcon as={AddIcon} />
        <FabLabel>Add Document</FabLabel>
      </Fab>
    </Box>
  );
}

export default ProjectDocumentPage;
