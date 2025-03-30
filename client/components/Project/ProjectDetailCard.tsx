import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Project } from "@/schema/project";
import { Text, View } from "react-native";
import { Edit, Trash } from "lucide-react-native";

interface ProjectDetailCardProps {
  project: Project;
  onEdit: (project: Project) => void;
  onDelete: (projectId: string) => void;
}

const ProjectCard = ({ project, onEdit, onDelete }: ProjectDetailCardProps) => {
  return (
    <Card className="w-full rounded-lg bg-gray-100 p-5 shadow-md">
      {/* <CardHeader> */}
      <Text className="text-xl font-bold text-gray-900">{project.name}</Text>
      {/* </CardHeader> */}
      {/* <CardContent> */}
      <View className="mb-2">
        <Text className="text-gray-700">
          JIRA Key: {project.jira_project_key}
        </Text>
        <Text className="text-gray-700">
          Email: {project.jira_project_email}
        </Text>
        <Text className="text-gray-700">
          Created: {new Date(project.created_at).toDateString()}
        </Text>
      </View>
      {/* </CardContent> */}
      {/* <CardFooter className="flex flex-row justify-end gap-3"> */}
      <Button
        className="bg-blue-500 px-3 py-2 rounded-lg"
        onPress={() => onEdit(project)}
      >
        <Edit size={16} color="white" />
        <Text className="text-white ml-2">Edit</Text>
      </Button>
      <Button
        className="bg-red-500 px-3 py-2 rounded-lg"
        onPress={() => onDelete(project.id)}
      >
        <Trash size={16} color="white" />
        <Text className="text-white ml-2">Delete</Text>
      </Button>
      {/* </CardFooter> */}
    </Card>
  );
};

export default ProjectCard;
