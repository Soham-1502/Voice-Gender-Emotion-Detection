from utils import local_css
local_css("assets/style.css")

import streamlit as st

st.title("📊 Model Information")
st.markdown("""
### How It Works

- Uses **Wav2Vec2** transformer models for audio processing.
- Trained on datasets like **RAVDESS**, **TESS**, and gender-specific datasets.
- ML Models used:
  - 🎯 Emotion: `Wav2Vec2` (fine-tuned for English speech emotion recognition)
  - 👤 Gender: `Wav2Vec2` (fine-tuned for gender recognition)

---

📦 Accuracy:
- Gender Detection: ~95% (based on model evaluation)
- Emotion Detection: ~85% (based on model evaluation)
""")