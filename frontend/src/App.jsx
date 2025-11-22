import { useState } from "react";
import Login from "./components/Login";
import VoiceAssistant from "./components/VoiceAssistant";
import { Toaster } from "react-hot-toast";

export default function App() {
  const [token, setToken] = useState(null);

  return (
    <div>
      <Toaster />
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <VoiceAssistant token={token} />
      )}
    </div>
  );
}
