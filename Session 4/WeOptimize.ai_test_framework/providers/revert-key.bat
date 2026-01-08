@echo off
setlocal

set "YAML=providers.yaml"
set "BACKUP=providers.yaml.bak"

if not exist "%BACKUP%" (
  echo [ERROR] Backup file "%BACKUP%" not found.
  echo Nothing to revert.
  exit /b 1
)

echo [INFO] Restoring "%YAML%" from "%BACKUP%"...
copy /Y "%BACKUP%" "%YAML%" >nul
if errorlevel 1 (
  echo [ERROR] Failed to restore "%YAML%".
  exit /b 1
)

echo [INFO] Deleting backup "%BACKUP%"...
del /Q "%BACKUP%" >nul
if errorlevel 1 (
  echo [WARN] Could not delete "%BACKUP%".
) else (
  echo [OK] Backup deleted.
)

echo [OK] "%YAML%" has been reverted to use the placeholder: ${WEOPTIMIZE_API_KEY}.
exit /b 0

pause