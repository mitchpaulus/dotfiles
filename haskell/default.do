redo-ifchange "$2".hs
ghc -o "$3" "$2".hs >&2
