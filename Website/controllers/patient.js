const Patient = require("../models/patient");

// exports.getAllPatients =async (req, res) => {
//     connect()
//       .then(async () => {
//         const db = client.db("depression");
//         const patients = await db.collection("patient").find({});
//         return patients
//       })
//       .catch((err) => console.log(err));
//   };

exports.getAllPatients = (req,res)=>{
    console.log("ENTERED in GETALLPATIENTS")
    Patient.find().exec((err, patients) => {
        if (err) {
          return res.status(400).json({
            error: "NO patients found",
          });
        }
        res.json(patients);
      });
}

exports.createPatient = (req, res) => {
  console.log("HOGAYA");
  const patient = new Patient(req.body);
  patient.save((err, patient) => {
    console.log("INSIDE SAVE");
    if (err) {
      console.log(err);
      return res.status(400).json({
        error: "Failed to save in your DB",
      });
    }
    res.json(patient);
  });
};
