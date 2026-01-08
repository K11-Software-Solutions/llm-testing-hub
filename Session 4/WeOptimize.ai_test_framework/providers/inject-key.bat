@echo off
setlocal enabledelayedexpansion

set "YAML=providers.yaml"
set "BACKUP=providers.yaml.bak"

if "%WEOPTIMIZE_API_KEY%"=="" (
  echo [ERROR] WEOPTIMIZE_API_KEY is not set in environment.
  echo Use:  setx WEOPTIMIZE_API_KEY your_key_here
  exit /b 1
)

if not exist "%YAML%" (
  echo [ERROR] %YAML% not found.
  exit /b 1
)

echo [INFO] Backing up %YAML% to %BACKUP%...
copy /Y "%YAML%" "%BACKUP%" >nul

echo [INFO] Injecting API key into %YAML%...
(for /f "usebackq delims=" %%L in ("%BACKUP%") do (
  set "line=%%L"
  set "line=!line:${WEOPTIMIZE_API_KEY}=%WEOPTIMIZE_API_KEY%!"
  echo(!line!
)) > "%YAML%"

echo [OK] Replacement complete.
echo.
echo Tip: Your key is now baked into %YAML%. 
echo      If you don't want to commit it to Git, add it to .gitignore.
