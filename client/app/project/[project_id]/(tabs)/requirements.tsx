import { Box } from "@/components/ui/box";
import React, { useEffect } from "react";
import { useAppStore } from "@/store/store";
import { useLocalSearchParams } from "expo-router";
import ProjectDocumentListView from "@/components/Project/Requirements/ProjectDocumentListView";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import { AddIcon } from "@/components/ui/icon";
import * as DocumentPicker from "expo-document-picker";
import { Alert } from "react-native";

function ProjectDocumentPage() {
  const { fetchProjectDocuments, addDocument, project, project_id } =
    useAppStore();

  useEffect(() => {
    fetchProjectDocuments(project_id as string);
  }, [project_id]);

  const handleDocumentSelect = async () => {
    const result = await DocumentPicker.getDocumentAsync({
      type: "application/pdf",
      copyToCacheDirectory: true,
    });

    if (!result.canceled && project_id) {
      const file = result.assets[0];
      const blob = await fetch(file.uri).then((res) => res.blob());
      const blob_file = new File([blob], file.name, {
        type: file.mimeType || "application/pdf",
      });

      try {
        addDocument({ project_id: project_id, file: blob_file });
        Alert.alert("File has been uploaded sucessfully");
      } catch (err: any) {
        console.error("Network error:", err.message);
        Alert.alert("Error encountered");
      }
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
