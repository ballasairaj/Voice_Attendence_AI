import os

# Fix OpenMP duplicate library issue
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from faster_whisper import WhisperModel

# Load Whisper model
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


# Function to convert audio into text
def transcribe_audio(audio_path):

    # Convert speech into text
    segments, info = model.transcribe(audio_path)

    full_text = ""

    # Combine all segments
    for segment in segments:

        full_text += segment.text + " "

    return full_text.strip()