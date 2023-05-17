import React, { Fragment } from "react";
import "./Header.css";

import { Link, withRouter } from "react-router-dom";
import { isAuthenticated, signout } from "../../helper/auth";

const currentTab = (history, path) => {
  if (history.location.pathname === path) {
    return { "border-bottom": "2px solid #fff" };
  } else {
    return { "border-bottom": "none" };
  }
};

const Header = ({ history }) => {
  return (
    <div className="navbar">
      <div className="navContainer flex">
        <h1 className="logo">DepreScan</h1>
        <nav>
          <ul>
            {/* <li>
              <Link style={currentTab(history, "/")} to="/">
                <a className="link">Home</a>
              </Link>
            </li> */}
            {!isAuthenticated() && (
              <Fragment>
                <li>
                  <Link style={currentTab(history, "/signup")} to="/signup">
                    <a className="link">Sign Up</a>
                  </Link>
                </li>
                <li>
                  <Link style={currentTab(history, "/login")} to="/login">
                    <a className="link">Sign In</a>
                  </Link>
                </li>
              </Fragment>
            )}
            {isAuthenticated() && (
              <Fragment>
                <li>
                  <Link style={currentTab(history, "/")} to="/">
                    <a className="link">Dashboard</a>
                  </Link>
                </li>
                <li>
                  <a 
                    className="link"
                    onClick={() => {
                      signout(() => {
                        history.push("/")
                      })
                    }}
                  >LogOut</a>
                </li>
              </Fragment>
            )}
          </ul>
        </nav>
      </div>
    </div>
  );
};

export default withRouter(Header);
