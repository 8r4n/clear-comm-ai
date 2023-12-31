import torchaudio

# Download the YESNO dataset
yesno_data = torchaudio.datasets.YESNO('.', download=True)

# Get the waveform and sample rate of the first audio file
waveform, sample_rate = yesno_data[0]

# Save the waveform as a WAV file
torchaudio.save("example.wav", waveform, sample_rate)