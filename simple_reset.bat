@echo off
echo Stopping containers...
docker compose down

echo Pulling latest images...
docker compose pull

echo Starting containers...
docker compose up -d

echo Done! Your site should be at http://localhost:8080
pause
