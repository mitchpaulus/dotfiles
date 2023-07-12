complete -c CCLLCParser -s p -x -a "alamo_welcome_center_csv ccllc fid_abq_bas fid_wlk fid_wlk_html icon metasys_export_tool meterlogic multi_sheet_excel simple_csv simple_tsv"
complete -c CCLLCParser -s t -l trends -d 'Print summary of available trends rather than parse'
complete -c CCLLCParser -l csv -d 'Print to CSV format instead of CCLLC'
complete -c CCLLCParser -s c -l count -d 'Also show data point count with trend summary'
complete -c CCLLCParser -l dates -d 'Print date summary for files'
complete -c CCLLCParser -l fish -d 'Print code for fish completions'
complete -c CCLLCParser -s h -l help -d 'Print help'
