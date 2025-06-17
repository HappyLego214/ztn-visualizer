import { Link } from "react-router";
import { sendRegisterData } from "./authlogic";
import { useState } from "react";

const Register = () => {
  const [passwordVisible, setPasswordVisible] = useState<boolean>(false);

  function togglePasswordVisibility() {
    setPasswordVisible((prev) => !prev);
  }

  async function handleRegisterSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    try {
      const response = await sendRegisterData(formData);
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="register-form-container">
      <div className="register-title">
        <h1>Create an Account</h1>
      </div>
      <div className="register-providers">
        <p>Microsoft</p>
        <p>Google</p>
        <p>Github</p>
      </div>
      <form
        id="register-form"
        className="register-form"
        onSubmit={handleRegisterSubmit}
      >
        <div className="register-form-input">
          <label>Username</label>
          <input name="username" type="text"></input>
        </div>
        <div className="register-form-input">
          <label>Email Address</label>
          <input name="email" type="text"></input>
        </div>
        <div className="register-form-input">
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
        <div className="register-form-input">
          <label>Confirm Password</label>
          <input name="confirmPassword" type="password"></input>
        </div>
        <div className="register-form-options">
          <div className="register-form-top-option">
            <button type="submit">Continue</button>
          </div>
          <div className="register-form-bottom-option">
            <p>Already have an account?</p>
            <Link to="/login">Sign in</Link>
          </div>
        </div>
      </form>
    </div>
  );
};

export default Register;
