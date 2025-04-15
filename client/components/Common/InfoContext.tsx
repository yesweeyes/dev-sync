import React, { createContext, useState, ReactNode } from "react";

type InfoContextType = {
  infoText: string;
  setInfoText: (text: string) => void;
};

export const InfoContext = createContext<InfoContextType>({
  infoText: "",
  setInfoText: () => {},
});

type Props = {
  children: ReactNode;
};

export const InfoProvider: React.FC<Props> = ({ children }) => {
  const [infoText, setInfoText] = useState("Welcome!");

  return (
    <InfoContext.Provider value={{ infoText, setInfoText }}>
      {children}
    </InfoContext.Provider>
  );
};
