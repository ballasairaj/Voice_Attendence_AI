import sounddevice as sd
from scipy.io.wavfile import write

# Function to record audio from microphone
def record_audio(filename, duration=6, sample_rate=16000):

    print("Recording Started...")

    # Record audio
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )

    # Wait until recording completes
    sd.wait()

    # Save audio file
    write(filename, sample_rate, audio)

    print(f"Audio saved as {filename}")