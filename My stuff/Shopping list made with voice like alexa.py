# Install dependencies automatically or via: python -m pip install SpeechRecognition PyAudio pyttsx3
import importlib
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def load_dependency(module_name, package_name):
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as error:
        if error.name != module_name:
            raise
        print(f"Missing dependency: {module_name}. Setting up a project-local environment...")
        try:
            environment = Path(__file__).resolve().parent / ".venv"
            environment_python = (
                environment / "Scripts" / "python.exe"
                if os.name == "nt"
                else environment / "bin" / "python"
            )
            if not environment_python.exists():
                subprocess.run(
                    [sys.executable, "-m", "venv", str(environment)],
                    check=True,
                )
            subprocess.run(
                [str(environment_python), "-m", "pip", "install", package_name],
                check=True,
            )
            result = subprocess.run([str(environment_python), __file__, *sys.argv[1:]])
            raise SystemExit(result.returncode)
        except (OSError, subprocess.CalledProcessError) as install_error:
            print(
                f"Could not install {package_name} in {environment}. Run:\n"
                f'"{environment_python}" -m pip install {package_name}'
            )
            raise SystemExit(1) from install_error


# Load dependencies
pyttsx3 = load_dependency("pyttsx3", "pyttsx3")
sr = load_dependency("speech_recognition", "SpeechRecognition")
pyaudio = load_dependency("pyaudio", "PyAudio")

# Fix for comtypes cache crash on network drives (UNC paths like \\UCASFS1\...)
try:
    import comtypes.client
except ModuleNotFoundError:
    comtypes = None
else:
    comtypes.client._dir = tempfile.gettempdir()

shopping_list = []

# Safe initialization for SAPI5
try:
    speaker = pyttsx3.init('sapi5')
except Exception:
    speaker = pyttsx3.init()

recognizer = sr.Recognizer()


def speak(message):
    print(f"Assistant: {message}")
    try:
        speaker.say(message)
        speaker.runAndWait()
    except Exception as e:
        print(f"[TTS Error]: {e}")


def listen(prompt):
    speak(prompt)
    try:
        with sr.Microphone() as microphone:
            recognizer.adjust_for_ambient_noise(microphone, duration=0.5)
            try:
                audio = recognizer.listen(microphone, timeout=6, phrase_time_limit=6)
            except sr.WaitTimeoutError:
                speak("I didn't hear anything. Please try again.")
                return ""

        try:
            recognized_text = recognizer.recognize_google(audio).lower().strip()
            print(f"You said: {recognized_text}")
            return recognized_text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Speech recognition is unavailable. Please check your internet connection.")
        return ""
    except OSError:
        print("\n[Error] No default input microphone detected or access is blocked.")
        speak("Microphone not detected. Please check your Windows sound settings.")
        return ""


def get_item_from_command(command, prefixes):
    for prefix in prefixes:
        if command.startswith(prefix):
            return command[len(prefix):].strip()
    return ""


speak("Shopping list ready. Say add, remove, show list, or exit.")
while True:
    command = listen("What would you like to do?")
    if not command:
        continue

    if command in {"exit", "quit", "stop", "goodbye"}:
        speak("Goodbye!")
        break
    elif any(word in command for word in ("show list", "view list", "read list", "what is on my list")):
        if shopping_list:
            speak("Your list contains: " + ", ".join(shopping_list))
        else:
            speak("Your shopping list is empty.")
    elif command.startswith(("add ", "add item ")) or command in {"add", "add item"}:
        item = get_item_from_command(command, ("add item ", "add "))
        if not item:
            item = listen("What item would you like to add?")
        if item:
            shopping_list.append(item)
            speak(f"{item} added to your shopping list.")
    elif command.startswith(("remove ", "delete ", "remove item ")) or command in {"remove", "delete", "remove item"}:
        item = get_item_from_command(command, ("remove item ", "remove ", "delete "))
        if not shopping_list:
            speak("Your shopping list is empty.")
        else:
            if not item:
                item = listen("Which item should I remove?")
            if item:
                try:
                    index = int(re.sub(r"\D", "", item)) - 1
                    removed = shopping_list.pop(index)
                except (ValueError, IndexError):
                    matches = [entry for entry in shopping_list if entry.lower() == item.lower()]
                    if matches:
                        removed = matches[0]
                        shopping_list.remove(removed)
                    else:
                        speak("I couldn't find that item. Say show list to hear your items.")
                        continue
                speak(f"{removed} removed from your shopping list.")
    else:
        speak("Please say add, remove, show list, or exit.")