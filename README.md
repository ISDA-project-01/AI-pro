# Local AI Assistant Platform

A production-quality local ChatGPT-style AI assistant platform for Windows 10 designed specifically for CPU-only systems with 8 GB RAM using **Ollama** and **Open WebUI**.

## Overview
This platform coordinates Ollama and Open WebUI through a lightweight Python controller. It supports 8 targeted lightweight models, local RAG document query, memory, secure execution, and optional speech features (Whisper / Tamil TTS).

## Core Principles
1. **8 GB RAM & CPU Optimized**: Runs lightweight models (1.0B to 3.8B parameters).
2. **One-Model-Active Policy**: Automatically unloads inactive models from memory before switching.
3. **Private & Local-First**: Runs offline without requiring cloud services or external API keys.

## Supported Models
- **llama3.2:3b**: General Chat
- **gemma2:2b**: Fast Chat
- **phi3.5:3.8b**: Reasoning & Writing
- **qwen2.5-coder:3b**: Coding & Programming
- **deepseek-r1:1.5b**: Mathematical & Logical Reasoning
- **openelm:3b**: General Assistant
- **ministral:3b**: Tool Experimentation
- **smollm2:1.7b**: Ultra-fast Simple Assistant

## Quick Start
1. Run `setup.bat` (or `setup.ps1` in PowerShell).
2. Launch services using `start.bat`.
3. Stop services using `stop.bat`.

## CLI Usage
```bash
python main.py health
python main.py status
python main.py models
python main.py switch-model qwen2.5-coder:3b
python main.py unload
```

## License
[MIT License](LICENSE.md)
