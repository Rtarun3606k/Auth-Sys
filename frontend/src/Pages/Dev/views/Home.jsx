import React from "react";
import DeveloperData from "../../../components/DeveloperData";
import UpdateDeveloper from "../../../components/UpdateDeveloper";
import DeleteDeveloper from "../../../components/DeleteDeveloper";
import AllDevelopers from "../../../components/AllDevelopers";
import CreateApp from "../../../components/CreateApp";

function DeveloperConsole() {
  return (
    <div>
      <h1>Developer Console</h1>
      <DeveloperData />
      <UpdateDeveloper />
      <DeleteDeveloper />
      <AllDevelopers />
      <CreateApp />
    </div>
  );
}

export default DeveloperConsole;
