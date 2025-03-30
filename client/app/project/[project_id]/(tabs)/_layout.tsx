import React from "react";
import { HStack } from "@/components/ui/hstack";
import { VStack } from "@/components/ui/vstack";
import { Box } from "@/components/ui/box";
import ProjectDetailCard from "@/components/Project/ProjectDetailCard";
import { Tabs } from "expo-router";
import FontAwesome from "@expo/vector-icons/FontAwesome";

function ProjectPageLayout() {
  return (
    <Box className="flex-1 w-full">
      <HStack className="w-full flex-1">
        {/* Left Section: Project Card */}
        <VStack
          space="md"
          className="flex-1 max-w-sm items-center justify-center bg-gray-100 p-5 rounded-xl"
        >
          <ProjectDetailCard
            name="My Project"
            description="This is my first project"
          />
        </VStack>
        <VStack className="flex-1 h-full bg-gray-50 p-5 rounded-xl">
          <Tabs screenOptions={{ tabBarActiveTintColor: "blue" }}>
            <Tabs.Screen
              name="document"
              options={{
                title: "Documents",
                tabBarIcon: ({ color }) => (
                  <FontAwesome size={28} name="file" color={color} />
                ),
              }}
            />
            <Tabs.Screen
              name="user_story"
              options={{
                title: "User Story",
                tabBarIcon: ({ color }) => (
                  <FontAwesome size={28} name="book" color={color} />
                ),
              }}
            />
            <Tabs.Screen
              name="design"
              options={{
                title: "Designn",
                tabBarIcon: ({ color }) => (
                  <FontAwesome size={28} name="code" color={color} />
                ),
              }}
            />
            <Tabs.Screen
              name="testcase"
              options={{
                title: "Testcases",
                tabBarIcon: ({ color }) => (
                  <FontAwesome size={28} name="check" color={color} />
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
