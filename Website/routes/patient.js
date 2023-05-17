const express = require("express");
const {createPatient, getAllPatients } = require("../controllers/patient");
const router = express.Router();

// router.get("/patients", getAllPatients);
router.post("/patients/create", createPatient);
router.get("/patients", getAllPatients);


module.exports = router
