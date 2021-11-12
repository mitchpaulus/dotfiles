# View Note

function vn --description="view note"
    set note (select_note)

    if test "$status" -ne 0
        return $status
    end

    set pdfname "$MPNOTES/$note.pdf"
    redo-ifchange "$pdfname"

    if test -f "$pdfname"
        if  test -n "$WSL_DISTRO_NAME"; and command -q wsl-opener
            wsl-opener "$pdfname"
        else
            xdg-open "$pdfname" > /dev/null 2> /dev/null
        end
        # pandoc --pdf-engine=lualatex -o "$pdfname" "$MPNOTES/$note.md"
    end
end
