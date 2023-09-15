import os
import sys
import json
import vosk   #pip install vosk

def transcribe_audio(audio_file):
    model_path = "vosk-model-small-en-us-0.15"  # Replace with the path to your Vosk model

    if not os.path.exists(model_path):
        print("Vosk model not found. Download it from https://alphacephei.com/vosk/models and extract it.")
        sys.exit(1)

    vosk.SetLogLevel(-1)  # Disable Vosk logging

    # Initialize the recognizer with the Vosk model
    recognizer = vosk.KaldiRecognizer(model_path, 16000)

    # Open the audio file
    with open(audio_file, "rb") as f:
        audio_data = f.read()

    # Initialize variables for transcript and remaining audio
    transcript = ""
    remaining_audio = audio_data

    while len(remaining_audio) > 0:
        chunk, remaining_audio = remaining_audio[:4096], remaining_audio[4096:]
        if recognizer.AcceptWaveform(chunk):
            result = recognizer.Result()
            transcript += json.loads(result)["text"]

    # Process the last chunk and finalize the transcript
    result = recognizer.FinalResult()
    transcript += json.loads(result)["text"]

    return transcript

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe_audio.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]

    if not os.path.exists(audio_file):
        print("Audio file not found.")
        sys.exit(1)

    transcript = transcribe_audio(audio_file)
    print("Transcript:")
    print(transcript)
