# New-Item -ItemType Directory -Path (Split-Path $PROFILE) -Force
# New-Item -ItemType File -Path $PROFILE -Force
# notepad $PROFILE
# Microsoft.PowerShell_profile.ps1

function Andover2EBO {
    param (
        [string]$InputText
    )

    $result = $InputText -creplace "([a-z])\.([A-Z])", '$1$2'
    $result = $result -replace "([A-z])\.([0-9])", '$1$2'
    $result = $result -replace "\.", '_'
    return $result
}

Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle InlineView
Set-PSReadLineOption -EditMode Emacs

Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward
