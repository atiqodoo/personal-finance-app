# Quick commit script
# Usage: .\quick-commit.ps1 "Your commit message"

param(
    [string]$Message = "Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
)

Write-Host "🚀 Quick Git Commit..." -ForegroundColor Green
Write-Host "📝 Message: $Message" -ForegroundColor Yellow

git add .
git commit -m "$Message"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Commit successful!" -ForegroundColor Green
    
    $push = Read-Host "Push to remote? (y/n)"
    if ($push -eq 'y' -or $push -eq 'Y') {
        git push
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Pushed to remote successfully!" -ForegroundColor Green
        }
    }
} else {
    Write-Host "❌ Commit failed" -ForegroundColor Red
}
