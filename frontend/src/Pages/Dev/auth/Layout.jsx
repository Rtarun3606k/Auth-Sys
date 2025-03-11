import React from "react";
import { Outlet } from "react-router-dom";
import Navbar from "../../../components/Navbar";
import Footer from "../../../components/Footer";

function Layout() {
  return (
    <div>
      <Navbar title="DEV CONSOLE" />
      <Outlet />
      <Footer />
    </div>
  );
}

export default Layout;
