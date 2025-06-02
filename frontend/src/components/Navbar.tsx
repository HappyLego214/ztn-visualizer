import { Link } from "react-router";
import { useState } from "react";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="left-navbar-container">
        <div className="navbar-logo">Navbar Logo</div>
        <div className="site-navigation">
          <Link to="/">Generic</Link>
          <Link to="/">Generic</Link>
          <Link to="/">Generic</Link>
          <Link to="/">Generic</Link>
        </div>
      </div>
      <div className="right-navbar-container">
        <div className="login-nav">
          <Link to="/">Log in</Link>
        </div>
        <div className="register-nav">
          <Link to="/">Get started with us!</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
