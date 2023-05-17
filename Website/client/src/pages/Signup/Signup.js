import React, { useState } from "react";
import "./Signup.css";

import { signup, isAuthenticated } from "../../helper/auth";
import { Link, Redirect } from "react-router-dom";
import Base from "../Base/Base";
import bg_image2 from "../../assets/images/bg_image2.svg";

const Signup = () => {
  const [values, setValues] = useState({
    name: "",
    username: "",
    email: "",
    password: "",
    error: "",
    success: false,
  });
  const [isLoading, setIsLoading] = useState(false);

  const { name, email, password, username, error, success } = values;

  const {user} = isAuthenticated();

  const handleChange = (name) => (event) => {
    setValues({ ...values, error: false, [name]: event.target.value });
  };

  const onSubmit = (event) => {
    setIsLoading(true);
    event.preventDefault();
    setValues({ ...values, error: false, success: false });
    signup({ name, email, password, username })
      .then((data) => {
        if (data.error) {
          setValues({ ...values, error: data.error, success: false });
        } else {
          setValues({
            ...values,
            name: "",
            username: "",
            email: "",
            password: "",
            success: true,
          });
          setIsLoading(false);
        }
      })
      .catch((err) => console.log("Error in signup", err));
  };

  const performRedirect = () => {
    if (isAuthenticated()) {
      return <Redirect to="/" />;
    }
  };

  const signUpForm = () => {
    return (
      <div className="container signup-mode">
        <div className="formImg signup">
          <div>
            <h2>Join Now!</h2>
            <h3>Explore Millions of Opportunities</h3>
          </div>
          <img src={bg_image2} />
        </div>
        <div className="form signup">
          <h2>SignUp Form</h2>
          <div className="errorContainer">
            <div>
              <input
                type="text"
                placeholder="Name"
                onChange={handleChange("name")}
                value={name}
              />
            </div>
            <div>
              <input
                type="text"
                placeholder="Username"
                onChange={handleChange("username")}
                value={username}
              />
            </div>
          </div>
          <div className="email">
            <input
              type="email"
              placeholder="Email Address"
              onChange={handleChange("email")}
              value={email}
            />
          </div>
          <div className="email errorContainer">
            <input
              type="password"
              placeholder="Password"
              onChange={handleChange("password")}
              value={password}
            />
          </div>
          <button className="myBtn" onClick={onSubmit}>
            {isLoading ? "Loading...":"Sign Up"}
          </button>
          <p className="signup">
            Already Have an Account? <Link to="/login"><span id="loginHere">LogIn Here</span></Link>
          </p>
          <p className="successMessage" style={{display: success ? "" : "none"}}>Account Created Successfully. Please Login</p>
          <p className="errorMessage" style={{display: error ? "" : "none"}}>Error: Sign Up Failed</p>
        </div>
      </div>
    );
  };

  const successMessage = () => {
    return (
      <div className="row">
        <div className="col-md-6 offset-sm-3 text-left">
          <div
            className="alert alert-success"
            style={{ display: success ? "" : "none" }}
          >
            New account was created successfully. Please
            <Link to="/signin">Login Here</Link>
          </div>
        </div>
      </div>
    );
  };

  const errorMessage = () => {
    return (
      <div className="row">
        <div className="col-md-6 offset-sm-3 text-left">
          <div
            className="alert alert-danger"
            style={{ display: error ? "" : "none" }}
          >
            {error}
          </div>
        </div>
      </div>
    );
  };

  return (
    <Base>
      <div className="mainContainer">{signUpForm()}</div>
      {performRedirect()}
    </Base>
  );
};

export default Signup;
