import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer and microphone
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Please speak now...")
        # Adjust for ambient noise and record audio from the microphone
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use Google's speech recognition to convert audio to text
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.RequestError:
        # API was unreachable or unresponsive
        print("API unavailable")
    except sr.UnknownValueError:
        # Speech was unintelligible
        print("Could not understand audio")

if __name__ == "__main__":
    recognize_speech()
