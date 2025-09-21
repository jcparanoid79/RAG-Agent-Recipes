@echo off
echo Starting AI Recipe Finder Application...

echo.
echo Starting Backend API...
start "Backend API" /min cmd /c "python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"

echo.
echo Waiting for API to start...
timeout /t 5 /nobreak >nul

echo.
echo Starting Frontend...
start "Frontend" /min cmd /c "cd frontend && python -m http.server 8080"

echo.
echo Setup complete!
echo.
echo Backend API is running at: http://localhost:8000
echo Frontend is available at: http://localhost:8080
echo.
echo Press any key to exit...
pause >nul