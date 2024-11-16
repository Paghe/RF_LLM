import numpy as np
import soundfile as sf

# Function to convert binary to text
def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

# Step 1: Read the transmitted signal
# received_signal, fs = sf.read("transmitted_signal.wav")
received_signal, fs = sf.read("noisy_transmitted_signal.wav")
samples_per_bit = fs // 10  # Same as transmitter

# Step 2: Demodulate the signal
decoded_bits = []
for i in range(0, len(received_signal), samples_per_bit):
    segment = received_signal[i:i+samples_per_bit]
    avg_amplitude = np.mean(np.abs(segment))
    if avg_amplitude > 0.5:  # Threshold for binary 1
        decoded_bits.append('1')
    else:
        decoded_bits.append('0')

binary_data_received = ''.join(decoded_bits)
print("Received Binary Data:", binary_data_received)

# Step 3: Convert binary back to text
received_message = binary_to_text(binary_data_received)
print("Received Message:", received_message)
