const express = require('express');
const app = express();
const cors = require("cors");
const path = require('path');
const mongoose = require("mongoose");
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

require('dotenv').config();

app.use(express.json({ limit: "200mb", extended: true }));
app.use(
  express.urlencoded({ limit: "200mb", extended: true, parameterLimit: 50000 })
);

app.use(cors());
app.use(bodyParser.json());
app.use(cookieParser());
app.use(express.json());

// Routes
const authRoutes = require("./routes/auth");
const userRoutes = require("./routes/user");
const categoryRoutes = require("./routes/category");
const quizRoutes = require("./routes/quiz");
const attemptRoutes = require("./routes/attempt");
const patientRoutes = require("./routes/patient");

app.use('/api', authRoutes)
app.use('/api', userRoutes)
app.use('/api', categoryRoutes)
app.use('/api', quizRoutes)
app.use('/api', attemptRoutes)
app.use('/api', patientRoutes)


//DB Connection
    mongoose.connect(process.env.DATABASE, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex: true
}).then(() => {
    console.log("DB CONNECTED");
});

// var MongoClient = require('mongodb').MongoClient;
// // var url = process.env.DATABASE;

// MongoClient.connect(process.env.DATABASE, function(err, db) {
//   if (err) throw err;
//   var dbo = db.db("depression");
//   dbo.collection("patient").findOne({}, function(err, result) {
//     if (err) throw err;
//     console.log(result + "2");
//     db.close();
//   });
// }).then(() => console.log("DB CONNECTED 2.0")).catch(err => console.log(err));

// const { MongoClient } = require('mongodb');
// // or as an es module:
// // import { MongoClient } from 'mongodb'

// // Connection URL
// const url = process.env.DATABASE;
// const client = new MongoClient("mongodb+srv://abkoder:%40AR.yusufi321db@quizzy.elc67.mongodb.net/quizzy?retryWrites=true&w=majority",  { useNewUrlParser: true, useUnifiedTopology: true });

// // Database Name
// const dbName = 'depression';

// async function main() {
//   // Use connect method to connect to the server
//   await client.connect();
//   console.log('Connected successfully to server');
//   const db = client.db(dbName);
//   const collection = db.collection('patient');

//   // the following code examples can be pasted here...

//   return 'done.';
// }

// main()
//   .then(console.log)
//   .catch(console.error)
//   .finally(() => client.close());

app.use(express.static(path.join(__dirname, "client/build")));

app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "client/build", "index.html"));
});

const PORT = process.env.PORT || 5000

app.listen(PORT, () => {
    console.log(`Server is Running at Port ${PORT}`);
})