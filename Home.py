import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(page_title="Voice AI", page_icon="🎧", layout="centered")

# Inject Minimal CSS Inline
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        background-attachment: fixed;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 { color: #222831; }
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #eeeeee;
    }
    .markdown-text-container {
        font-size: 18px;
        line-height: 1.6;
    }
    /* Custom image styling */
    img {
        max-width: 100%;
        height: 300px;
        object-fit: contain;
        display: block;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# Load CSS from file
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found.")

local_css("assets/style.css")

# Cache Lottie JSON fetch
@st.cache_data
def load_lottie_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f"❌ Lottie load error: {e}")
    return None

# Load Lottie Animation
lottie_ai = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")
st.title("🎧 Welcome to Voice Emotion & Gender Detector")

if lottie_ai:
    st_lottie(lottie_ai, height=300, key="ai_lottie")

# App Description
st.markdown("""
Welcome to your AI-powered voice analysis platform!  
This site allows you to upload `.wav` audio files and detect the **emotion** and **gender** of the speaker using machine learning.

---

🎙️ Navigate to the sidebar to try it out.

💡 Features:
- Upload your voice
- Get real-time predictions
- Learn how the model works
""")

# Cache External Image
@st.cache_data
def get_image_url():
    return "https://www.shutterstock.com/shutterstock/photos/2144055901/display_1500/stock-vector-ear-hearing-sound-earphone-logo-2144055901.jpg"

st.image(get_image_url(), caption="AI Listening In...")