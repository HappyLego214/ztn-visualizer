import { BrowserRouter as Router, Routes, Route } from "react-router";
import Navbar from "./components/Navbar";
import Homepage from "./components/Homepage";
import AuthContainer from "./components/auth/AuthContainer";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";

import "./App.css";

function App() {
  return (
    <Router>
      <main className="main-container">
        <Routes>
          <Route path="/" element={<Homepage />}></Route>
          <Route
            path="/login"
            element={
              <AuthContainer>
                <Login />
              </AuthContainer>
            }
          ></Route>
          <Route
            path="/register"
            element={
              <AuthContainer>
                <Register />
              </AuthContainer>
            }
          ></Route>
        </Routes>
      </main>
    </Router>
  );
}

export default App;
