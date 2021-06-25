awk '

BEGIN { in_nvim = 0 }

/NVIM START/ { in_nvim = 1 }

!in_nvim { print }

/NVIM END/ { in_nvim = 0 }

' ../.config/nvim/init.vim
