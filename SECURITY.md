# Security Policy

## Reporting Vulnerabilities
Please report security concerns responsibly by contacting the maintainers directly. Do not open public issues for zero-day vulnerabilities.

## Local API Safety
- The controller API binds to `127.0.0.1` by default.
- Do NOT expose Ollama or the local controller API publicly without proper firewall rules and authentication safeguards.
- Code execution and terminal execution features are disabled by default.
