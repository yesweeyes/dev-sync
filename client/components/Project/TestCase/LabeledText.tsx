import React from "react";
import { Text } from "react-native";

const LabeledText = ({
  label,
  value,
}: {
  label: string;
  value: string | string[];
}) => (
  <Text className="text-sm font-roboto text-gray-800">
    <Text style={{ fontWeight: "bold" }}>{label}:</Text>{" "}
    {Array.isArray(value)
      ? value.map((item, index) => (
          <Text key={index}>
            {item}
            {index < value.length - 1 ? "\n" : ""}
          </Text>
        ))
      : value}
  </Text>
);

export default LabeledText;
