import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router";
import "./App.css";

function App() {
  return (
    <Router>
      <div>
        <Navbar>
          <Route path="/login"></Route>
          <Route path="/register"></Route>
          <Route path="/home"></Route>
        </Navbar>
      </div>
    </Router>
  );
}

export default App;
