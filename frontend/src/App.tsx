import { BrowserRouter as Router, Routes, Route } from "react-router";
import Navbar from "./components/Navbar";
import Homepage from "./components/Homepage";
import AuthContainer from "./components/auth/AuthContainer";
import "./App.css";

function App() {
  return (
    <Router>
      <main className="main-container">
        <Routes>
          <Route path="/" element={<Homepage />}></Route>
          <Route path="/login" element={<AuthContainer />}></Route>
          <Route path="/register"></Route>
        </Routes>
      </main>
    </Router>
  );
}

export default App;
