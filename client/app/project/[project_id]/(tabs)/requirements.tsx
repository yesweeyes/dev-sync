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
import axios from "axios";

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

    if (result.canceled === false) {
      const file = result.assets[0];
      const formData = new FormData();
      formData.append("project_id", project_id! as string);
      formData.append("file", {
        uri: file.uri,
        name: file.name,
        type: "application/pdf",
      });
      // try {
      //   const res = await axios.post(
      //     "http://127.0.0.1:8000/api/v1/document/upload",
      //     formData,
      //     {
      //       headers: {
      //         // DO NOT include 'Content-Type'
      //         Accept: "application/json",
      //       },
      //     }
      //   );
      //   console.log("Upload success:", res.data);
      // } catch (err) {
      //   console.error("Upload error:", err.response?.data || err.message);
      // }

      try {
        const response = await fetch(
          "http://127.0.0.1:8000/api/v1/document/upload",
          {
            method: "POST",
            headers: {
              Accept: "application/json",
              // DO NOT add 'Content-Type': fetch will set it with correct boundary
            },
            body: formData,
          }
        );

        const data = await response.json();

        if (response.ok) {
          console.log("Upload success:", data);
        } else {
          console.error("Upload error:", data);
        }
      } catch (err: any) {
        console.error("Network error:", err.message);
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
