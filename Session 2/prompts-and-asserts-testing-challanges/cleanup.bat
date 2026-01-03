@echo off
echo [INFO] Starting cleanup...

REM Delete .env in current folder
if exist ".env" (
  del /f /q ".env"
  echo [OK] Deleted .env
) else (
  echo [WARN] No .env file found
)

REM Delete results.html in current folder
if exist "results.html" (
  del /f /q "results.html"
  echo [OK] Deleted results.html
) else (
  echo [WARN] No results.html file found
)

echo [INFO] Cleanup complete.
pause
