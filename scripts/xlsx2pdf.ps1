param (
    [string]$InputPath,      # Full path to the input Excel file
    [string]$WorksheetName   # Name of the worksheet to export (optional)
)

$ExitCode = 0

# Create an Excel application object
$Excel = New-Object -ComObject Excel.Application
$Excel.Visible = $true  # Run Excel in the background
$Excel.DisplayAlerts = $false  # Disable alerts

[Console]::Error.Write("Exporting $InputPath`n")

try {
    # Open the workbook
    $FullPath = (Resolve-Path $InputPath).Path

    # Get TMP directory, save to %TMP%/xlsx.pdf
    $TmpPath = $env:TMP
    $OutputPath = [System.IO.Path]::Combine($TmpPath, "xlsx.pdf")

    $Workbook = $Excel.Workbooks.Open($FullPath)

    # Wait for the workbook to load, sleep 1 second until $Workbook.Worksheets.Count > 0
    # Timing matters for COM.
    while ($Workbook.Worksheets.Count -eq 0) {
        Start-Sleep -Seconds 1
    }
    
    # Get the worksheet to export
    if ($WorksheetName) {
        $Worksheet = $Workbook.Sheets | Where-Object { $_.Name -eq $WorksheetName }
        if (-not $Worksheet) {
            $msg = "Worksheet '$WorksheetName' not found in the workbook. Possible sheets include:"
            $msg += $Workbook.Sheets | ForEach-Object { " $($_.Name)" }
            throw $msg
        }
    } else {
        # Default to the first worksheet if no name is provided
        $Worksheet = $Workbook.Sheets.Item(1)
    }
    
    # Export the worksheet to PDF
    # Params:
    # 1. Type
    # 2. Output file path
    # 3. Quality XlFixedFormatQuality, 0 Standard, 1 Minimum
    # 4. IncludeDocProperties T/F
    # 5. IgnorePrintAreas T/F
    # 6. From
    # 7. To
    # 8. OpenAfterPublish T/F
    # 9. FixedFormatExtClassPtr
    $Worksheet.ExportAsFixedFormat([Microsoft.Office.Interop.Excel.XlFixedFormatType]::xlTypePDF, $OutputPath, 0, $true, $false, [Type]::Missing, [Type]::Missing, $false, [Type]::Missing)
    [Console]::Error.Write("PDF export successful: $OutputPath`n")
} catch {
    Write-Error "An error occurred: $_"
    $ExitCode = 1
} finally {
    # Clean up
    if ($Workbook) {
        $Workbook.Close($false)
    }
    $Excel.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($Excel) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
    exit $ExitCode
}
