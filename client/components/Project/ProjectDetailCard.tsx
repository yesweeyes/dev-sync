import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ProjectUpdate } from "@/schema/project";
import { Linking, View } from "react-native";
import { Edit, Trash } from "lucide-react-native";
import { useProjectStore } from "@/store/project";
import { Heading } from "@/components/ui/heading";
import { Link, LinkText } from "@/components/ui/link";
import { Text } from "@/components/ui/text";

const ProjectCard = () => {
  const { project } = useProjectStore();

  function handleProjectEdit() {}
  function handleProjectDelete() {}

  return (
    <Card className="w-full rounded-lg bg-gray-100 p-5 h-full space-y-6 font-roboto">
      <Text className="text-3xl font-bold text-gray-900">{project?.name}</Text>
      <View className="mb-4 space-y-2">
        <Heading>JIRA Integration</Heading>
        <Text className="text-gray-700" isTruncated={true}>
          <Link href={project?.jira_project_endpoint}>
            <LinkText>{project?.jira_project_endpoint}</LinkText>
          </Link>
        </Text>
        <Text className="text-gray-700">
          JIRA Key: {project?.jira_project_key}
        </Text>
        <Text className="text-gray-700">
          Email: {project?.jira_project_email}
        </Text>
        <Text className="text-gray-700">
          Created On:{" "}
          {project?.created_at
            ? new Date(project?.created_at).toLocaleDateString()
            : ""}
        </Text>
      </View>
      <View className="flex flex-row justify-end gap-4 mt-4">
        <Button
          className="bg-blue-500 px-4 py-2 flex flex-row items-center rounded-lg"
          onPress={handleProjectEdit}
        >
          <Edit size={16} color="white" />
          {/* <Text className="text-white ml-2">Edit</Text> */}
        </Button>
        <Button
          className="bg-red-500 px-4 py-2 flex flex-row items-center rounded-lg"
          onPress={handleProjectDelete}
        >
          <Trash size={16} color="white" />
          {/* <Text className="text-white ml-2">Delete</Text> */}
        </Button>
      </View>
    </Card>
  );
};

export default ProjectCard;
