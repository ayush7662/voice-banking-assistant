import { useState } from "react";
import axios from "axios";
import toast from "react-hot-toast";

export default function Login({ setToken }) {
  const [phone, setPhone] = useState("");
  const [otp, setOtp] = useState("");
  const [sent, setSent] = useState(false);

  const sendOTP = async () => {
    try {
      await axios.post("http://127.0.0.1:5000/send-otp", { phone });
      toast.success("OTP sent (check backend console)");
      setSent(true);
    } catch (e) {
      toast.error("Failed to send OTP");
    }
  };

  const verifyOTP = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/verify", {
        phone,
        otp,
      });
      setToken(res.data.token);
      toast.success("Login successful!");
    } catch (e) {
      toast.error("Invalid OTP");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Login</h2>

      <input
        placeholder="Phone Number"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />
      <button onClick={sendOTP}>Send OTP</button>

      {sent && (
        <>
          <input
            placeholder="Enter OTP"
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
          />
          <button onClick={verifyOTP}>Verify</button>
        </>
      )}
    </div>
  );
}
