import { BrowserRouter as Router, Routes, Route } from "react-router";
import Navbar from "./components/Navbar";
import Homepage from "./components/Homepage";
import "./App.css";

function App() {
  return (
    <Router>
      <main className="main-container">
        <Navbar />
        <Routes>
          <Route path="/login"></Route>
          <Route path="/register"></Route>
          <Route path="/" element={<Homepage />}></Route>
        </Routes>
      </main>
    </Router>
  );
}

export default App;
