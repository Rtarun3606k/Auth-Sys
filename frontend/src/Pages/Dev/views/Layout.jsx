import React from "react";
import Navbar from "../../../components/Navbar";
import Footer from "../../../components/Footer";
import { Outlet } from "react-router-dom";

const Layout_user = () => {
  const tabs = [
    {
      name: "Home",
      link: "/dev/home",
    },
    {
      name: "Profile",
      link: "/dev/profile",
    },
  ];

  return (
    <div>
      <Navbar title="DEV CONSOLE" tabs={tabs} />
      <Outlet />
      <Footer />
    </div>
  );
};

export default Layout_user;
