import React from "react";
import Login from "./Login";

const AuthContainer = () => {
  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="logo-box">
          <h1>Logo</h1>
        </div>
        <div className="auth-form">
          <Login></Login>
        </div>
      </div>
    </div>
  );
};

export default AuthContainer;
