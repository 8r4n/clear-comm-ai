from speechbrain.pretrained import SpectralMaskEnhancement

model = SpectralMaskEnhancement.from_hparams(
    source="speechbrain/metricgan-plus-voicebank",
)

model.enhance_file("example.wav", format="wav")