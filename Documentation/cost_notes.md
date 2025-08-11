
# Mistral Model Cost Notes

- **Model:** mistralai/Mistral-7B-Instruct-v0.3
- **Load in 4-bit Quantization:** Yes (nf4) — reduces VRAM cost.
- **Runtime Environment:** Google Cloud VM with NVIDIA T4 GPU.
- **Average Latency per Sample:** 4.443 sec
- **Estimated Cost:** Depends on GPU rental time; with T4 on GCP preemptible instance, ~$0.3500 per hour.

> Note: Cost estimates exclude dataset preparation and storage.
