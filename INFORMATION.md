# Project Information

## Overview
The Local AI Assistant Platform delivers a ChatGPT-like AI experience entirely locally on Windows 10 without requiring cloud servers, subscriptions, or expensive dedicated GPUs.

## Why Local AI on 8 GB RAM?
Most cloud AI systems process user prompts externally. This local platform processes queries on your own machine. Running on 8 GB RAM requires strict memory management—loading only one lightweight quantized LLM (1.0B-3.8B parameters) into memory at a time.

## Architectural Design
The architecture splits responsibility into three layers:
1. **Frontend**: Open WebUI provides a clean browser chat interface.
2. **Orchestration**: Python Local AI Controller manages model switching, memory unloading, RAG context, and safety.
3. **Inference Engine**: Ollama handles GGUF quantized model execution on CPU.
