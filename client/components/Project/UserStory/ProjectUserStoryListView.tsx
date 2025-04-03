import React, { useState } from "react";
import { FlatList, Text, TouchableOpacity } from "react-native";
import {
  ChevronDown,
  ChevronUp,
  Trash2,
  Edit,
  Send,
} from "lucide-react-native";
import { Card } from "@/components/ui/card";
import { Button, ButtonIcon } from "@/components/ui/button";
import { HStack } from "@/components/ui/hstack";
import { VStack } from "@/components/ui/vstack";
import { useStore } from "@/store/store";
import { deleteUserStory, pushUserStoryToJIRA } from "@/api/user_story";
import { UserStory, UserStoryUpdate } from "@/schema/user_story";
import { Box } from "@/components/ui/box";
import EditUserStoryModal from "./EditUserStoryModal";

function UserStoryListView() {
  const { user_stories, fetchUserStories, project_id, updateUserStory } =
    useStore();
  const [expanded, setExpanded] = useState<{ [key: string]: boolean }>({});
  const [isEditModalOpen, setEditModalOpen] = useState(false);
  const [selectedStory, setSelectedStory] = useState<UserStory>();

  const handleEdit = (user_story: UserStory) => {
    setSelectedStory(user_story);
    setEditModalOpen(true);
  };

  const handleUpdate = (updatedStory: UserStoryUpdate) => {
    if (selectedStory) {
      updateUserStory(selectedStory.id, updatedStory);
    }
    setEditModalOpen(false);
  };

  const toggleExpand = (id: string) => {
    setExpanded((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  async function handleDelete(user_story_id: string) {
    if (user_story_id && project_id) {
      await deleteUserStory(user_story_id);
      fetchUserStories(project_id);
    }
  }

  async function handlePushToJIRA(user_story_id: string) {
    if (user_story_id) {
      await pushUserStoryToJIRA(user_story_id);
    }
  }

  return (
    <Box className="h-full w-full">
      <EditUserStoryModal
        isOpen={isEditModalOpen}
        onClose={() => setEditModalOpen(false)}
        onUpdate={handleUpdate}
        userStory={selectedStory}
      />

      <FlatList
        data={user_stories}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Card className="p-2 m-2 rounded-xl bg-white">
            <VStack space="md">
              <HStack className="justify-between items-center">
                <TouchableOpacity onPress={() => toggleExpand(item.id)}>
                  <HStack className="items-center space-x-2">
                    {expanded[item.id] ? (
                      <ChevronUp size={20} color="black" />
                    ) : (
                      <ChevronDown size={20} color="black" />
                    )}
                    <Text className="text-base font-roboto text-typography-black">
                      {item.title}
                    </Text>
                  </HStack>
                </TouchableOpacity>
                <HStack space="sm">
                  <Button
                    className="bg-blue-600 rounded-full w-14 h-14 items-center justify-center"
                    onPress={() => handlePushToJIRA(item.id)}
                  >
                    <ButtonIcon as={Send} size="lg" />
                  </Button>
                  <Button
                    className="bg-yellow-500 rounded-full w-14 h-14 items-center justify-center"
                    onPress={() => handleEdit(item)}
                  >
                    <ButtonIcon as={Edit} size="lg" />
                  </Button>
                  <Button
                    className="bg-red-600 rounded-full w-14 h-14 items-center justify-center"
                    onPress={() => handleDelete(item.id)}
                  >
                    <ButtonIcon as={Trash2} size="lg" />
                  </Button>
                </HStack>
              </HStack>
              {expanded[item.id] && (
                <VStack className="p-2 bg-gray-100 rounded-lg" space="sm">
                  <Text className="text-sm font-roboto text-gray-800">
                    {item.description}
                  </Text>
                  <Text className="text-sm font-roboto text-gray-600">
                    Acceptance Criteria: {item.acceptance_criteria}
                  </Text>
                  <Text className="text-sm font-roboto text-gray-600">
                    Story Points: {item.storyPoints}
                  </Text>
                  <Text className="text-sm font-roboto text-gray-600">
                    Issue Type: {item.issueType}
                  </Text>
                </VStack>
              )}
            </VStack>
          </Card>
        )}
      />
    </Box>
  );
}

export default UserStoryListView;
