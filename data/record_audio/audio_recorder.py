import sounddevice as sd
import numpy as np
import wavio
import datetime

# Audio recording settings
sample_rate = 44100  # Samples per second
duration = 600  # Duration in seconds (adjust as needed)
output_filename = f"interview_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.wav"

# Record audio
print(f"Recording audio to {output_filename}. Press Ctrl+C to stop...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
sd.wait()

# Save audio to a WAV file
wavio.write(output_filename, audio_data, sample_rate, sampwidth=2)

print(f"Audio recording saved as {output_filename}.")
