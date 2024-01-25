# importing libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# sampling frequency
freq = 44100

# recording duration
duration = 12

# start recorder with the given values of duration and sampling frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# record audio for given number of seconds
sd.wait()

# This will convert the Numpy array to an audio file with the given sampling frequency
wv.write("recording1.wav", recording, freq, sampwidth=2)
