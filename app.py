import streamlit as st
import google.generativeai as genai
from texttospeech import text_to_speech
from speech import convert_speech_to_text

# Set up the model
genai.configure(api_key="AIzaSyBCP77DFnVbDamah6d39NDpU7jPnu8UfGE")  # Replace with your actual API key

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

system_instruction = "You are an Interviewer. Your task is to train software engineers by asking them questions regarding interview by providing feedbacks for their answers and suggesting better answers. Also rate the overall interview out of 10 comparing it to an ideal interview. Only give the feedback when the user says 'Thank you, I am done for today's interview.' Don't put any special characters while giving feedback and suggestion."

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

# Function to start the interview
def start_interview():
    st.write("Welcome to the Mock Interview App!")
    st.write("Click the button below to start recording your interview:")
    if st.button("Start Recording"):
        interview()

# Function to conduct the interview
def interview():
    st.write("Interview Started...")
    st.write("Speak into your microphone and answer the questions.")
    st.write("When you're done, click the 'Stop Recording' button or say 'Thank you, I am done for today's interview.'")
    history = []  # To store conversation history
    while True:
        user_input = convert_speech_to_text()
        if user_input.lower() == "exit":
            break
        # Add user input to conversation history
        history.append({
            "role": "user",
            "parts": [user_input]
        })

        # Start chat with updated history
        convo = model.start_chat(history=history)

        # Get model response
        model_response = convo.send_message(content=user_input)  # Pass user input as content

        # Add model response to conversation history
        history.append({
            "role": "model",
            "parts": [model_response.text]
        })

        # Display user's speech input and model's response
        st.write("You:", user_input)
        st.write("Model:", model_response.text)
        text_to_speech(model_response.text)

# Main function
def main():
    start_interview()

if __name__ == "__main__":
    main()
