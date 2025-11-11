<#
Load previously saved Docker images and bring up the offline compose stack.

Usage (offline machine):
  ./scripts/load-images.ps1 -ImagesDir .\offline_images

This script will:
  - load any tar files in ImagesDir into the local Docker engine
  - run `docker compose -f docker-compose.offline.yml up -d`
#>

param(
    [string]$ImagesDir = "./offline_images"
)

if (-not (Test-Path $ImagesDir)) {
    Write-Error "Images directory '$ImagesDir' not found. Place the tar files exported from the online machine here.";
    exit 1
}

$tars = Get-ChildItem -Path $ImagesDir -Filter "*.tar" -File
if ($tars.Count -eq 0) {
    Write-Error "No tar files found in $ImagesDir";
    exit 1
}

foreach ($t in $tars) {
    Write-Host "Loading $($t.FullName) ..."
    docker load -i $t.FullName
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to load $($t.FullName)";
        exit 1
    }
}

Write-Host "Starting offline compose stack..."
docker compose -f docker-compose.offline.yml up -d
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to start compose stack";
    exit 1
}

Write-Host "Offline stack started. Site should be at http://localhost:8080" -ForegroundColor Green
