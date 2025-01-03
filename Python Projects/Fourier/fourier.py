import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
from scipy.io import wavfile

# Les inn WAV-filen (erstatt 'output.wav' med din egen fil)
samplerate, data = wavfile.read('529.wav')

# Hvis lyden er stereo, ta kun én kanal for enkelhet
if len(data.shape) > 1:
    data = data[:, 0]

N = len(data)

# Utfør FFT
Y = fft.fft(data)
freqs = fft.fftfreq(N, 1/samplerate)

# Fokuser på den positive halvparten av spekteret
half = N // 2
freqs_half = freqs[:half]
Y_half = np.abs(Y[:half])

# Plotte frekvensspekteret
plt.figure(figsize=(10, 6))
plt.plot(freqs_half, Y_half)
plt.title('Frekvensspekter')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('Amplitudestyrke')
plt.grid(True)
plt.tight_layout()
plt.show()

# Finn de frekvensene med størst utslag (amplitude)
# Sorter frekvenser etter amplitude i synkende rekkefølge
sorted_indices = np.argsort(Y_half)[::-1]  # Sorterer indeksene basert på amplitude, stigende, og snur rekkefølgen
top_n = 20  # Antall toppelementer du vil liste ut
top_frequencies = freqs_half[sorted_indices[:top_n]]
top_amplitudes = Y_half[sorted_indices[:top_n]]

# Skriv ut de topp 10 frekvensene med størst utslag
print("Topp 10 frekvenser med størst amplitude:")
for f, A in zip(top_frequencies, top_amplitudes):
    print(f"Frekvens: {f:.2f} Hz, Amplitude: {A:.2f}")
