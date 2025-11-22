import { useState } from "react";
import axios from "axios";
import { recordAudio } from "./Recorder";
import toast from "react-hot-toast";

export default function VoiceAssistant({ token }) {
  const [response, setResponse] = useState("");

  const startRecording = async () => {
    const recorder = await recordAudio();
    toast.success("Recording... speak now");

    setTimeout(async () => {
      const audioBlob = await recorder.stop();
      toast.success("Recording stopped");

      const formData = new FormData();
      formData.append("audio", audioBlob, "voice.wav");

      // Step 1: STT
      const sttRes = await axios.post(
        "http://127.0.0.1:5000/stt",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      const text = sttRes.data.text;
      console.log("STT:", text);

      // Step 2: NLU
      const nluRes = await axios.post("http://127.0.0.1:5000/nlu", {
        text,
      });
      console.log("NLU:", nluRes.data);

      // Step 3: Backend action
      const actionRes = await axios.post(
        "http://127.0.0.1:5000/action",
        nluRes.data,
        { headers: { Authorization: `Bearer ${token}` } }
      );

      const finalText = actionRes.data.result;
      setResponse(finalText);

      // Step 4: TTS audio
      const tts = await axios.post(
        "http://127.0.0.1:5000/tts",
        { text: finalText },
        { responseType: "blob" }
      );

      const audioURL = window.URL.createObjectURL(tts.data);
      const audio = new Audio(audioURL);
      audio.play();
    }, 3000);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Voice Banking Assistant</h2>

      <button onClick={startRecording}>🎤 Start Voice Command</button>

      <h3>Response:</h3>
      <p>{response}</p>
    </div>
  );
}
