@echo off
setlocal EnableDelayedExpansion

echo [INFO] Cleaning up all results.html and .env files in %CD% and subfolders...

rem Delete results.html files
for /R %%F in (results.html) do (
  if exist "%%F" (
    echo [DEL] Deleting "%%F"
    del /F /Q "%%F"
  )
)

rem Delete .env files
for /R %%F in (.env) do (
  if exist "%%F" (
    echo [DEL] Deleting "%%F"
    del /F /Q "%%F"
  )
)

rem ==== Cleanup promptfoo-errors.log in nested folders (skip node_modules) ====
set "CLEAN_ROOT=%CD%"
set /a ERRCOUNT=0

for /f "delims=" %%F in ('
  dir /b /s /a:-d "%CLEAN_ROOT%\promptfoo-errors.log" ^| findstr /I /V "\\node_modules\\"
') do (
  del /f /q "%%F" && set /a ERRCOUNT+=1
)

echo [INFO] Removed !ERRCOUNT! promptfoo-errors.log file(s).

echo [INFO] Cleanup complete.
pause
endlocal
