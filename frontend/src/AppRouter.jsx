import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Layout from "./Pages/Dev/auth/Layout";
import Login from "./Pages/Dev/auth/Login";
import Register from "./Pages/Dev/auth/Register";
import Home from "./Pages/Dev/views/Home";
import Profile from "./Pages/Dev/views/Profile";
import Layout_user from "./Pages/Dev/views/Layout";

function AppRouter() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/dev-auth" element={<Layout />}>
            <Route path="login" element={<Login />} />
            <Route path="register" element={<Register />} />
          </Route>
          <Route path="/dev" element={<Layout_user />}>
            <Route path="home" element={<Home />} />
            <Route path="profile" element={<Profile />} />
            {/* <Route path="register" element={<Register />} /> */}
          </Route>

          <Route path="*" element={<h1>Not Found</h1>} />
        </Routes>
      </Router>
    </div>
  );
}

export default AppRouter;
