"""
Text to Speech Tutorial - Ready to Run
Make sure to install required libraries before running:
    pip install pyttsx3 gTTS playsound==1.2.2
"""
''''
# ==========================================
# METHOD 1: Offline TTS using 'pyttsx3'
# ==========================================
import pyttsx3

def test_offline_tts():
    # Initialize the engine
    engine = pyttsx3.init()
    
    # 1. Basic Playback
    print("Playing offline voice...")
    engine.say("Hello! This is the offline pyttsx3 voice engine.")
    engine.runAndWait()
    
    # 2. Customizing Speed and Voice
    engine.setProperty('rate', 150) # Slow down speed (default is ~200)
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id) # Switch to female voice if available
        
    # 3. Recording/Saving directly to an MP3 file
    print("Recording offline voice to 'offline_output.mp3'...")
    engine.save_to_file("This audio message was recorded offline.", "offline_output.mp3")
    engine.runAndWait()


# ==========================================
# METHOD 2: Online TTS using Google Cloud ('gTTS')
# ==========================================
# Note: Requires an internet connection
from gtts import gTTS
from playsound import playsound
import os

def test_online_tts():
    text_data = "Hello! This is a natural-sounding recording from Google."
    
    # 1. Create and Save the recording
    print("Downloading and recording online voice to 'google_output.mp3'...")
    tts = gTTS(text=text_data, lang='en')
    tts.save("google_output.mp3")
    
    # 2. Play the recording back immediately
    print("Playing online voice playback...")
    playsound("google_output.mp3")

'''''''''
# ==========================================
# METHOD 3: OS Native Shortcuts (No installations)
# ==========================================
def test_native_tts():
    import sys
    import os
    print("Playing native OS voice shortcut...")
    
    if sys.platform == "darwin": # macOS
        os.system("say 'Hello from your Mac terminal'")
    elif sys.platform.startswith("linux"): # Linux
        os.system("spd-say 'Hello from your Linux terminal'")
    else:
        print("Native command line shortcut not supported on Windows without third-party tools.")

'''''
# ==========================================
# EXECUTION BLOCK
# Uncomment the function you want to compile and run:
# ==========================================
if __name__ == "__main__":
    test_offline_tts()
    # test_online_tts()
    # test_native_tts()
'''