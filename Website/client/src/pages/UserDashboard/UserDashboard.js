import React, { useEffect, useState } from "react";
import "./UserDashboard.css";

import Base from "../Base/Base";
import { Redirect } from "react-router";
import PrimaryButton from "../../components/PrimaryButton/PrimaryButton";
import { Link } from "react-router-dom";
import { getAllPatients } from "../../helper/patient";

const UserDashboard = () => {
  const [patients, setPatients] = useState();
  const [isRefresh, setIsRefreshed] = useState();
  const [isLoading, setIsLoading] = useState(true);
  const [searchVal, setSearchVal] = useState("");
  const [searchResult, setSearchResult] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const [searchByWhat, setSearchByWhat] = useState("Select");

  const colors = [
    "bg-primary",
    "bg-success",
    "bg-warning",
    "bg-danger",
    "bg-info",
    "bg-secondary",
  ];

  const btnColors = [
    "btn-info",
    "btn-warning",
    "btn-danger",
    "btn-success",
    "btn-primary",
  ];

  useEffect(() => {
    getAllPatients()
      .then((allP) => {
        setPatients(allP);
      })
      .then(() => {
        setIsLoading(false);
      })
      .catch((err) => console.log(err));
  }, [isRefresh, isSearching]);

  const handleSearch = () => {
    setIsSearching(true);
    if (searchVal === "") {
      setPatients(patients);
      return;
    }
    const filterBySearch = patients.filter((p) => {
      console.log(patients);
      switch (searchByWhat) {
        case "Name":
          if (p.patientName) {
            if (p.patientName.toLowerCase().includes(searchVal.toLowerCase())) {
              return p;
            }
          }
          break;
        case "Email":
          if (p.patientEmail) {
            if (
              p.patientEmail.toLowerCase().includes(searchVal.toLowerCase())
            ) {
              return p;
            }
          }
          break;
        case "Age":
          if (p.patientAge) {
            if (p.patientAge.toLowerCase().includes(searchVal.toLowerCase())) {
              return p;
            }
          }
          break;
        case "Phone Number":
          if (p.patientPhone) {
            if (
              p.patientPhone.toLowerCase().includes(searchVal.toLowerCase())
            ) {
              return p;
            }
          }
          break;
        case "Gender":
          if (p.patientGender) {
            if (
              p.patientGender.toLowerCase().includes(searchVal.toLowerCase())
            ) {
              return p;
            }
          }
          break;
      }
    });
    setSearchResult(filterBySearch);
  };

  return (
    <Base>
      <div className="heading">
        <h1 className="text-white">Welcome to Dashboard</h1>
      </div>
      <div className="row user-dashboard">
        <div className="col-10 offset-1 col-md-8 offset-md-2">
          <div className="input-group py-3">
            <input
              type="text"
              className="form-control w-50 search-input"
              placeholder="Search..."
              value={searchVal}
              onChange={(e) => {
                setSearchVal(e.target.value);
                if (e.target.value == "") {
                  setIsSearching(false);
                }
              }}
            />
            <button className="btn btn-primary" onClick={() => handleSearch()}>
              Search
            </button>
            {/* <button
              class="btn btn-warning dropdown-toggle d-inline"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              {searchByWhat}
            </button>
            <ul className="dropdown-menu">
              <li onClick={() => setSearchByWhat("Name")}>
                <a className="dropdown-item" href="#">
                  Name
                </a>
              </li>
              <li onClick={() => setSearchByWhat("Email")}>
                <a className="dropdown-item" href="#">
                  Email
                </a>
              </li>
              <li onClick={() => setSearchByWhat("Age")}>
                <a className="dropdown-item" href="#">
                  Age
                </a>
              </li>
              <li onClick={() => setSearchByWhat("Phone Number")}>
                <a className="dropdown-item" href="#">
                  Phone Number
                </a>
              </li>
              <li onClick={() => setSearchByWhat("Gender")}>
                <a className="dropdown-item" href="#">
                  Gender
                </a>
              </li>
            </ul> */}
          </div>
          <div className="input-group mb-3 -warning">
            <label className="input-group-text bg-info">{searchByWhat}</label>
            <select
              className="form-select bg-info"
              onChange={(e) => setSearchByWhat(e.target.value)}
            >
              <option selected disabled className="bg-white">
                Search By...
              </option>
              <option value="Name" className="bg-white text-dark">
                Name
              </option>
              <option value="Email" className="bg-white text-dark">
                Email
              </option>
              <option value="Age" className="bg-white text-dark">
                Age
              </option>
              <option value="Phone Number" className="bg-white text-dark">
                Phone Number
              </option>
              <option value="Gender" className="bg-white text-dark">
                Gender
              </option>
            </select>
          </div>
          <div className="table-responsive">
            <table className="table table-bordered text-center text-white">
              <thead>
                <tr className="bg-dark text-white">
                  <th>Patient Name</th>
                  <th>Email</th>
                  <th className="d-none d-md-table-cell">Age</th>
                  <th className="d-none d-md-table-cell">Gender</th>
                  <th className="d-none d-md-table-cell">Phone</th>
                  {/* <th>Depression Score</th>
                <th>Enthusiasm</th>
                <th>Optimisum</th> */}
                </tr>
              </thead>
              <tbody>
                {isSearching ? (
                  isLoading ? (
                    <div class="spinner-border" role="status">
                      <span class="visually-hidden">Loading...</span>
                    </div>
                  ) : (
                    searchResult.map((p, i) => {
                      return (
                        <tr>
                          <td>
                            <Link
                              to={{
                                pathname: "/patient/" + p._id,
                                state: p,
                              }}
                              className={`btn ${btnColors[i % 5]} text-white`}
                            >
                              {p.patientName}
                            </Link>
                          </td>
                          <td>{p?.patientEmail}</td>
                          <td className="d-none d-md-table-cell">
                            {p?.patientAge}
                          </td>
                          <td className="d-none d-md-table-cell">
                            {p?.patientGender}
                          </td>
                          <td className="d-none d-md-table-cell">
                            {p?.patientPhone}
                          </td>
                          {/* <td>{p["depression score"]}</td>
                      <td>{p?.enthusiasm}</td>
                      <td>{p?.optimisum}</td> */}
                        </tr>
                      );
                    })
                  )
                ) : isLoading ? (
                  <tr className="text-center border-none">
                    <td colspan="5">
                      <div className="spinner-border text-primary m-5">
                        <span className="visually-hidden">Loading...</span>
                      </div>
                    </td>
                  </tr>
                ) : (
                  patients.map((p, i) => {
                    return (
                      <tr>
                        <td>
                          <Link
                            to={{
                              pathname: "/patient/" + p._id,
                              state: p,
                            }}
                            className={`btn ${btnColors[i % 5]} text-white`}
                          >
                            {p.patientName}
                          </Link>
                        </td>
                        <td>{p?.patientEmail}</td>
                        <td className="d-none d-md-table-cell">
                          {p?.patientAge}
                        </td>
                        <td className="d-none d-md-table-cell">
                          {p?.patientGender}
                        </td>
                        <td className="d-none d-md-table-cell">
                          {p?.patientPhone}
                        </td>
                        {/* <td>{p["depression score"]}</td>
                      <td>{p?.enthusiasm}</td>
                      <td>{p?.optimisum}</td> */}
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </Base>
  );
};

export default UserDashboard;
