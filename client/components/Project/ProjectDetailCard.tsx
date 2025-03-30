import { Card } from "@/components/ui/card";
import { Text } from "react-native";

const ProjectCard = ({
  name,
  description,
}: {
  name: string;
  description: string;
}) => {
  return (
    <Card className="w-full rounded-lg bg-gray-100 p-5">
      {/* <CardHeader className="text-xl font-bold">{name}</CardHeader> */}
      {/* <CardContent> */}
      <Text className="text-gray-600">{description}</Text>
      {/* </CardContent> */}
    </Card>
  );
};

export default ProjectCard;
