import React from "react";
import { useState } from "react";

const Login = () => {
  const [passwordCheck, setPasswordCheck] = useState(false);

  function handleCheck() {
    if (passwordCheck) {
      setPasswordCheck(false);
    } else {
      setPasswordCheck(true);
    }
  }

  return (
    <div className="login-form">
      <div className="login-title-container">
        <div className="login-title">
          <h2>Sign in</h2>
        </div>
        <div className="login-subtitle">
          <p>New user?</p>
          <p>Create an account</p>
        </div>
      </div>
      <div className="login-entry">
        {passwordCheck ? (
          <div className="login-email">
            <label>Enter Password</label>
            <input></input>
            <div className="login-submit-container">
              <button onClick={handleCheck}>Submit</button>
            </div>
          </div>
        ) : (
          <div className="login-email">
            <label>Email Address</label>
            <input></input>
            <div className="login-submit-container">
              <button onClick={handleCheck}>Continue</button>
            </div>
          </div>
        )}
      </div>
      <div className="login-options"></div>
    </div>
  );
};

export default Login;
