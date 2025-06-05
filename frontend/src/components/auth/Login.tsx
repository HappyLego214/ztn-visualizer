import React from "react";
import { useState } from "react";

const Login = () => {
  const [passwordVisible, setPasswordVisible] = useState<boolean>(false);

  function togglePasswordVisibility() {
    setPasswordVisible((prev) => !prev);
  }

  return (
    <div className="login-form-container">
      <div className="login-title-container">
        <div className="login-title">
          <h2>Sign in</h2>
        </div>
        <div className="login-email-subtitle">
          <p>New user?</p>
          <p>Create an account</p>
        </div>
      </div>
      <form id="login-form" className="login-entry">
        <div className="login-inputs">
          <label>Email Address</label>
          <input name="email" type="email"></input>
        </div>
        <div className="login-inputs">
          <label>Password</label>
          <div className="password-container">
            {passwordVisible ? (
              <>
                <input name="password" type="text"></input>
                <span
                  className="material-symbols-outlined"
                  onClick={togglePasswordVisibility}
                >
                  visibility
                </span>
              </>
            ) : (
              <>
                <input name="password" type="password"></input>
                <span
                  onClick={togglePasswordVisibility}
                  className="material-symbols-outlined"
                >
                  visibility_off
                </span>
              </>
            )}
          </div>
        </div>
        <div className="login-options-container">
          <div className="login-options">
            <div className="login-signedin-container">
              <input type="checkbox"></input>
              <label>Stay signed in</label>
            </div>
            <div className="login-forget-container">
              <p>Reset your password</p>
            </div>
          </div>
          <div className="login-submit-container">
            <button type="submit">Continue</button>
          </div>
        </div>
      </form>
      <div className="login-options"></div>
    </div>
  );
};

export default Login;
