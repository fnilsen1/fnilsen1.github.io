import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

# Function to plot Fourier Transform
def plot_fourier_transform(audio_file):
    # Load the audio file
    sample_rate, data = wavfile.read(audio_file)

    # If stereo, select only one channel
    if len(data.shape) == 2:
        data = data[:, 0]

    # Number of samples
    N = len(data)

    # Fourier transform and frequencies
    fft_data = fft(data)
    fft_data = np.abs(fft_data[:N//2])  # Take the positive half of the spectrum

    freqs = np.fft.fftfreq(N, 1/sample_rate)
    freqs = freqs[:N//2]  # Positive frequencies only

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(freqs, fft_data)
    plt.title('Fourier Transform of the Audio Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

# Usage
audio_file = 'Python Projects\Fourier\c-major-chord.mp3'  # Replace with the path to your audio file
plot_fourier_transform(audio_file)
