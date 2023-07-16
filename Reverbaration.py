import numpy as np
import scipy.signal as signal
import sounddevice as sd

G = 0.6
Td = 0.12
fs = 48000

N = int(np.round(Td * fs))
b = np.concatenate(([1], np.zeros(N-1), [-G]))
a = np.array([1])

inputFile = 'countdown.wav'  # Replace with the actual audio file name

inputSignal, fs = sd.read(inputFile)  # Read the audio file
outputSignal = signal.lfilter(b, a, inputSignal)  # Apply the filter

sd.play(outputSignal, fs)  # Play the filtered audio

# Wait until the sound finishes playing
sd.wait()
