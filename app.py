import os
import warnings

warnings.filterwarnings("ignore")

from utils.audio_recorder import record_audio
from utils.speech_to_text import transcribe_audio
from utils.intent_detector import detect_attendance_status
from utils.speaker_verification import verify_speaker
from utils.attendance_manager import (
    create_attendance_table,
    mark_attendance
)

# Create attendance table
create_attendance_table()

# Teacher enters student name
teacher_called_name = input(
    "\nEnter called student name: "
).lower()

# Registered student voice path
registered_voice = (
    f"voices/{teacher_called_name}.wav"
)

# Check if student is enrolled
if not os.path.exists(registered_voice):

    print("\nStudent not enrolled")

    exit()

print(
    f"\nWaiting for {teacher_called_name} response..."
)

# Record student's response
response_audio = "response.wav"

record_audio(
    response_audio,
    duration=5
)

# Convert speech to text
detected_text = transcribe_audio(
    response_audio
)

print(
    f"\nDetected Text: {detected_text}"
)

# Get attendance status from Mistral
attendance_status = (
    detect_attendance_status(
        detected_text
    )
)

print(
    f"\nAttendance Status: {attendance_status}"
)

# Speaker verification
# (Only for display / monitoring)
speaker_result = verify_speaker(
    registered_voice,
    response_audio
)

print(
    f"\nSpeaker Verification: {speaker_result}"
)

# --------------------------------------------------
# DATABASE UPDATE DEPENDS ONLY ON MISTRAL RESPONSE
# --------------------------------------------------

if attendance_status == "STUDENT IS PRESENT":

    mark_attendance(
        teacher_called_name,
        "PRESENT"
    )

    print(
        "\nAttendance Marked: PRESENT"
    )

elif attendance_status == "STUDENT IS ABSENT":

    mark_attendance(
        teacher_called_name,
        "ABSENT"
    )

    print(
        "\nAttendance Marked: ABSENT"
    )

else:

    print(
        "\nUnexpected Mistral Response"
    )


# import os
# import warnings

# warnings.filterwarnings("ignore")

# from utils.audio_recorder import record_audio

# from utils.speech_to_text import transcribe_audio

# from utils.intent_detector import detect_attendance_intent

# from utils.speaker_verification import verify_speaker

# from utils.attendance_manager import (
#     create_attendance_table,
#     mark_attendance
# )


# # Create attendance database table
# create_attendance_table()


# # Teacher enters called student name
# teacher_called_name = input(
#     "\nEnter called student name: "
# ).lower()


# # Path of enrolled student voice
# registered_voice = (
#     f"voices/{teacher_called_name}.wav"
# )


# # Check whether student is enrolled
# if not os.path.exists(registered_voice):

#     print("\nStudent not enrolled")

#     exit()


# print(f"\nWaiting for {teacher_called_name} response...")


# # Record student response
# response_audio = "response.wav"

# record_audio(
#     response_audio,
#     duration=5
# )


# # Convert speech into text
# detected_text = transcribe_audio(
#     response_audio
# )

# print(f"\nDetected Text: {detected_text}")


# # Detect attendance confirmation intent

# intent_result = detect_attendance_intent(
#     detected_text
# )

# print(f"\nIntent Result: {intent_result}")


# # Verify speaker identity
# speaker_result = verify_speaker(
#     registered_voice,
#     response_audio
# )

# print(f"\nSpeaker Verification: {speaker_result}")


# # Final attendance decision
# if intent_result and speaker_result:

#     mark_attendance(
#         teacher_called_name
#     )

#     print("\nAttendance Marked Successfully")

# else:

#     print("\nAttendance Verification Failed")