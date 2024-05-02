import pyttsx3 as pt

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pt.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)