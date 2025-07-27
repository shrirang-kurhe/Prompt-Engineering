import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your Google AI API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API key not found. Please add it to your .env file.")
else:
    genai.configure(api_key=api_key)

# Gemini model name
MODEL_NAME = "gemini-1.5-flash-latest"  # or use gemini-1.5-pro-latest

def generate_response(prompt, temperature=0.7):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title('🔮 Prompt Engineering with Google Gemini')
st.write('Enter your prompt below and see how the model responds.')

user_prompt = st.text_area('✍️ Prompt', height=200)

if st.button('Generate Response'):
    if user_prompt:
        with st.spinner('Generating response...'):
            response = generate_response(user_prompt)
            if response:
                st.subheader('🧠 Assistant Response:')
                st.write(response)
    else:
        st.warning('Please enter a prompt before generating a response.')

st.markdown("---")
st.caption("🔐 This app uses Google's Gemini API to generate responses based on your input.")
