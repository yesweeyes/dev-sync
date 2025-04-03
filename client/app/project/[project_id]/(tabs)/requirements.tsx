import { Box } from "@/components/ui/box";
import React, { useEffect } from "react";
import { useAppStore } from "@/store/store";
import { useLocalSearchParams } from "expo-router";
import ProjectDocumentListView from "@/components/Project/Requirements/ProjectDocumentListView";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import { AddIcon } from "@/components/ui/icon";
import * as DocumentPicker from "expo-document-picker";
import { Alert } from "react-native";
import { api_form_data } from "@/api/api";

function ProjectDocumentPage() {
  const { fetchProjectDocuments, addDocument, project } = useAppStore();
  const { project_id } = useLocalSearchParams();

  useEffect(() => {
    fetchProjectDocuments(project_id as string);
  }, [project_id]);

  const handleDocumentSelect = async () => {
    try {
      const result = await DocumentPicker.getDocumentAsync({
        type: "*/*", // Accept all file types
        copyToCacheDirectory: false,
        multiple: false,
      });

      if (result.canceled || !result.assets.length || !project) {
        console.log("File selection cancelled");
        return;
      }

      const file = result.assets[0];

      // await addDocument({
      //   project_id: project?.id as string,
      //   file: file,
      // });
      const formData = new FormData();
      formData.append("project_id", project.id);
      // formData.append("file", {
      //   uri: file.uri,
      //   name: file.name,
      //   type: file.mimeType || "application/pdf",
      // });

      const response = await api_form_data.post("/document/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data", // Ensure correct format
        },
      });

      console.log("File uploaded successfully:", response.data);

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
