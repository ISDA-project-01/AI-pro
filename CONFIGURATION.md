# Configuration Guide

Configuration parameters are loaded from `.env` or system environment variables into `config.py`.

## Key Parameters
- `OLLAMA_HOST`: URL for Ollama service (default: `http://127.0.0.1:11434`).
- `DEFAULT_MODEL`: Default starting model (`llama3.2:3b`).
- `CONTEXT_LENGTH`: Context window in tokens (default: `8192`).
- `TEMPERATURE`: Response randomness (default: `0.7`).
- `WEB_SEARCH_ENABLED`: Set `true` to enable web search.
- `CODE_EXECUTION_ENABLED`: Set `true` to enable Python code execution.
