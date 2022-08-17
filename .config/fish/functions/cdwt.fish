function cdwt
    # Change Directory: Windows Terminal
    set LOCALAPPDATA (wslpath -u (winenv LOCALAPPDATA))

    set WT_DIR $LOCALAPPDATA/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/

    cd $WT_DIR
end
