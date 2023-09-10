import React from "react";
import "../styles/UserCard.css";
import { useNavigate } from "react-router-dom";
import avatar from "../assets/avatar.jpg";

const UserCard = ({ user, token }) => {
  const navigate = useNavigate();

  const handleSubmit = async () => {
    const payload = { "requested-user-id": user.id };

    const res = await fetch("http://localhost:8000/v1/chatspace/", {
      method: "POST",
      cache: "no-cache",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    });

    const body = await res.json();

    if (res.status == 200 || res.status == 201) {
      navigate("/chat", {
        state: {
          chat_space_id: body["chat-space-id"],
          receiver_id: user.id,
          token: token,
        },
      });
    } else {
      alert(body || "An Error Occured, Refer To The Console");
    }
  };

  return (
    <div className="user">
      <div>
        <img src={avatar} />
      </div>

      <div className="bottom-section">
        <div className="user-username">
          <div>{user.username}</div>
        </div>
      </div>

      <div className="chat-button">
        <button type="submit" onClick={handleSubmit}>
          Chat
        </button>
      </div>
    </div>
  );
};

export default UserCard;
