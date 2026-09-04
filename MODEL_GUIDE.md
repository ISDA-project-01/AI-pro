# Model Guide

## Supported Models Overview

| Model Tag | Name | Size | Recommended Role |
| :--- | :--- | :--- | :--- |
| `llama3.2:3b` | Llama 3.2 3B | 2.0 GB | General Chat & RAG |
| `gemma2:2b` | Gemma 2 2B | 1.6 GB | Fast Q&A & Summaries |
| `phi3.5:3.8b` | Phi 3.5 3.8B | 2.2 GB | Productivity & Writing |
| `qwen2.5-coder:3b` | Qwen2.5-Coder 3B | 1.9 GB | Code Generation & Debugging |
| `deepseek-r1:1.5b` | DeepSeek-R1 1.5B | 1.1 GB | Logic & Math Reasoning |
| `openelm:3b` | OpenELM 3B | 1.8 GB | Lightweight Assistant |
| `ministral:3b` | Ministral 3B | 2.1 GB | Tool Experimentation |
| `smollm2:1.7b` | SmolLM2 1.7B | 1.0 GB | Ultra-fast Assistant |

## Memory Lifecycle
All models reside on disk after download. When a model is selected, `model_manager.py` sends an unload signal to Ollama to free RAM before loading the newly chosen model.
