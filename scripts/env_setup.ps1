# Check if pip is installed
if (!(Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "pip could not be found. Please install pip first."
    exit 1
}

# Install dependencies
Write-Host "Installing required Python dependencies..."
pip install shutil requests subprocess

Write-Host "Python dependencies installed successfully."
exit 0
