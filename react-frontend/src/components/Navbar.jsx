import React from "react";
import "../styles/Navbar.css";

const NavBar = () => {
  return (
    <div className="navbar">
      <div className="company-name">WebSocket Chat App</div>
      <div className="company-logo">
        <img
          width="48"
          height="48"
          src="https://img.icons8.com/color/48/film-reel.png"
          alt="film-reel"
        />
      </div>
    </div>
  );
};

export default NavBar;
