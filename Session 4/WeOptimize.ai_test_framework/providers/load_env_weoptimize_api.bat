@echo off
setlocal enabledelayedexpansion

rem ==== Search for .env.weoptimize.ai in ., .., ..\.., ..\..\.. (up to 4 parents) ====
set "ENVFILE="
for %%D in (".","..","..\..","..\..\..","..\..\..\..") do (
  if exist "%%~fD\.env.weoptimize.ai" (
    set "ENVFILE=%%~fD\.env.weoptimize.ai"
    goto :found_env
  )
)

echo [WARN] No .env.weoptimize.ai file found in current or up to 4 parent directories.
goto :end

:found_env
echo [INFO] Found .env.weoptimize.ai at: %ENVFILE%

rem ==== Load environment variables from .env.weoptimize.ai ====
for /f "usebackq tokens=1,* delims==" %%a in ("%ENVFILE%") do (
  set "%%a=%%b"
  setx %%a "%%b" >nul
  echo [OK] Set %%a=%%b

   rem ==== Sync with .env (update if exists, else append) ====
  set "TARGET_ENV=.env"
  if exist "%TARGET_ENV%" (
    rem Remove any existing line for %%a=
    findstr /V /B /C:"%%a=" "%TARGET_ENV%" >"%TARGET_ENV%.tmp"
    move /Y "%TARGET_ENV%.tmp" "%TARGET_ENV%" >nul
  )
  echo %%a=%%b>>"%TARGET_ENV%"
  echo [SYNC] %%a set in %TARGET_ENV% as %%b
)

rem ==== Confirm (use delayed expansion here) ====
echo Inside batch: WEOPTIMIZE_API_KEY=!WEOPTIMIZE_API_KEY!

rem ==== Curl test ====
curl -X POST "https://api.weoptimize.ai/chats/promptfoo/session" ^
  -H "Content-Type: application/json" ^
  -H "x-api-key: !WEOPTIMIZE_API_KEY!" ^
  -d "{\"email\":\"kavita.jadhav1109@gmail.com\",\"messages\":[{\"role\":\"user\",\"content\":\"Test message\"}]}"

:end
echo.
echo Finished. Open a NEW cmd window and run:
echo   echo %%WEOPTIMIZE_API_KEY%%
echo (because setx writes permanently, but old windows won’t see it).

pause


