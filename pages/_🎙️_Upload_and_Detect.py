import streamlit as st
import soundfile as sf
from io import BytesIO
import os
import tempfile

# Import prediction function
try:
    from backend.model.predict import predict_gender_emotion
except ModuleNotFoundError:
    st.error("Error: 'predict.py' module not found. Ensure 'predict.py' is in the 'ML-project/backend/model/' directory.")
    st.stop()

# Load CSS for dark theme
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found.")

local_css("assets/style.css")

# Page content
st.title("🎙️ Voice Emotion & Gender Detection")
st.markdown("""
Upload a `.wav` file to detect the speaker's gender and emotion using pre-trained Wav2Vec2 models from Hugging Face.
""")

# File uploader
uploaded_file = st.file_uploader("Choose a .wav file", type=["wav"])

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()

    # 🎧 Show audio player
    st.markdown("#### 🔊 Uploaded Audio")
    st.audio(audio_bytes, format="audio/wav")

    # 🔘 Predict button
    if st.button("🔍 Predict"):
        try:
            # Load audio data for model
            audio_data, sample_rate = sf.read(BytesIO(audio_bytes))

            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                sf.write(temp_file.name, audio_data, sample_rate)
                temp_file_path = temp_file.name

            # Run prediction
            gender, emotion = predict_gender_emotion(temp_file_path)

            # Clean up temp file
            os.unlink(temp_file_path)

            # Show results
            st.success("Analysis complete!")
            st.markdown("### Results", unsafe_allow_html=True)
            with st.container():
                st.markdown(
                    f"""
                    <div class="results-container">
                        <div class="analysis-box">Gender : {gender}</div>
                        <div class="analysis-box">Emotion : {emotion}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
else:
    st.info("Please upload a .wav file to begin analysis.")
