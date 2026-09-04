# Requirements

## Minimum System Requirements
- **OS**: Windows 10 (64-bit)
- **RAM**: 8 GB
- **Storage**: 15 GB available space (for storing 8 GGUF model files)
- **CPU**: Intel Core i5 (4th Gen+) or AMD Ryzen 3+
- **GPU**: None required (CPU-only execution)

## Python Dependencies
Required minimal libraries:
- `requests >= 2.31.0`
- `psutil >= 5.9.0`
- `python-dotenv >= 1.0.0`
- `flask >= 3.0.0`

## Optional Voice Dependencies
- `openai-whisper` (for speech-to-text)
- `torch` / `transformers` (for TTS synthesis)
