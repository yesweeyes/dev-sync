import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ProjectUpdate } from "@/schema/project";
import { Linking, View } from "react-native";
import { Edit, Trash } from "lucide-react-native";
import { useAppStore } from "@/store/store";
import { Heading } from "@/components/ui/heading";
import { Link, LinkText } from "@/components/ui/link";
import { Text } from "@/components/ui/text";
import { useRouter } from "expo-router";
import { useState } from "react";
import EditProjectModal from "./EditProjectModal";

const ProjectCard = () => {
  const { project, updateProject, deleteProject, fetchProject } = useAppStore();
  const [isEditModalOpen, setEditModalOpen] = useState(false);
  const router = useRouter();

  function handleProjectEdit(projectUpdateData: ProjectUpdate) {
    if (!project) return;
    updateProject(project.id, projectUpdateData);
  }

  function handleProjectDelete() {
    if (!project) return;
    deleteProject(project.id);
    router.navigate("/");
  }

  return (
    <Card className="w-full rounded-lg bg-gray-100 p-5 h-full space-y-6 font-roboto">
      {isEditModalOpen && (
        <EditProjectModal
          isOpen={isEditModalOpen}
          onClose={() => setEditModalOpen(false)}
          onUpdate={handleProjectEdit}
        />
      )}
      <Text className="text-4xl font-bold text-gray-900 font-roboto">
        {project?.name}
      </Text>
      <View className="mb-4 space-y-2">
        <Heading className="font-roboto">JIRA Integration</Heading>
        <Text className="text-gray-700" isTruncated={true}>
          <Link href={project?.jira_project_endpoint}>
            <LinkText>{project?.jira_project_endpoint}</LinkText>
          </Link>
        </Text>
        <Text className="text-gray-700 font-roboto">
          JIRA Key: {project?.jira_project_key}
        </Text>
        <Text className="text-gray-700 font-roboto">
          Email: {project?.jira_project_email}
        </Text>
        <Text className="text-gray-700 font-roboto">
          Created On:{" "}
          {project?.created_at
            ? new Date(project?.created_at).toLocaleDateString()
            : ""}
        </Text>
      </View>
      <View className="flex flex-row justify-end gap-4 mt-4">
        <Button
          className="bg-yellow-500 px-4 py-2 flex flex-row items-center rounded-lg"
          onPress={() => {
            setEditModalOpen(true);
          }}
        >
          <Edit size={16} color="white" />
        </Button>
        <Button
          className="bg-red-500 px-4 py-2 flex flex-row items-center rounded-lg"
          onPress={handleProjectDelete}
        >
          <Trash size={16} color="white" />
        </Button>
      </View>
    </Card>
  );
};

export default ProjectCard;
