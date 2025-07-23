import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config (must be the first Streamlit command)
st.set_page_config(page_title="Voice AI", page_icon="🎧", layout="centered")

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
st.title("🎧 Voice Emotion & Gender Detector")

if lottie_ai:
    st_lottie(lottie_ai, height=300, key="ai_lottie")  # Balanced with image

# App Description
st.markdown("""
Welcome to your **AI-powered voice analysis platform**!  
Upload `.wav` audio files to detect the **emotion** and **gender** of the speaker using advanced machine learning models.

---

🎙️ **Navigate to the sidebar** to start analyzing your audio.

💡 **Features**:
- Upload your voice in `.wav` format
- Real-time predictions with SVM and CNN models
- Explore how AI understands emotions and gender
""")

# Cache External Image (Neon Microphone with Sound Waves)
@st.cache_data
def get_image_url():
    return "https://img.freepik.com/free-vector/microphone-with-sound-wave_23-2148494967.jpg"  # Neon microphone icon

st.markdown("### 👋 Get Started")
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px;">
        <a href="/Upload_and_Detect" target="_self">
            <button style="
                background-color: #6c5ce7;
                color: white;
                padding: 12px 28px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                font-weight: 600;
                cursor: pointer;
                transition: background 0.3s ease;
            ">
                🎙️ Get Started
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)