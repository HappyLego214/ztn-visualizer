import React from "react";
import { type AuthContainerProps } from "../Interfaces";

const AuthContainer = ({ children }: AuthContainerProps) => {
  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="logo-box">
          <h1>Logo</h1>
        </div>
        <div className="auth-form">{children}</div>
      </div>
    </div>
  );
};

export default AuthContainer;
