# # import whisper
# # import librosa
# # import tempfile
# # import soundfile as sf

# # # Load Whisper model
# # model = whisper.load_model("base")


# # def transcribe_audio(uploaded_file):

# #     # Save uploaded file temporarily
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
# #         tmp.write(uploaded_file.read())
# #         audio_path = tmp.name

# #     # Load audio using librosa
# #     audio, sr = librosa.load(audio_path, sr=16000)

# #     # Save normalized audio
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp2:
# #         sf.write(tmp2.name, audio, sr)
# #         processed_path = tmp2.name

# #     # Whisper transcription
# #     result = model.transcribe(processed_path)

# #     return result["text"]

# import whisper
# import tempfile
# import librosa
# import numpy as np

# # Load Whisper model once
# model = whisper.load_model("base")


# def transcribe_audio(uploaded_file):

#     # Save uploaded file temporarily
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
#         tmp.write(uploaded_file.read())
#         audio_path = tmp.name

#     # Load audio with librosa
#     audio, sr = librosa.load(audio_path, sr=16000, mono=True)

#     # Convert to float32 numpy array
#     audio = np.array(audio, dtype=np.float32)

#     # Whisper transcription
#     result = model.transcribe(audio)

#     return result["text"]

import whisper
import tempfile

# Load Whisper model
model = whisper.load_model("base")


def transcribe_audio(uploaded_file):

    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    # Let Whisper handle preprocessing
    result = model.transcribe(audio_path)

    return result["text"]