complete -c 'subtask_upload.py' -s h -l help -d 'Show help message'
complete -c 'subtask_upload.py' -l report
complete -c 'subtask_upload.py' -l systems-manual
complete -c 'subtask_upload.py' -d 'Project Id' -s p -x
complete -c 'subtask_upload.py' -x -d "Project Drivers" -a "(subtask_upload.py drivers)"
