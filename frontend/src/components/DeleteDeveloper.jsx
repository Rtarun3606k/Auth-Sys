import React from "react";

function DeleteDeveloper() {
  const handleDelete = () => {
    fetch("/dev/deleteDev", {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((response) => response.json())
      .then((data) => alert(data.msg))
      .catch((error) => console.error("Error deleting developer:", error));
  };

  return (
    <div>
      <h2>Delete Developer</h2>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
}

export default DeleteDeveloper;
