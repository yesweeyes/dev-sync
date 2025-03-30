import React, { useEffect } from "react";
import { HStack } from "@/components/ui/hstack";
import { VStack } from "@/components/ui/vstack";
import { Box } from "@/components/ui/box";
import ProjectDetailCard from "@/components/Project/ProjectDetailCard";
import { Tabs, useLocalSearchParams, useRouter } from "expo-router";
import MaterialIcons from "@expo/vector-icons/MaterialIcons";
import { useProjectStore } from "@/store/project";

function ProjectPageLayout() {
  const { project_id } = useLocalSearchParams();
  const { fetchProject } = useProjectStore();

  useEffect(() => {
    fetchProject(project_id as string);
  }, [project_id]);

  return (
    <Box className="flex-1 w-full">
      <HStack className="w-full flex-1">
        {/* Left Section: Project Card */}
        <VStack
          space="md"
          className="flex-1 max-w-sm items-center justify-center bg-gray-100 p-5 rounded-xl"
        >
          {/* <ProjectDetailCard /> */}
        </VStack>
        <VStack className="flex-1 h-full pl-2 rounded-xl">
          <Tabs
            screenOptions={{
              tabBarActiveTintColor: "blue",
              headerShown: false,
              tabBarPosition: "top",
              tabBarStyle: {
                borderBottomWidth: 0,
              },
            }}
          >
            <Tabs.Screen
              name="requirements"
              options={{
                title: "Requirements",
                tabBarIcon: ({ color }) => (
                  <MaterialIcons
                    name="document-scanner"
                    size={24}
                    color={color}
                  />
                ),
              }}
            />
            <Tabs.Screen
              name="user_story"
              options={{
                title: "User Story",
                tabBarIcon: ({ color }) => (
                  <MaterialIcons name="person" size={24} color={color} />
                ),
              }}
            />
            <Tabs.Screen
              name="design"
              options={{
                title: "Design",
                tabBarIcon: ({ color }) => (
                  <MaterialIcons name="engineering" size={24} color={color} />
                ),
              }}
            />
            <Tabs.Screen
              name="testcase"
              options={{
                title: "Testcases",
                tabBarIcon: ({ color }) => (
                  <MaterialIcons name="check-box" size={24} color={color} />
                ),
              }}
            />
            <Tabs.Screen
              name="code_review"
              options={{
                title: "Code Review",
                tabBarIcon: ({ color }) => (
                  <MaterialIcons name="code" size={24} color={color} />
                ),
              }}
            />
          </Tabs>
        </VStack>
      </HStack>
    </Box>
  );
}

export default ProjectPageLayout;
