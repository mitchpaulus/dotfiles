function cdwt
    # Change Directory: Windows Terminal
    set LOCALAPPDATA (wslpath -u (winenv LOCALAPPDATA))

    set WT_DIR $LOCALAPPDATA/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/

    if test -d $WT_DIR
        cd $WT_DIR
    else
        set WT_DIR $LOCALAPPDATA/Packages/Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe/LocalState/

        if test -d $WT_DIR
            cd $WT_DIR
        else
            printf 'Could not find Windows Terminal directory.\n' >&2
        end
    end

end
