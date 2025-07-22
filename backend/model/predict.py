import torch
import librosa
import os
from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2ForSequenceClassification
import random
import numpy as np

torch.manual_seed(42)
np.random.seed(42)
random.seed(42)

# Load processors and models
emotion_model_id = "r-f/wav2vec-english-speech-emotion-recognition"
gender_model_id = "alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech"

emotion_processor = Wav2Vec2FeatureExtractor.from_pretrained(emotion_model_id)
emotion_model = Wav2Vec2ForSequenceClassification.from_pretrained(emotion_model_id)
emotion_model.eval()

gender_processor = Wav2Vec2FeatureExtractor.from_pretrained(gender_model_id)
gender_model = Wav2Vec2ForSequenceClassification.from_pretrained(gender_model_id)
gender_model.eval()

def predict_gender_emotion(audio_path):
    """
    Predict gender and emotion from an audio file.
    
    Args:
        audio_path (str): Path to the WAV audio file.
    
    Returns:
        tuple: (gender, emotion)
    """
    # Load audio
    waveform, sr = librosa.load(audio_path, sr=16000)

    # Emotion prediction
    inputs_emotion = emotion_processor(
        waveform, sampling_rate=16000, return_tensors="pt", padding=True
    )
    with torch.no_grad():
        logits_emotion = emotion_model(**inputs_emotion).logits
    predicted_emotion_id = torch.argmax(logits_emotion, dim=-1).item()
    emotion = emotion_model.config.id2label[predicted_emotion_id]

    # Gender prediction
    inputs_gender = gender_processor(
        waveform, sampling_rate=16000, return_tensors="pt", padding=True
    )
    with torch.no_grad():
        logits_gender = gender_model(**inputs_gender).logits
    predicted_gender_id = torch.argmax(logits_gender, dim=-1).item()
    gender = gender_model.config.id2label[predicted_gender_id]

    return gender, emotion

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "1001_DFA_ANG_XX.wav")
    gender, emotion = predict_gender_emotion(file_path)
    print(f"Gender: {gender}, Emotion: {emotion}")