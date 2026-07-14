# install.ps1 -- Ball-OTOP Custom Skills Installer
# Copies custom skills from Ball-OTOP into ~/.claude/skills/
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File ".\install.ps1"

$target     = Join-Path $env:USERPROFILE ".claude\skills"
$skillsRoot = Join-Path $PSScriptRoot "skills"

New-Item -ItemType Directory -Force -Path $target | Out-Null

$synced = 0
foreach ($category in Get-ChildItem -Path $skillsRoot -Directory) {
    foreach ($skill in Get-ChildItem -Path $category.FullName -Directory) {
        $dest = Join-Path $target $skill.Name
        New-Item -ItemType Directory -Force -Path $dest | Out-Null
        robocopy $skill.FullName $dest /E /NFL /NDL /NJH /NJS /NC /NS | Out-Null
        Write-Host ("  COPIED  " + $category.Name + "/" + $skill.Name) -ForegroundColor Green
        $synced++
    }
}

Write-Host ""
Write-Host ("Installed " + $synced + " custom skills.") -ForegroundColor Green
Write-Host ""
Write-Host "Install upstream skills (if not yet installed):" -ForegroundColor Cyan
Write-Host "  /plugin marketplace add forrestchang/andrej-karpathy-skills"
Write-Host "  npx skills add thananon/9arm-skills"
Write-Host "  npx skills@latest add mattpocock/skills"
Write-Host "  (After mattpocock: run /setup-matt-pocock-skills once per project)"
Write-Host ""
Write-Host "Restart Claude Code / Cowork to load the new skills." -ForegroundColor Yellow
Read-Host "`nPress Enter to close"
