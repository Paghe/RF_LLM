import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Function to convert text to binary
def text_to_binary(text):
	return ''.join(format(ord(char), '08b') for char in text)

# Parameters
fs = 44100  # Sampling frequency (samples per second)
carrier_freq = 3000  # Carrier frequency (Hz)
samples_per_bit = fs // 10  # 10 bits per second
text_message = "Hello World! This is the end!"

# Step 1: Convert text to binary
binary_data = text_to_binary(text_message)
print("Binary Data:", binary_data)

# Step 2: Generate RF signal (Amplitude Modulation)
time_per_bit = np.linspace(0, 1, samples_per_bit, endpoint=False)
modulated_signal = []

for bit in binary_data:
    carrier = np.sin(2 * np.pi * carrier_freq * time_per_bit)  # Carrier wave
    if bit == '1':
        modulated_signal.extend(carrier)  # Full amplitude for binary 1
    else:
        modulated_signal.extend(0.3 * carrier)  # Reduced amplitude for binary 0

modulated_signal = np.array(modulated_signal)

# Step 3: Add noise with adjustable intensity
noise_std_dev = 0.2  # Standard deviation of noise (adjust this value)
noise = np.random.normal(0, noise_std_dev, modulated_signal.shape)
noisy_signal = modulated_signal + noise

# Save the noisy RF signal
sf.write("noisy_transmitted_signal.wav", noisy_signal, fs)
print(f"Noisy transmitted signal saved with noise_std_dev = {noise_std_dev}")

# Step 4: Visualize the noisy modulated signal
plt.plot(noisy_signal[:1000])  # Plot first 1000 samples
plt.title("Noisy Amplitude Modulated Signal (Transmitted)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

