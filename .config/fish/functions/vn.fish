# View Note

function vn

    set note (select_note)

    set pdfname "$MPNOTES/$note.pdf"

    if test ! -f "$pdfname"
        pandoc -o "$pdfname" "$MPNOTES/$note.md"
    end

    xdg-open "$pdfname" > /dev/null 2> /dev/null

end
