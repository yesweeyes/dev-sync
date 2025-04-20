import React from "react";
import { Fab, FabLabel, FabIcon } from "@/components/ui/fab";
import { AddIcon } from "@/components/ui/icon";
import * as DocumentPicker from "expo-document-picker";
import { useAppStore } from "@/store/store";
import { Box } from "@/components/ui/box";

function ProjectAddDocumentButton() {
  const { addDocument, project_id } = useAppStore();

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
      } catch (err: any) {
        console.error("Network error:", err.message);
      }
    }
  };
  return (
    <Box>
      <Fab
        size="md"
        placement="bottom right"
        className="hover:scale-105 transition-transform"
        onPress={handleDocumentSelect}
      >
        <FabIcon as={AddIcon} />
        <FabLabel>Add</FabLabel>
      </Fab>
    </Box>
  );
}

export default ProjectAddDocumentButton;
