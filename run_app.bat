@echo off
echo ========================================================
echo Starting Intelligent Ticket Routing System...
echo ========================================================

REM Start Backend
echo [1/2] Starting Python FastAPI Backend on port 8000...
start "Backend API" cmd /k "cd backend && .\venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000"

REM Start Frontend
echo [2/2] Starting React Vite Frontend on port 5173...
REM We use the absolute path fallback for node/npm just in case your PATH variable hasn't fully updated yet.
set "PATH=C:\Program Files\nodejs;%PATH%"
start "Frontend UI" cmd /k "cd frontend && npm.cmd run dev"

echo.
echo Both applications are booting up in separate terminal windows!
echo.
echo - Your API will be at: http://localhost:8000
echo - Your UI will be at: http://localhost:5173
echo.
pause
