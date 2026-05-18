#!/usr/bin/env mshell
[wslpath -u -a
    [winenv LOCALAPPDATA] * ; chomp
] * ; chomp localappdata!
['cp' $DOTFILES "/scripts/xlsx2pdf.ps1" + @localappdata "/xlsx2pdf/xlsx2pdf.ps1" +];
