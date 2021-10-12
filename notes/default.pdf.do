markdown_file="$2".md
redo-ifchange "$2".md

pandoc -o "$3" --to pdf --pdf-engine=lualatex "$markdown_file"
