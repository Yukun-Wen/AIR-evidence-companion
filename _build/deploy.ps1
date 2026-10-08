# Deploy AIR evidence site to GitHub.
# Run AFTER you have logged in:  gh auth login
# or set $env:GH_TOKEN = "<token>"
$gh = "C:\Program Files\GitHub CLI\gh.exe"
$git = "C:\Program Files\Git\bin\git.exe"
Set-Location $PSScriptRoot\..
# create repo (public) named AIR-evidence-companion, or reuse existing
$repo = & $gh repo view --json nameWithOwner -q .nameWithOwner 2>$null
if(-not $repo){
  $repo = & $gh repo create AIR-evidence-companion --public --source . --push 2>&1
  Write-Host $repo
} else {
  Write-Host "Using existing repo: $repo"
}
# ensure remote + push
$remote = & $git remote get-url origin 2>$null
if(-not $remote){
  & $git remote add origin "https://github.com/$repo.git" 2>$null
}
& $git push -u origin main
Write-Host "Pushed. Enable Pages: gh repo edit $repo --homepage https://$($repo -split '/')[0].github.io/$($repo -split '/')[1] --enable-pages"
