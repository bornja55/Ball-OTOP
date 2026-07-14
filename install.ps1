# install.ps1 - Ball-OTOP Skill Installer
# Copies all skills from Ball-OTOP to ~/.claude/skills/
# Usage: powershell -ExecutionPolicy Bypass -File ".\install.ps1"

$target     = Join-Path $env:USERPROFILE ".claude\skills"
$skillsRoot = Join-Path $PSScriptRoot "skills"

New-Item -ItemType Directory -Force -Path $target | Out-Null

$count = 0
foreach ($cat in Get-ChildItem -Path $skillsRoot -Directory) {
    foreach ($skill in Get-ChildItem -Path $cat.FullName -Directory) {
        $dest = Join-Path $target $skill.Name
        New-Item -ItemType Directory -Force -Path $dest | Out-Null
        robocopy $skill.FullName $dest /E /NFL /NDL /NJH /NJS /NC /NS | Out-Null
        Write-Host ("  OK  " + $cat.Name + "/" + $skill.Name) -ForegroundColor Green
        $count++
    }
}

Write-Host ""
Write-Host ("Done: " + $count + " skills installed to ~/.claude/skills/") -ForegroundColor Green
Write-Host "Restart Claude Code / Cowork to load them." -ForegroundColor Yellow
Read-Host "`nPress Enter to close"
