import React, { useState, useEffect } from "react";

function AllDevelopers() {
  const [devsData, setDevsData] = useState([]);

  useEffect(() => {
    fetch("/dev/getAllDevs", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    })
      .then((response) => response.json())
      .then((data) => setDevsData(data.DevsData))
      .catch((error) =>
        console.error("Error fetching developers data:", error)
      );
  }, []);

  if (devsData.length === 0) return <div>No developers found</div>;

  return (
    <div>
      <h2>All Developers</h2>
      <ul>
        {devsData.map((dev) => (
          <li key={dev._id}>{dev.email}</li>
        ))}
      </ul>
    </div>
  );
}

export default AllDevelopers;
