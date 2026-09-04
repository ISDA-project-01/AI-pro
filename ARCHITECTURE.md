# System Architecture

```text
                    USER
                     │
                     ▼
              ┌──────────────┐
              │  Open WebUI  │
              └──────┬───────┘
                     │
                     ▼
          ┌────────────────────┐
          │ Local AI Controller│
          └─────────┬──────────┘
                    │
                    ▼
               ┌─────────┐
               │ Ollama  │
               └────┬────┘
                    │
             ONE ACTIVE MODEL
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Llama       Qwen        DeepSeek
```

## Component Roles
- **Open WebUI**: Primary Web UI interface.
- **Local AI Controller**: Flask/Python orchestration layer (`app.py`, `main.py`).
- **Ollama**: Local inference server on `http://127.0.0.1:11434`.
