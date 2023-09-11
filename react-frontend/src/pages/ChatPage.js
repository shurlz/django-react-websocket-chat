import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import "../styles/Home.css";
import MessageCard from "../components/MessageCard";
import { API_URL, WEB_SOCKET_URL } from "../constants.js";


const ChatPage = () => {
  const location = useLocation();
  const data = location.state || {};
  const [oldMessages, setOldMessages] = useState([]);

  const fetchMessages = async () => {
    const payload = { "chatspace-id": data.chat_space_id };
    const res = await fetch(`${API_URL}/v1/messages/chatspace/`, {
      method: "POST",
      cache: "no-cache",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${data.token}`,
      },
    });
    const prevMsg = await res.json();
    setOldMessages(prevMsg);
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  const ws = new WebSocket(
    `${WEB_SOCKET_URL}/ws/chat/${data.chat_space_id}/?token=${data.token}`,
  );
  ws.onopen = () => {
    // console.log("WebSocket connection established.");
  };
  ws.onmessage = (event) => {
    const messageData = JSON.parse(event.data);
    const newMessagesList = [...oldMessages, messageData.message];
    setOldMessages(newMessagesList);
  };
  ws.onclose = () => {
    console.log("WebSocket connection closed.");
  };

  const handleSubmitChat = async (event) => {
    event.preventDefault();
    const message = event.target.elements.message.value;
    const payload = { message, receiver: data.receiver_id };

    if (message.trim() !== "") {
      ws.send(JSON.stringify(payload));
    }
  };

  return (
    <div className="authpage">
      {oldMessages?.length > 0 ? (
        <div className="messages">
          {oldMessages.map((message) => (
            <MessageCard message={message} />
          ))}
        </div>
      ) : (
        <div>No mesages yet</div>
      )}

      <div className="auth-form">
        <form onSubmit={handleSubmitChat}>
          <input placeholder="enter your message" name="message" required />
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
};

export default ChatPage;
