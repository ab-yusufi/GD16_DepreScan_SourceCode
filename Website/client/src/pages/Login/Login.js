import React, { useState } from "react";
import "./Login.css";
import bg_image2 from "../../assets/images/bg_image2.svg";

import Base from "../Base/Base";
import { signin, authenticate, isAuthenticated } from "../../helper/auth";

import {Link, Redirect} from 'react-router-dom'

const Login = () => {
  const [values, setValues] = useState({
    email: "",
    password: "",
    error: "",
    success: false,
    loading: false,
    didRedirect: false,
  });

  const {user} = isAuthenticated();

  const { email, password, error, success, didRedirect, loading } = values;

  const handleChange = (name) => (event) => {
    setValues({ ...values, error: false, [name]: event.target.value });
  };

  const onSubmit = (event) => {
    event.preventDefault();
    setValues({ ...values, error: false, success: false, loading: true });
    signin({ email, password })
      .then((data) => {
        if (data.error) {
          setValues({ ...values, error: data.error, success: false, loading: false });
        } else {
          authenticate(data, () => {
            setValues({
              ...values,
              didRedirect: true
            });
          });
        }
      })
      .catch(console.log("Error in login"));
  };

  const performRedirect = () => {
    if (didRedirect) {
      if (user && user.role === 1) {
        return <Redirect to="/" />;
      } else {
        return <Redirect to="/" />;
      }
    }
    if (isAuthenticated()) {
      return <Redirect to="/" />;
    }
  };

  const loginForm = () => {
    return (
      <div className="mainContainer">
        <div className="login-container">
          <div className="formImg signin">
            <div>
              <h2>Login Here!</h2>
              <h3>We've Missed You A Lot</h3>
            </div>
            <img src={bg_image2} />
          </div>
          <div className="form signin">
            <h2>Login Form</h2>
            <div>
              <input 
                type="email" 
                placeholder="Email Address"
                onChange={handleChange("email")}
                value={email}
                />
            </div>
            <div>
              <input 
                type="password" 
                placeholder="Password"
                onChange={handleChange("password")}
                value={password}
                />
            </div>
            <button className="myBtn" onClick={onSubmit}>{loading ? "Loading..." : "Log In"}</button>
            <p
              className="successMessage"
              style={{ display: success ? "" : "none" }}
            >
              Login Successful
            </p>
            <p
              className="errorMessage"
              style={{ display: error ? "" : "none" }}
            >
              Error: Login Failed
            </p>
            <p className="forgot">Forgot Password?</p>
            <p className="signup">
              Don't Have an Account? <Link to="/signup"><span id="joinHere">Join Here</span></Link>
            </p>
            
          </div>
        </div>
      </div>
    );
  };

  return (
  <Base>
    {loginForm()}
    {performRedirect()}
  </Base>);
};

export default Login;
