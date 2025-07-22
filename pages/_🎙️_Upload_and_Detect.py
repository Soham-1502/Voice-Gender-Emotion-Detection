

import streamlit as st
import os
import sys
import tempfile

# ✅ Add root folder to path so backend/ works
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# ✅ Import from utils (ensure utils.py is in root folder)
from utils import local_css
local_css("assets/style.css")

# ✅ Import your model function (AFTER fixing path)
from backend.model.audio_model import predict_audio

# ✅ Streamlit UI code starts here
st.set_page_config(page_title="🎙️ Voice Emotion & Gender Detection")

st.title("🎤 Upload Voice and Detect Emotion & Gender")
st.markdown("Upload a `.wav` audio file to detect the speaker's **gender** and **emotion** using machine learning.")

uploaded_file = st.file_uploader("🎧 Upload your voice (.wav only)", type=["wav"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.audio(uploaded_file, format="audio/wav")

    with st.spinner("🧠 Analyzing voice..."):
        gender, emotion = predict_audio(tmp_path)

    if gender == "Error":
        st.error(f"Prediction Failed: {emotion}")
    else:
        st.success(f"🧍‍♂️ **Gender**: `{gender}`")
        st.success(f"🎭 **Emotion**: `{emotion}`")

