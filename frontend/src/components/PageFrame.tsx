import React from "react";
import { type PageFrameProps } from "./Interfaces";

const PageFrame: React.FC<PageFrameProps> = ({ children }) => {
  return <div className="pageframe-container">{children}</div>;
};

export default PageFrame;
