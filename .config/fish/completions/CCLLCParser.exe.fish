complete -c CCLLCParser.exe -s p -x -a "ccllc fid_abq_bas fid_wlk fid_wlk_html icon metasys_export_tool meterlogic simple_csv"
complete -c CCLLCParser.exe -s t -l trends -d 'Print summary of available trends rather than parse'
complete -c CCLLCParser.exe -l csv -d 'Print to CSV format instead of CCLLC'
complete -c CCLLCParser.exe -s c -l count -d 'Also show data point count with trend summary'
complete -c CCLLCParser.exe -l dates -d 'Print date summary for files'
complete -c CCLLCParser.exe -l fish -d 'Print code for fish completions'
complete -c CCLLCParser.exe -s h -l help -d 'Print help'
