import speech_recognition as sr
import pyttsx3
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError:
        speak("Could not request results from speech recognition service.")
        return ""

def run_voice_assistant():
    speak("Hello! How can I help you today?")
    
    while True:
        query = listen()
        
        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
            
        elif 'hello' in query:
            speak("Hello there! Ready to write some code?")
            
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day.")
            break

if __name__ == "__main__":
    run_voice_assistant()