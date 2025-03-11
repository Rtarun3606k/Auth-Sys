import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Layout from "./Pages/Dev/auth/Layout";
import Login from "./Pages/Dev/auth/Login";
import Register from "./Pages/Dev/auth/Register";

function AppRouter() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/dev" element={<Layout />}>
            <Route path="login" element={<Login />} />
            <Route path="register" element={<Register />} />
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default AppRouter;
