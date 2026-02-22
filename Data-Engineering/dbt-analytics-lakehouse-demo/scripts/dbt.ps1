param(
    [string]$Target = "dev",
    [switch]$FullRefresh
)

# Get project root (one level up from scripts folder)
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$AnalyticsPath = Join-Path $ProjectRoot "analytics"

# Set dbt environment variables (session-only)
$env:DBT_TARGET = $Target
$env:DBT_PROFILES_DIR = $AnalyticsPath

Write-Host "---------------------------------------------"
Write-Host "Running dbt"
Write-Host "Target: $Target"
Write-Host "Profiles Dir: $AnalyticsPath"
Write-Host "---------------------------------------------"

Push-Location $AnalyticsPath

# Install dependencies
dbt deps

# Seed
if ($FullRefresh) {
    dbt seed --full-refresh
} else {
    dbt seed
}

# Build (models + tests)
if ($FullRefresh) {
    dbt build --full-refresh --fail-fast
} else {
    dbt build --fail-fast
}

Pop-Location
