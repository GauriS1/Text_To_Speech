import os
import time
import pyttsx3
from gtts import gTTS
from playsound import playsound
from langdetect import detect

def split_text_with_pauses(input_text, pause_characters={'.', '!', '?', ','}, pause_duration=0.7):
    Text = []
    sentence = ""
    for char in input_text:
        sentence += char
        if char in pause_characters:
            Text.append(sentence.strip())
            sentence = ""
    if sentence.strip():
        Text.append(sentence.strip())
    return Text, pause_duration

def convert_text_to_speech(input_text):
    if not input_text.strip():
        return

    try:
        detected_language = detect(input_text)
    except:
        detected_language = 'en'

    Text, segment_pause = split_text_with_pauses(input_text)

    # Join all text segments back together with natural pause simulation (e.g., periods)
    combined_text = " ".join(Text)
    output_audio_path = os.path.join(os.getcwd(), "final_speech.mp3")

    try:
        time.sleep(0.5)  # brief pause before starting
        gTTS(combined_text, lang=detected_language).save(output_audio_path)
        time.sleep(0.2)  # ensure file is saved
        playsound(output_audio_path)

    except:
        speech_engine = pyttsx3.init()
        speech_engine.setProperty('rate', 150)
        time.sleep(0.5)
        speech_engine.say(combined_text)
        speech_engine.runAndWait()

if __name__ == "__main__":
    try:
        user_input_text = input("Enter the text to speak: ")
        convert_text_to_speech(user_input_text)
    except KeyboardInterrupt:
        print("\nCancelled by user.")
