import os

# Fix OpenMP issue
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Disable symlink warnings
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from speechbrain.pretrained import SpeakerRecognition


# Load speaker verification model
verification = SpeakerRecognition.from_hparams(

    source="speechbrain/spkrec-ecapa-voxceleb",

    savedir="pretrained_models/spkrec-ecapa-voxceleb",

    run_opts={
        "device": "cpu"
    }
)


# Function to verify speaker
def verify_speaker(registered_audio, test_audio):

    try:

        # IMPORTANT:
        # Convert paths into absolute paths
        registered_audio = os.path.abspath(
            registered_audio
        )

        test_audio = os.path.abspath(
            test_audio
        )

        print(f"\nRegistered Audio: {registered_audio}")

        print(f"Test Audio: {test_audio}")

        # Compare both audio files
        score, prediction = verification.verify_files(

            registered_audio,
            test_audio
        )

        similarity_score = score.item()

        print(f"\nSimilarity Score: {similarity_score}")

        # Custom threshold
        if similarity_score > 0.50:

            print("Speaker Verified")

            return True

        else:

            print("Speaker Not Verified")

            return False

    except Exception as e:

        print(f"\nSpeaker Verification Error: {e}")

        return False