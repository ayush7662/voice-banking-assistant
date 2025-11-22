import whisper
import os

# Load Whisper model once
model = whisper.load_model("tiny")

def speech_to_text(filepath):
    # Ensure file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Audio file not found: {filepath}")

    # Transcribe audio
    result = model.transcribe(filepath)
    text = result.get("text", "")
    print(f"Transcribed text: {text}")
    return text
