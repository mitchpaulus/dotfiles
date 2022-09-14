# `join` program design

The POSIX `join` command just isn't good enough for me.
The defaults don't make sense for the data that I normally work with.

Here are my design thoughts on making my own command line join utility.

Default values:

1. Assume Tab separated
2. Assume no headers
3. Assume both files are *unsorted*
4. Default to inner join

Required configuration

1. Key column selection for both files.
2. Delimiter
3. Inner, outer, left, or right join
