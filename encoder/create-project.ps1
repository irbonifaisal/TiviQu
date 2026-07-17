# ============================================
# TiviQu Encoder - Project Skeleton Creator
# ============================================

Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "   TiviQu Encoder Project Generator"
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# ---------- Root Files ----------

$files = @(
    "encoder.py",
    "config.py",
    "requirements.txt",
    "README.md"
)

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "Created file : $file"
    }
}

# ---------- Folder Structure ----------

$folders = @(
    "core",

    "ffmpeg",

    "workspace",

    "workspace\input",
    "workspace\output",
    "workspace\temp",
    "workspace\cache",
    "workspace\logs"
)

foreach ($folder in $folders) {

    if (!(Test-Path $folder)) {

        New-Item -ItemType Directory -Path $folder | Out-Null

        Write-Host "Created folder : $folder"

    }

}

# ---------- Core Modules ----------

$coreFiles = @(
    "__init__.py",
    "scanner.py",
    "validator.py",
    "analyzer.py",
    "thumbnail.py",
    "hls.py",
    "metadata.py",
    "organizer.py",
    "logger.py",
    "utils.py"
)

foreach ($file in $coreFiles) {

    $path = Join-Path "core" $file

    if (!(Test-Path $path)) {

        New-Item -ItemType File -Path $path | Out-Null

        Write-Host "Created file : $path"

    }

}

Write-Host ""
Write-Host "=======================================" -ForegroundColor Green
Write-Host "Project Skeleton Created Successfully!"
Write-Host "=======================================" -ForegroundColor Green