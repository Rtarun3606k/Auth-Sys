import React, { useState } from "react";

function CreateApp() {
  const [appData, setAppData] = useState({});

  const handleChange = (e) => {
    setAppData({ ...appData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/dev/createApp", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
      body: JSON.stringify({ appData }),
    })
      .then((response) => response.json())
      .then((data) => alert(data.msg))
      .catch((error) => console.error("Error creating app:", error));
  };

  return (
    <div>
      <h2>Create App</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="appname"
          placeholder="App Name"
          onChange={handleChange}
        />
        <input
          type="text"
          name="redirectionURL"
          placeholder="Redirection URL"
          onChange={handleChange}
        />
        <input
          type="text"
          name="errorURL"
          placeholder="Error URL"
          onChange={handleChange}
        />
        <input
          type="text"
          name="cookiesName"
          placeholder="Cookies Name"
          onChange={handleChange}
        />
        <button type="submit">Create</button>
      </form>
    </div>
  );
}

export default CreateApp;
