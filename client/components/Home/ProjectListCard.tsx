import React from "react";
import { View, Linking } from "react-native";
import { useRouter } from "expo-router";
import { Button, ButtonText, ButtonIcon } from "@/components/ui/button";
import { ArrowRight, Link } from "lucide-react-native";
import { Project } from "@/schema/project";

interface ProjectListCardProps {
  project: Project;
}

function ProjectListCard(props: ProjectListCardProps) {
  const router = useRouter();
  const { project } = props;
  return (
    <View className="flex-row items-center">
      <Button
        onPress={() => router.push(`/project/${project.id}`)}
        className={`p-8 my-1 rounded-full flex-row justify-between items-center flex-1 bg-gray-50`}
      >
        <ButtonText className="text-base font-roboto text-left text-typography-black ">
          {project.name} ({project.jira_project_key})
        </ButtonText>
        <ButtonIcon as={ArrowRight} />
      </Button>
      <Button
        onPress={() => Linking.openURL(project.jira_project_endpoint)}
        className="ml-2 mr-2 w-14 h-14 bg-blue-600 rounded-full items-center justify-center"
      >
        <ButtonIcon as={Link} size="lg" />
      </Button>
    </View>
  );
}

export default ProjectListCard;
