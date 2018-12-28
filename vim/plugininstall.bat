IF "%HOME%"=="" (
    ECHO Home variable is not set
    EXIT
)
mkdir %HOME%\vimfiles\pack\mitchplugins\start
cd %HOME%\vimfiles\pack\mitchplugins\start
git clone https://github.com/mitchpaulus/vim-siemens-ppcl.git
git clone https://github.com/mitchpaulus/autocorrect.vim.git
git clone https://github.com/mitchpaulus/vim-tex2text.git
git clone https://github.com/mitchpaulus/latex-plus.git

IF EXIST %HOME%\vimfiles\bundle\Vundle.vim (
        echo "Vundle already exists"
        )
ELSE (
        mkdir %HOME%\vimfiles\bundle
        cd %HOME%\vimfiles\bundle
        git clone https://github.com/VundleVim/Vundle.vim.git
     )
