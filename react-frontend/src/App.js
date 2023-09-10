import { BrowserRouter, Route, Routes } from "react-router-dom";

import "./styles/Global.css";
import NavBar from "./components/Navbar";
import Auth from "./pages/UserAuth";
import UserHome from "./pages/HomePage";
import ChatPage from "./pages/ChatPage";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <>
                <NavBar /> <Auth />
              </>
            }
          />
          <Route
            path="/home"
            element={
              <>
                <NavBar /> <UserHome />
              </>
            }
          />
          <Route
            path="/chat"
            element={
              <>
                <NavBar /> <ChatPage />
              </>
            }
          />
        </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
