param(
    [string]$venvPath = "./.venv",
    [string]$pythonExe = "python"
)

Write-Host "Creating virtual environment at $venvPath using $pythonExe"

if (-not (Get-Command $pythonExe -ErrorAction SilentlyContinue)) {
    Write-Error "Python executable '$pythonExe' not found in PATH. Please install Python or provide full path via -pythonExe"
    exit 1
}

python -m venv $venvPath

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to create venv"
    exit $LASTEXITCODE
}

$activate = Join-Path $venvPath "Scripts\Activate.ps1"
if (Test-Path $activate) {
    Write-Host "To activate the venv run:"
    Write-Host "    & '$activate'"
}
else {
    Write-Warning "Activation script not found at $activate. Venv might not have been created correctly."
}

Write-Host "Installing requirements.txt if present..."
$req = Join-Path (Get-Location) "requirements.txt"
if (Test-Path $req) {
    & "$venvPath\Scripts\python.exe" -m pip install --upgrade pip
    & "$venvPath\Scripts\python.exe" -m pip install -r $req
}

Write-Host "Done."
