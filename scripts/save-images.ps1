<#
Save prebuilt Docker images to tar files for offline transfer.

Usage (online machine):
  ./scripts/save-images.ps1 -OutputDir .\offline_images

This script will:
  - build the local image from the repository Dockerfile (tag: local/al-folio:offline)
  - save the resulting image to a tar file in the specified output directory
#>

param(
    [string]$OutputDir = "./offline_images"
)

Write-Host "Preparing output directory: $OutputDir"
if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

Write-Host "Building Docker image local/al-folio:offline from Dockerfile..."
$build = docker build -t local/al-folio:offline .
if ($LASTEXITCODE -ne 0) {
    Write-Error "Docker build failed. Ensure Docker is running and you have network access for base images.";
    exit 1
}

$tarPath = Join-Path -Path $OutputDir -ChildPath "al-folio-offline.tar"
Write-Host "Saving image to $tarPath ..."
docker save local/al-folio:offline -o $tarPath
if ($LASTEXITCODE -ne 0) {
    Write-Error "docker save failed.";
    exit 1
}

Write-Host "Done. Copy the '$OutputDir' folder to the offline machine and run 'scripts/load-images.ps1' there." -ForegroundColor Green
