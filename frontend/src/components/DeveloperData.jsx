import React, { useState, useEffect } from "react";

function DeveloperData() {
  const [devData, setDevData] = useState(null);

  useEffect(() => {
    fetch("/dev/getDev", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => setDevData(data.DevData))
      .catch((error) => console.error("Error fetching developer data:", error));
  }, []);

  if (!devData) return <div>Loading...</div>;

  return (
    <div>
      <h2>Developer Data</h2>
      <pre>{JSON.stringify(devData, null, 2)}</pre>
    </div>
  );
}

export default DeveloperData;
