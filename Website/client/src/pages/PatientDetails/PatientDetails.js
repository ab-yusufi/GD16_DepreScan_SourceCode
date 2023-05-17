import "./PatientDetails.css";
import React, { useEffect, Fragment } from "react";
import { useParams } from "react-router-dom";
import bg_image2 from "../../assets/images/bg_image2.svg";
import profile_img from "../../assets/images/profile_img.png";
import profile_img2 from "../../assets/images/profile_img2.png";
import Base from "../Base/Base";

const PatientDetails = (props) => {
  const p = props.location.state;
  useEffect(() => {
    console.log(props.location.state.phqQuestions);
  }, []);

  return (
    <Base>
      <div className="container-fluid mt-4">
        <div className="row">
          <div className="col-12 col-md-8 offset-md-2">
            <div className="box">
              <span></span>
              <div className="content">
                <div className="row">
                  <div className="col-10 offset-1 col-md-4 offset-md-0 d-flex justify-content-center text-center ps-5">
                    <img
                      src={profile_img2}
                      className="img-fluid align-self-center border border-3 rounded-circle"
                    />
                  </div>
                  <div className="col-10 offset-1 col-md-8 offset-md-0">
                    <ul className="list-group me-0 me-md-3 mt-3 mt-md-0">
                      <li className="list-group-item bg-primary text-white">
                        ID: {p._id}
                      </li>
                      <li className="list-group-item bg-primary text-white">
                        Name: {p.patientName}
                      </li>
                      <li className="list-group-item bg-primary text-white">
                        Email: {p.patientEmail}
                      </li>
                      <li className="list-group-item bg-primary text-white">
                        Age: {p.patientAge}
                      </li>
                      <li className="list-group-item bg-primary text-white">
                        Gender: {p.patientGender}
                      </li>
                      <li className="list-group-item bg-primary text-white">
                        Phone: {p.patientPhone}
                      </li>
                    </ul>
                    <ul className="list-group me-0 mt-3 me-md-3">
                      <li className={`list-group-item ${Number(p["depression score"].slice(0,-1)) >= 50 ? "bg-danger":"bg-success"} text-white`}>
                        Depression Score: {p["depression score"]}
                      </li>
                      <li className={`list-group-item ${Number(p.enthusiasm.slice(0,-1)) >= 50 ? "bg-danger":"bg-success"} text-white`}>
                        Enthusiasm: {p.enthusiasm}
                      </li>
                      <li className={`list-group-item ${Number(p.optimisum.slice(0,-1)) >= 50 ? "bg-danger":"bg-success"} text-white`}>
                        Optimisum: {p.optimisum}
                      </li>
                      <li className={`list-group-item ${Number(p?.phqScore) >= 15 ? "bg-danger":"bg-success"} text-white`}>
                        PHQ Score: {p?.phqScore}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <h2 className="text-white text-center">Patient's Responses</h2>
            <div className="box">
              <span></span>
              
              <div className="content">
                
                <ul className="list-group mx-3">
                  <li className="list-group-item bg-transparent text-white">
                    Question 1: {p.question1}
                  </li>
                  <li
                    className={`list-group-item ${
                      p.response1.toLowerCase() == "yes"
                        ? "bg-success"
                        : "bg-danger"
                    } text-white `}
                  >
                    Patient's Response: {p.response1}
                  </li>
                  <li className="list-group-item bg-transparent text-white">
                    Question 2: {p.question2}
                  </li>
                  <li
                    className={`list-group-item ${
                      p.response2.toLowerCase() == "yes"
                        ? "bg-success"
                        : "bg-danger"
                    } text-white`}
                  >
                    Patient's Response: {p.response2}
                  </li>
                  <li className="list-group-item bg-transparent text-white">
                    Question 3: {p.question3}
                  </li>
                  <li
                    className={`list-group-item ${
                      p.response3.toLowerCase() == "yes"
                        ? "bg-success"
                        : "bg-danger"
                    } text-white`}
                  >
                    Patient's Response: {p.response3}
                  </li>
                  {/* <li className="list-group-item bg-transparent text-white">
                    Depression Score: {p["depression score"]}
                  </li>
                  <li className="list-group-item bg-transparent text-white">
                    Enthusiasm: {p.enthusiasm}
                  </li>
                  <li className="list-group-item bg-transparent text-white">
                    Optimisum: {p.optimisum}
                  </li>
                  <li className="list-group-item bg-transparent text-white">
                    PHQ Score: {p?.phqScore}
                  </li> */}
                </ul>
              </div>
            </div>
            <h2 className="text-white text-center">PHQ9 Responses</h2>

            {p.phqQuestions && p.phqResponses && (
              <div className="box">
                <span></span>
                <div className="content">
                  <ul className="list-group mx-3">
                    <li className="list-group-item bg-transparent text-white">
                      Over the last 2 weeks, how often have you been bothered by
                      any of the following problems?
                    </li>
                    {p?.phqQuestions.map((q, i) => (
                      <Fragment>
                        <li className="list-group-item bg-info text-dark">
                          {i == 0
                            ? "1. Little interest or pleasure in doing things?"
                            : q}
                        </li>
                        <li className="list-group-item bg-transparent text-white">
                          {`Response: `} {p?.phqResponses[i]}
                        </li>
                      </Fragment>
                    ))}
                  </ul>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </Base>
  );
};

export default PatientDetails;
