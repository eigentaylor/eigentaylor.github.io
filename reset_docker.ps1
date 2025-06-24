# al-folio Docker Reset Script for Windows
# This script stops, removes, and restarts the Docker container for local development.

Write-Host "🐳 al-folio Docker Reset Script" -ForegroundColor Cyan
Write-Host "=" * 40 -ForegroundColor Cyan

# Check if docker-compose.yml exists
if (-not (Test-Path "docker-compose.yml")) {
    Write-Host "❌ Error: docker-compose.yml not found!" -ForegroundColor Red
    Write-Host "   Make sure you're running this script from the al-folio project directory." -ForegroundColor Yellow
    exit 1
}

# Stop and remove containers
Write-Host "🔄 Stopping Docker containers..." -ForegroundColor Yellow
try {
    docker compose down
    Write-Host "✅ Containers stopped successfully" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Warning: Failed to stop containers (they might not be running)" -ForegroundColor Yellow
}

# Optional: Remove Docker images for fresh start
Write-Host "`n🔄 Removing Docker images for fresh start..." -ForegroundColor Yellow
try {
    docker compose down --rmi all
    Write-Host "✅ Images removed successfully" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Warning: Failed to remove images" -ForegroundColor Yellow
}

# Pull latest images
Write-Host "`n🔄 Pulling latest Docker images..." -ForegroundColor Yellow
try {
    docker compose pull
    Write-Host "✅ Images pulled successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to pull Docker images. Exiting." -ForegroundColor Red
    exit 1
}

# Start containers in detached mode
Write-Host "`n🚀 Starting Docker containers..." -ForegroundColor Yellow
try {
    docker compose up -d
    Write-Host "✅ Containers started successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to start containers. Exiting." -ForegroundColor Red
    exit 1
}

# Wait for container to start
Write-Host "`n⏳ Waiting for container to fully start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Check container status
Write-Host "`n📊 Checking container status..." -ForegroundColor Yellow
docker compose ps

# Show logs
Write-Host "`n📋 Recent container logs:" -ForegroundColor Yellow
docker compose logs --tail=10

Write-Host "`n" + "=" * 40 -ForegroundColor Cyan
Write-Host "🎉 Docker reset complete!" -ForegroundColor Green
Write-Host "🌐 Your site should be available at: http://localhost:8080" -ForegroundColor Cyan
Write-Host "📝 To view live logs: docker compose logs -f" -ForegroundColor Yellow
Write-Host "🛑 To stop containers: docker compose down" -ForegroundColor Yellow
