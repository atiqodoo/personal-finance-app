# Git status overview script

Write-Host "📊 Git Repository Overview" -ForegroundColor Green
Write-Host "=" * 30 -ForegroundColor Green
Write-Host ""

Write-Host "📍 Current Branch:" -ForegroundColor Yellow
git branch --show-current

Write-Host ""
Write-Host "📊 Status:" -ForegroundColor Yellow
git status --short

Write-Host ""
Write-Host "📝 Recent Commits:" -ForegroundColor Yellow
git log --oneline -5

Write-Host ""
Write-Host "🔗 Remote URLs:" -ForegroundColor Yellow
git remote -v

Write-Host ""
Write-Host "📁 Repository Info:" -ForegroundColor Yellow
Write-Host "   Files tracked: $(git ls-files | Measure-Object | Select-Object -ExpandProperty Count)"
Write-Host "   Total commits: $(git rev-list --count HEAD 2>$null)"
Write-Host "   Repository size: $((Get-ChildItem -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB) MB"
