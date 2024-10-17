## Needed imports: pip install pydub simpleaudio numpy
import serial
import time
import numpy as np
import simpleaudio as sa

# Function to generate a sine wave tone
def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude of 0.5
    audio = tone * (2**15 - 1)  # Convert to 16-bit audio
    return audio.astype(np.int16)  # Convert to int16

# Replace 'COM3' with your Arduino's port
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for the Arduino to reset

try:
    while True:
        # Read data from the Arduino
        if arduino.in_waiting > 0:
            ldr_value = arduino.readline().decode('utf-8').rstrip()
            print(ldr_value)  # Print the LDR value for debugging

            # Check if the light level is low
            if int(ldr_value) < 300:  # Adjust the threshold as needed
                # Generate a tone for a piano key (e.g., C4, 261.63 Hz)
                frequency = 261.63  # Frequency for middle C
                duration = 1.0  # 1 second duration
                wave = generate_sine_wave(frequency, duration)

                # Play the generated sound
                play_wave = sa.play_buffer(wave, num_channels=1, bytes_per_sample=2, sample_rate=44100)
                play_wave.wait_done()  # Wait until sound finishes

except KeyboardInterrupt:
    pass
finally:
    arduino.close()
