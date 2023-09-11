import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Home.css";
import { API_URL } from "../constants.js";


const Auth = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmitUser = async (username, password) => {
    const payload = { username, password };

    const res = await fetch(`${API_URL}/v1/auth/`, {
      method: "POST",
      cache: "no-cache",
      body: JSON.stringify(payload),
    });

    const body = await res.json();

    if (res.status == 200 || res.status == 201) {
      navigate("/home", {
        state: {
          token: body.token,
          user: body.user,
        },
      });
    } else {
      alert(body || "An Error Occured, Refer To The Console");
    }
  };

  return (
    <div className="authpage">
      <div className="auth-welcome-text">
        <h2>Sign Up or Sign In here...</h2>
      </div>

      <div className="auth-form">
        <form>
          <input
            placeholder="username"
            onChange={(e) => {
              setUsername(e.target.value);
            }}
            value={username}
            required
          />
          <input
            placeholder="password"
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            value={password}
            required
          />
          <button
            onClick={() => {
              handleSubmitUser(username, password);
            }}
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default Auth;
