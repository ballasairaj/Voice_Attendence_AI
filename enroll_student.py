from utils.audio_recorder import record_audio

# Student name input
student_name = input("Enter student name: ").lower()

# Save student voice sample
audio_path = f"voices/{student_name}.wav"

# Record student voice
record_audio(audio_path, duration=5)

print("Student voice enrolled successfully")