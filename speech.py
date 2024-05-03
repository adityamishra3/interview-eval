import speech_recognition as sr

def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You (speech):", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Error: {0}".format(e))
        return ""

if __name__ == "__main__":
    converted_text = convert_speech_to_text()
    print("Converted Text:", converted_text)
