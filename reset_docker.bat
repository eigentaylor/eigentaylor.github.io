@echo off
echo.
echo 🐳 al-folio Docker Reset Script
echo ========================================
echo.

REM Check if docker-compose.yml exists
if not exist "docker-compose.yml" (
    echo ❌ Error: docker-compose.yml not found!
    echo    Make sure you're running this script from the al-folio project directory.
    pause
    exit /b 1
)

echo 🔄 Stopping Docker containers...
docker compose down
if %errorlevel% equ 0 (
    echo ✅ Containers stopped successfully
) else (
    echo ⚠️  Warning: Failed to stop containers ^(they might not be running^)
)

echo.
REM Accept optional first arg: skippull to avoid pulling images when offline
set SKIP_PULL=0
if /I "%1"=="skippull" (
    set SKIP_PULL=1
)

if %SKIP_PULL%==1 (
    echo ⏭️ Skipping docker image pull (skippull flag detected)
) else (
    echo 🔄 Pulling latest Docker images...
    docker compose pull
    if %errorlevel% neq 0 (
        echo ❌ Failed to pull Docker images. Exiting.
        pause
        exit /b 1
    )
    echo ✅ Images pulled successfully
)

echo.
echo 🚀 Starting Docker containers...
docker compose up -d
if %errorlevel% neq 0 (
    echo ❌ Failed to start containers. Exiting.
    pause
    exit /b 1
)
echo ✅ Containers started successfully

echo.
echo ⏳ Waiting for container to fully start...
timeout /t 5 /nobreak > nul

echo.
echo 📊 Checking container status...
docker compose ps

echo.
echo 📋 Recent container logs:
docker compose logs --tail=10

echo.
echo ========================================
echo 🎉 Docker reset complete!
echo 🌐 Your site should be available at: http://localhost:8080
echo 📝 To view live logs: docker compose logs -f
echo 🛑 To stop containers: docker compose down
echo.
pause
