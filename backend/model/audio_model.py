import sys
import os

# Ensure backend/model is in sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from predict import predict_gender_emotion

def predict_audio(audio_path):
    """
    Predict gender and emotion from an audio file.
    
    Args:
        audio_path (str): Path to the WAV audio file.
    
    Returns:
        tuple: (gender, emotion) or ("Error", error_message) if prediction fails.
    """
    try:
        if not os.path.exists(audio_path):
            return "Error", "Audio file not found"
        gender, emotion = predict_gender_emotion(audio_path)
        return gender, emotion
    except Exception as e:
        return "Error", f"Prediction failed: {str(e)}"