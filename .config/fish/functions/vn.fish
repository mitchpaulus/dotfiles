# View Note

function vn --description="view note"

    set note (select_note)

    if test "$status" -eq 0
        set pdfname "$MPNOTES/$note.pdf"
        redo-ifchange "$pdfname"
    end

    if test -f "$pdfname"
        xdg-open "$pdfname" > /dev/null 2> /dev/null
        # pandoc --pdf-engine=lualatex -o "$pdfname" "$MPNOTES/$note.md"
    end
end
