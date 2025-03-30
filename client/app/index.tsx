import { FlatList, ScrollView, Pressable, View, Linking } from "react-native";
import { useRouter } from "expo-router";
import { createProject, getAllProjects } from "../api/project";
import { Box } from "@/components/ui/box";
import { Button, ButtonText, ButtonIcon } from "@/components/ui/button";
import { useEffect, useState } from "react";
import { Project, ProjectCreate } from "@/schema/project";
import { Text } from "@/components/ui/text";
import { VStack } from "@/components/ui/vstack";
import { HStack } from "@/components/ui/hstack";
import { Plus } from "lucide-react-native";
import CreateProjectModal from "@/components/Home/CreateProjectModal";
import ProjectListCard from "@/components/Home/ProjectListCard";

function HomePage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [isCreateModalOpen, setIsCreateModalOpen] = useState<boolean>(false);

  async function fetchProjects() {
    try {
      const response = await getAllProjects();
      if (Array.isArray(response)) {
        setProjects(response);
      } else {
        setProjects([]);
      }
    } catch (error) {
      console.error(error);
      setProjects([]);
    }
  }

  async function handleSubmit(project: ProjectCreate) {
    try {
      await createProject(project);
    } catch (error) {
      console.error(error);
    } finally {
      fetchProjects();
    }
  }

  useEffect(() => {
    fetchProjects();
  }, []);

  return (
    <Box className="flex-1 w-full">
      {isCreateModalOpen && (
        <CreateProjectModal
          isOpen={isCreateModalOpen}
          onClose={() => {
            setIsCreateModalOpen(false);
          }}
          onCreate={handleSubmit}
        />
      )}
      <HStack space="xl" className="w-full flex-1">
        {/* Left Section: Create Project (Centered) */}
        <VStack
          space="md"
          className="flex-1 max-w-sm items-center justify-center bg-gray-100 p-5 rounded-xl"
        >
          {/* Create Project Section */}
          <HStack className="items-center justify-center flex-wrap">
            <Text className="text-6xl text-blue-600 font-semibold font-roboto ">
              create
            </Text>
            <Text className="text-6xl text-typography-black font-semibold font-roboto">
              project
            </Text>
          </HStack>

          <Button
            className="mt-10 px-6 py-4 rounded-full flex-row items-center  bg-blue-600"
            onPress={() => setIsCreateModalOpen(true)}
          >
            <ButtonIcon as={Plus} size="md" />
            <ButtonText className="text-xl font-bold">Project</ButtonText>
          </Button>
        </VStack>

        {/* Right Section: Project List + Navigate to Project */}
        <VStack className="flex-1 h-full bg-gray-50 p-5 rounded-xl">
          {/* Navigate to Project Section (Above List) */}
          <VStack className="w-full items-center mb-5">
            <HStack className="items-center justify-center p-2">
              <Text className="text-6xl text-blue-600 font-semibold font-roboto">
                open&nbsp;
              </Text>
              <Text className="text-6xl text-typography-black font-semibold font-roboto">
                project
              </Text>
            </HStack>
          </VStack>

          <ScrollView className="h-full">
            <FlatList
              data={projects.filter((item) => item?.id)}
              keyExtractor={(item, index) =>
                item?.id ? item.id.toString() : `fallback-${index}`
              }
              renderItem={({ item, index }) => (
                <ProjectListCard project={item} />
              )}
            />
          </ScrollView>
        </VStack>
      </HStack>
    </Box>
  );
}

export default HomePage;
