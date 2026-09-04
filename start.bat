@echo off
echo Starting Local AI Assistant Services...
start /b python main.py health
start /b python app.py
timeout /t 3 /nobreak >nul
start http://127.0.0.1:8080
echo Controller & UI started!
