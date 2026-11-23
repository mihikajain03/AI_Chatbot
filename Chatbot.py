import os
import re
import sys
import datetime

import cohere
import pyttsx3
import speech_recognition as sr
import pyaudio  # noqa: F401  (required by speech_recognition's Microphone backend)
import wikipedia
import webbrowser

# --- Config -----------------------------------------------------------------
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")
COHERE_MODEL = "command-a-03-2025"
VOICE_INDEX = 1
SPEECH_RATE = 175
EXIT_WORDS = {"stop", "quit", "exit", "goodbye", "shut down", "shutdown"}

if not COHERE_API_KEY:
    sys.exit(
        "COHERE_API_KEY is not set. Set it first, e.g.\n"
        '  PowerShell:  $env:COHERE_API_KEY = "your-key"\n'
        '  bash:        export COHERE_API_KEY="your-key"'
    )

co = cohere.Client(api_key=COHERE_API_KEY)

# --- Text to speech -------------------------------------------------------------
# Initialize the engine once; re-initializing on every call is slow.
_engine = pyttsx3.init("sapi5")
_voices = _engine.getProperty("voices")
if _voices:
    _engine.setProperty("voice", _voices[min(VOICE_INDEX, len(_voices) - 1)].id)
_engine.setProperty("rate", SPEECH_RATE)


def speak(audio):
    if not audio:
        return
    _engine.say(audio)
    _engine.runAndWait()


# --- Speech recognition -------------------------------------------------------
_recognizer = sr.Recognizer()
_recognizer.pause_threshold = 2


def takeCommand():
    with sr.Microphone() as source:
        _recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = _recognizer.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            return "none"

    try:
        print("Recognizing...")
        query = _recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please..!")
        return "none"
    return query.lower()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning! I am Tira Ma'am. Ready to assist you!")
    elif hour < 18:
        speak("Good Afternoon! I am Tira Ma'am. Ready to assist you!")
    else:
        speak("Good Evening! I am Tira Ma'am. Ready to assist you!")


# --- Cohere ----------------------------------------------------------------
_SENTENCE_END = re.compile(r"(.+?[.!?])(\s+|$)", re.DOTALL)


def ask_cohere(query):
    """Stream the answer, speaking each sentence as soon as it is complete."""
    buffer = ""
    full = []
    try:
        for event in co.chat_stream(
            model=COHERE_MODEL,
            message=f"Give a short one-two line answer to: {query}",
            temperature=0.6,
        ):
            if event.event_type != "text-generation":
                continue
            chunk = event.text
            print(chunk, end="", flush=True)
            full.append(chunk)
            buffer += chunk
            while True:
                match = _SENTENCE_END.match(buffer)
                if not match:
                    break
                speak(match.group(1).strip())
                buffer = buffer[match.end():]
        print()
        if buffer.strip():
            speak(buffer.strip())
        return "".join(full).strip()
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I couldn't get an answer right now")
        return ""


def main():
    wishMe()
    while True:
        query = takeCommand()

        if query == "none":
            continue

        if any(word in query for word in EXIT_WORDS):
            speak("Goodbye!")
            break

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(topic, sentences=1)
            except wikipedia.DisambiguationError as e:
                results = f"That could mean several things, such as {e.options[0]}."
            except wikipedia.PageError:
                results = "I couldn't find a Wikipedia page for that."
            except Exception:
                results = "Sorry, the Wikipedia lookup failed."
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        else:
            ask_cohere(query)


if __name__ == "__main__":
    main()
