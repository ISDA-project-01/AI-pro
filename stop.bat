@echo off
echo Stopping Local AI Assistant Services...
python main.py unload
taskkill /FI "WINDOWTITLE eq Local AI Controller*" /F 2>nul
echo Services stopped safely.
pause
