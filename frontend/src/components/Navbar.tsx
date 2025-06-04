import { Link } from "react-router";
import { useState } from "react";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="left-navbar-container">
        <div className="navbar-logo">
          <Link to="/">Navbar Logo</Link>
        </div>
        <div className="site-navigation">
          <Link to="/">Generic</Link>
          <Link to="/">Generic</Link>
          <Link to="/">Generic</Link>
          <Link to="/">Generic</Link>
        </div>
      </div>
      <div className="right-navbar-container">
        <div className="login-nav">
          <Link to="/login">Log in</Link>
        </div>
        <div className="register-nav">
          <Link to="/register">Get started with us!</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
