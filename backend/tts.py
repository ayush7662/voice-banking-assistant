from gtts import gTTS
import tempfile

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    fname = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
    tts.save(fname)
    return fname
