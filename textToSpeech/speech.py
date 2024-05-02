import speech_recognition as sr
import threading

# Function to recognize speech
def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Initialize microphone
    mic = sr.Microphone()
    
    # Variable to indicate if speech recognition is stopped
    stopped = False
    
    # Function to listen for keyboard input
    def keyboard_listener():
        nonlocal stopped
        input("Press Enter to stop speech recognition...")
        stopped = True
    
    # Start keyboard listener in a separate thread
    keyboard_thread = threading.Thread(target=keyboard_listener)
    keyboard_thread.start()
    
    # Indicate microphone is on
    print("Microphone is on. Speak now...")
    
    # Record speech until stopped
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while not stopped:
            try:
                audio = recognizer.listen(source, timeout=None)
                # Indicate speech recognition in progress
                print("Recognizing speech...")
                
                # Recognize speech
                text = recognizer.recognize_google(audio)
                
                # Print recognized speech
                print("You said:", text)
                
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
    
    # Wait for the keyboard listener thread to finish
    keyboard_thread.join()

# Call the function to start speech recognition
recognize_speech()