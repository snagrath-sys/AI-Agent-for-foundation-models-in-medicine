import streamlit as st
from PIL import Image
import base64
import os

def setup_page():
    """Configure the Streamlit page settings"""
    st.set_page_config(
        page_title="smolAgent — Clinical AI Assistant",
        page_icon=":nerd_face:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
        <style>
        .main {
            padding: 0;
            font-family: 'Inter', sans-serif;
        }
        .stApp {
            position: relative;
            min-height: 100vh;
        }
        .stApp::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: linear-gradient(rgba(0, 32, 128, 0.3), rgba(0, 16, 64, 0.6));
            z-index: 1;
        }
        .stApp::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.7;
            z-index: 0;
        }
        .block-container {
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            max-width: 1000px;
            position: relative;
            z-index: 2;
            margin: 2rem auto;
        }
        .stTitle {
            text-align: center;
            color: white;
            font-weight: 600;
            margin-bottom: 2rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .description {
            text-align: center;
            padding: 1rem;
            margin-bottom: 2rem;
            color: rgba(255, 255, 255, 0.9);
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        /* Chat container styling */
        .stChatMessage {
            padding: 1rem 0;
        }
        .stChatMessage div {
            padding: 0.5rem 1rem;
            border-radius: 15px;
            max-width: 80%;
            line-height: 1.4;
        }
        /* User message styling */
        .stChatMessage[data-testid="user-message"] div {
            background-color: rgba(255, 255, 255, 0.9);
            margin-right: auto;
            border-bottom-left-radius: 5px;
            backdrop-filter: blur(10px);
        }
        /* Assistant message styling */
        .stChatMessage[data-testid="assistant-message"] div {
            background-color: rgba(232, 242, 255, 0.9);
            margin-left: auto;
            border-bottom-right-radius: 5px;
            color: #1e3a8a;
            backdrop-filter: blur(10px);
        }
        /* Input box styling */
        .stTextInput input {
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 0.75rem 1rem;
            font-size: 0.95rem;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            backdrop-filter: blur(10px);
        }
        .stTextInput input:focus {
            border-color: rgba(255, 255, 255, 0.5);
            box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
        }
        .stTextInput input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Set background image
    background_image = _get_base64_encoded_image("static/app_background.jpg")
    st.markdown(
        f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{background_image}");
            background-size: cover;
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

def _get_base64_encoded_image(image_path):
    """Get base64 encoded image"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_header():
    """Display the app title and description"""
    st.title("smolAgent — Clinical AI Assistant")
    st.markdown(
        '<p class="description">Ask diagnostic questions or upload patient data '
        '(This is a demo app, do not upload real patient data)</p>', 
        unsafe_allow_html=True
    )

def init_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_history():
    """Display the chat history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_user_input():
    """Get user input from chat interface"""
    return st.chat_input("Ask a question about patient diagnosis...")

def display_user_message(message):
    """Display user message in chat"""
    with st.chat_message("user"):
        st.markdown(message)

def display_assistant_response(response):
    """Display assistant response in chat"""
    with st.chat_message("assistant"):
        st.markdown(response)

def update_chat_history(role, content):
    """Update the chat history with new messages"""
    st.session_state.messages.append({"role": role, "content": content})
