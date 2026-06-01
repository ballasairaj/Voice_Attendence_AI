import os

from dotenv import load_dotenv

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral client
client = MistralClient(api_key=api_key)


def detect_attendance_status(text):

    prompt = f"""
    You are an attendance assistant.

    Analyze the student's response.

    Student Response:
    "{text}"

    Rules:

    Return ONLY:

    STUDENT IS PRESENT

    OR

    STUDENT IS ABSENT

    Examples:

    Present sir -> STUDENT IS PRESENT
    Present mam -> STUDENT IS PRESENT
    Yes sir -> STUDENT IS PRESENT
    Yes mam -> STUDENT IS PRESENT
    I am here -> STUDENT IS PRESENT
    Here teacher -> STUDENT IS PRESENT

    Good morning -> STUDENT IS ABSENT
    Hello -> STUDENT IS ABSENT
    Thank you -> STUDENT IS ABSENT
    Can I come in -> STUDENT IS ABSENT
    """

    response = client.chat(

        model="mistral-small-latest",

        messages=[
            ChatMessage(
                role="user",
                content=prompt
            )
        ]
    )

    status = response.choices[0].message.content.strip()

    print(f"\nMistral Response: {status}")

    return status





# import os

# from dotenv import load_dotenv

# from mistralai.client import MistralClient
# from mistralai.models.chat_completion import ChatMessage


# # Load environment variables
# load_dotenv()

# # Get API key
# api_key = os.getenv("MISTRAL_API_KEY")

# # Initialize Mistral client
# client = MistralClient(api_key=api_key)


# # Function to detect attendance confirmation intent
# def detect_attendance_intent(text):

#     prompt = f"""
#     You are an AI attendance assistant.

#     Determine whether the following sentence
#     is a classroom attendance confirmation response.

#     Examples of YES:
#     - present sir
#     - present teacher
#     - yes mam
#     - yes sir

#     - yes teacher
#     - i am here
#     - here sir
#     - here teacher
#     - here mam
#     - i am present
#     - here
#     - Present
#     - Yes

#     Examples of NO:
#     - absent sir
#     - not present
#     - no mam
#     - no sir
#     - no teacher
    
#     - good morning
#     - can i come in
#     - hello
#     - thank you

#     Sentence:
#     "{text}"

#     Reply ONLY with:
#     YES, STUDENT IS PRESENT
#     or
#     NO, STUDENT IS ABSENT
#     """

#     response = client.chat(

#         model="mistral-small-latest",

#         messages=[
#             ChatMessage(
#                 role="user",
#                 content=prompt
#             )
#         ]
#     )

#     answer = response.choices[0].message.content.strip()

#     print(f"\nMistral Response: {answer}")

#     return "YES" in answer.upper()