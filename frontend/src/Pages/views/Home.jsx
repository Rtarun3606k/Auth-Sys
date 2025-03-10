import { Link } from "react-router-dom";
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import React from "react";
const Home = () => {
  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <Navbar />

      <main className="flex-grow flex items-center justify-center px-4 sm:px-6 lg:px-8 py-12">
        <div className="max-w-md w-full bg-white p-8 rounded-lg shadow-md">
          <div className="flex justify-center mb-6">
            <img
              src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/logo1680774054150-removebg-jwbKzbl8AZvbRzKSZeBpJVvHROdhCA.png"
              alt="PES University Logo"
              className="h-16 w-auto"
            />
          </div>

          <h1 className="text-3xl font-bold text-center text-[#2e3a6a] mb-2">
            Welcome to PES University
          </h1>
          <h2 className="text-xl text-center text-gray-600 mb-8">
            Student Registration Portal
          </h2>

          <div className="border-t border-gray-200 my-6"></div>

          <p className="text-center text-gray-600 mb-6">
            Please register or login to access your student account.
          </p>

          <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 justify-center">
            <Link
              to="/register"
              className="bg-[#2e3a6a] text-white py-2 px-6 rounded-md font-medium hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 text-center"
            >
              Register Now
            </Link>
            <Link
              to="/login"
              className="border border-[#2e3a6a] text-[#2e3a6a] py-2 px-6 rounded-md font-medium hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 text-center"
            >
              Login
            </Link>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default Home;
