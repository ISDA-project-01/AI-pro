# Performance Tuning

## Optimizing Speed on CPU & 8 GB RAM
1. **Thread Allocation**: Ollama automatically detects CPU cores. Ensure background tasks are minimized.
2. **Context Window**: Keep `CONTEXT_LENGTH` between 4096 and 8192 to prevent excessive CPU memory usage.
3. **Quantization**: Use standard 4-bit (q4_K_M) model weights available via Ollama tags.
