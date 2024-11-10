# find

`-exec command ;`: Don't forget the ';'.
`-a` and `-o`: And and or logic
`-maxdepth`/`-mindepth`: Levels to descend. 0 is literally just the starting point.
                         So if it is a single, the most it could ever return is 1 result, itself.
`-name` or `-iname`: filename matches shell pattern
`-type`: file type

    - `d`: directory
    - `f`: regular file
    - `l`: symbolic link

`-printf format`: print with formatting
    - Normal escapes like '\n'
    - `%f`: File's name with any leading directories removed (only the last element).
    - `%h`: Leading directories of file's name (all but the last element).  If the file name contains no slashes (since it is in
            the current directory) the %h specifier expands to `.'.
    - `%p`: Full name
    - `%P`: File's name with the name of the starting-point under which it was found removed.
