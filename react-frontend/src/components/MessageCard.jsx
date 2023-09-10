import React from "react";

const MessageCard = ({ message }) => {
  return (
    <div className="message">
      <div className="message-body">{message.content}</div>

      <div className="message-footer">
        <div>Sent at {message.created_at}</div>
        <div>Sent by {message.sender.username}</div>
      </div>
    </div>
  );
};

export default MessageCard;
