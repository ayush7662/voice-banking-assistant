# Voice Banking Assistant

A Python-based voice banking assistant that allows users to interact with a mock bank using voice commands. Features include checking account balance, transferring money, viewing recent transactions, and text-to-speech responses.


GitHub Repository: https://github.com/ayush7662/voice-banking-assistant
Demo Video: https://drive.google.com/file/d/1njbgmFS3OaYuBAKFWw5UwESyPp1A7E7N/view?usp=sharing


---

## Features

- **OTP Authentication**: Mock OTP verification for user login.
- **Speech-to-Text (STT)**: Convert your voice commands into text using OpenAI's Whisper model.
- **Natural Language Understanding (NLU)**: Recognizes intents such as checking balance, transferring money, and viewing transactions.
- **Banking API**: Handles account data, balances, transfers, and transaction history using SQLite.
- **Text-to-Speech (TTS)**: Converts responses to audio using gTTS.
- **Flask REST API**: Provides endpoints for OTP, STT, NLU, actions, and TTS.

---

## Project Structure

voice-banking-assistant/
│
├── backend/
│ ├── app.py # Flask app
│ ├── models.py # Database models and initialization
│ ├── bank_api.py # Banking functions (balance, transfer, transactions)
│ ├── nlu.py # Natural language understanding
│ ├── stt.py # Speech-to-text using Whisper
│ ├── tts.py # Text-to-speech using gTTS
│ └── venv/ # Python virtual environment
│
├── uploads/ # Directory to store uploaded audio
└── README.md


---

## Requirements

- Python 3.10+
- Flask
- Flask-CORS
- Flask-JWT-Extended
- SQLAlchemy
- gTTS
- OpenAI Whisper
- ffmpeg (must be installed and added to PATH)

Install Python dependencies:

```bash
pip install -r requirements.txt


Make sure ffmpeg is installed and available in your system PATH:

ffmpeg -version

Setup

Clone the repository:

git clone https://github.com/ayush7662/voice-banking-assistant.git
cd voice-banking-assistant/backend


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate       



Install dependencies:

pip install -r requirements.txt


Initialize the database:

python
>>> from models import init_db
>>> init_db()
>>> exit()

Running the App

Start the Flask server:

python app.py


Default URL: http://127.0.0.1:5000

API Endpoints
Endpoint	Method	Description
/send-otp	POST	Send mock OTP for authentication
/verify	POST	Verify OTP and receive JWT token
/stt	POST	Upload audio and convert speech to text
/nlu	POST	Parse text to extract intent
/action	POST	Perform banking action based on intent
/tts	POST	Convert text response to speech
Example Voice Commands

Check Balance: “Check my balance”, “What is my account balance?”

Transfer Money: “Transfer 500 to account 2001”, “Pay 300 to acct 2002”

View Transactions: “Show my recent transactions”, “Transaction history”

Note: Currently the assistant only returns balance, transactions, or handles transfers. Asking for the account number is not supported for security.

License

This project is for educational purposes.


---

I can also create a **`requirements.txt`** for your project so users can install all dependencies easily.  

Do you want me to do that next?
