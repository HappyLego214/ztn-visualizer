import React from "react";
import PageFrame from "./PageFrame";
import Navbar from "./Navbar";

const Homepage = () => {
  return (
    <div className="homepage-container">
      <Navbar />
      <PageFrame>1</PageFrame>
      <PageFrame>2</PageFrame>
      <PageFrame>3</PageFrame>
    </div>
  );
};

export default Homepage;
