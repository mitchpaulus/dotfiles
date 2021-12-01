function docx2pdf --description 'Convert .docx file to .pdf'
    OfficeToPDF.exe '/bookmarks' '/readonly' '/noquit' '/working_dir' 'C:\Users\mpaulus\tmp'  $argv
end
