import { Link } from "react-router-dom";
import React from "react";

const Navbar = () => {
  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex-shrink-0 flex items-center">
              <img
                src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/logo1680774054150-removebg-jwbKzbl8AZvbRzKSZeBpJVvHROdhCA.png"
                alt="PES University Logo"
                className="h-8 w-auto"
              />
              <span className="ml-3 text-[#2e3a6a] font-semibold text-lg">
                Student Portal
              </span>
            </Link>
            <div className="ml-6">
              <Link
                to="/dev/home"
                className="text-[#2e3a6a] hover:text-blue-800 px-3 py-2 rounded-md text-sm font-medium"
              >
                Home
              </Link>
            </div>
          </div>
          <div className="flex items-center">
            <Link
              to="/dev/login"
              className="text-[#2e3a6a] hover:text-blue-800 px-3 py-2 rounded-md text-sm font-medium"
            >
              Login
            </Link>
            <Link
              to="/dev/register"
              className="text-[#2e3a6a] hover:text-blue-800 px-3 py-2 rounded-md text-sm font-medium"
            >
              Register
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
