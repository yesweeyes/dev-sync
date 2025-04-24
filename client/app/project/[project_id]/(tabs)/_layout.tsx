import React, { useEffect } from "react";
import { HStack } from "@/components/ui/hstack";
import { VStack } from "@/components/ui/vstack";
import { Box } from "@/components/ui/box";
import ProjectDetailCard from "@/components/Project/ProjectDetailCard";
import { Tabs, useLocalSearchParams } from "expo-router";
import { useAppStore } from "@/store/store";
import { ListChecks } from "lucide-react-native";
import { FileText } from "lucide-react-native";
import { UserRoundPen } from "lucide-react-native";
import { CodeXml } from "lucide-react-native";
import { Box as BoxIcon } from "lucide-react-native";

function ProjectPageLayout() {
  const { project_id } = useLocalSearchParams();
  const {
    fetchProject,
    documents,
    user_stories,
    test_cases,
    code_reviews,
    design_docs,
  } = useAppStore();

  useEffect(() => {
    fetchProject(project_id as string);
  }, [project_id]);

  return (
    <Box className="flex-1 w-full">
      <HStack className="w-full flex-1">
        {/* Left Section: Project Card */}
        <VStack
          space="md"
          className="flex-1 max-w-sm items-center justify-center bg-gray-100 p-5 rounded-xl h-full"
        >
          <ProjectDetailCard />
        </VStack>
        <VStack className="flex-1 h-full pl-2 rounded-xl">
          <Tabs
            screenOptions={{
              tabBarActiveTintColor: "white",
              tabBarActiveBackgroundColor: "#2563eb",
              headerShown: false,
              tabBarPosition: "top",
              tabBarStyle: {
                borderBottomWidth: 1,
              },
              tabBarLabelStyle: {
                fontSize: 14,
              },
            }}
          >
            <Tabs.Screen
              name="requirements"
              options={{
                title: `Requirement Document (${documents.length})`,
                tabBarIcon: ({ color }) => <FileText color={color} />,
              }}
            />
            <Tabs.Screen
              name="user_story"
              options={{
                title: `User Story (${user_stories.length})`,
                tabBarIcon: ({ color }) => <UserRoundPen color={color} />,
              }}
            />
            <Tabs.Screen
              name="design"
              options={{
                title: `Technical Design (${design_docs.length})`,
                tabBarIcon: ({ color }) => <BoxIcon color={color} />,
              }}
            />
            <Tabs.Screen
              name="testcase"
              options={{
                title: `Test Cases (${test_cases.length})`,
                tabBarIcon: ({ color }) => <ListChecks color={color} />,
              }}
            />
            <Tabs.Screen
              name="code_review"
              options={{
                title: `Code Review (${code_reviews.length})`,
                tabBarIcon: ({ color }) => <CodeXml color={color} />,
              }}
            />
          </Tabs>
        </VStack>
      </HStack>
    </Box>
  );
}

export default ProjectPageLayout;
