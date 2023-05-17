import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./pages/Home/Home";
import Signup from "./pages/Signup/Signup";
import Login from "./pages/Login/Login";
import PageNotFound from "./pages/PageNotFound/PageNotFound";
import UserDashboard from "./pages/UserDashboard/UserDashboard";
import PrivateRoute from "./helper/auth/PrivateRoutes";
import CreateQuiz from "./pages/CreateQuiz/CreateQuiz";
import { QuizProvider } from "./context/QuizContext";
import PatientDetails from "./pages/PatientDetails/PatientDetails";

function App() {
  return (
    <QuizProvider>
      <Router>
        <Switch>
          <PrivateRoute exact path="/" component={UserDashboard} />
          <Route exact path="/signup" component={Signup} />
          <Route exact path="/login" component={Login} />
          {/* <Route exact path="/user/dashboard" component={UserDashboard}/> */}
          <PrivateRoute
            exact
            path="/user/dashboard"
            component={UserDashboard}
          />
          <PrivateRoute exact path="/user/quiz/create" component={CreateQuiz} />
          <Route exact path="/patient/:id" component={PatientDetails}/>
          <Route path="*" component={PageNotFound} />
        </Switch>
      </Router>
    </QuizProvider>
  );
}

export default App;
