import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import UserCard from "../components/UserCard";
import { API_URL } from "../constants.js";

import "../styles/Home.css";


const UserHome = () => {
  const [allUsers, setAllUsers] = useState([]);
  const location = useLocation();
  const userdata = location.state || {};

  const fetchUsers = async () => {
    const res = await fetch(`${API_URL}/v1/all-users/`, {
      method: "GET",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${userdata.token}`,
      },
    });
    const data = await res.json();
    setAllUsers(data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className="homepage">
      <div className="welcome-user-text">Welcome {userdata.user.username}</div>

      <div className="all-users-header">
        <h2>All registered users * Excluding you</h2>
      </div>

      {allUsers?.length > 0 ? (
        <div className="users-container">
          {allUsers.map((user) => (
            <UserCard user={user} token={userdata.token} />
          ))}
        </div>
      ) : (
        <div className="no-users">
          <h3>loading users...</h3>
        </div>
      )}
    </div>
  );
};

export default UserHome;
