from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import random
import os  
from models import init_db
from stt import speech_to_text
from nlu import parse
from tts import text_to_speech
from bank_api import get_balance, transfer, get_transactions

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "secret123"
jwt = JWTManager(app)

OTP_STORE = {}

UPLOAD_FOLDER = r"E:\voice-banking-assistant\uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/send-otp", methods=["POST"])
def send_otp():
    phone = request.json["phone"]
    otp = str(random.randint(100000, 999999))
    OTP_STORE[phone] = otp
    print("MOCK OTP →", otp)
    return {"msg": "OTP sent"}

@app.route("/verify", methods=["POST"])
def verify():
    phone = request.json["phone"]
    otp = request.json["otp"]
    if OTP_STORE.get(phone) == otp:
        token = create_access_token(identity=phone)
        return {"token": token}
    return {"error": "Invalid OTP"}, 400

@app.route("/stt", methods=["POST"])
def stt():
    audio = request.files["audio"]
    path = "audio.wav"
    audio.save(path)
    text = speech_to_text(path)
    return {"text": text}

@app.route("/nlu", methods=["POST"])
def nlu():
    text = request.json["text"]
    return parse(text)

@app.route("/action", methods=["POST"])
@jwt_required()
def action():
    data = request.json
    intent = data["intent"]

    if intent == "check_balance":
        bal = get_balance("ACCT1001")
        return {"result": f"Your balance is {bal}"}

    if intent == "transfer":
        ok, msg = transfer("ACCT1001", data["account"], data["amount"])
        return {"result": msg}

    if intent == "transactions":
        tx = get_transactions("ACCT1001")
        return {"result": tx}

    return {"error": "Unknown intent"}

@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()  # Safely get JSON
    if not data or "text" not in data:
        return {"error": "No text provided"}, 400  # Return 400 if missing

    text = data["text"]
    path = text_to_speech(text)
    return send_file(path, mimetype="audio/mpeg")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
