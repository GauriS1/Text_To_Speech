import os
import pyttsx3
from gtts import gTTS
from playsound import playsound

def speak_text(text):
    if not text.strip():
        print("⚠️ Please enter non-empty text.")
        return

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(current_dir, "tts_text.mp3")

    try:
        tts = gTTS(text)
        tts.save(save_path)
        print(f"✅ Saved and playing: {save_path}")
        playsound(save_path)
    except Exception as e:
        print(f"❌ gTTS failed: {e}")
        print("▶ Falling back to pyttsx3 (WAV - Offline)...")
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e2:
            print(f"❌ pyttsx3 also failed: {e2}")

# Run
if __name__ == "__main__":
    try:
        user_input = input("Enter the text you want to convert to speech:\n")
        speak_text(user_input)
    except KeyboardInterrupt:
        print("\n⛔ Operation cancelled by user.")
