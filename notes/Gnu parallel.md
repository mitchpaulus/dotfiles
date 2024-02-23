```
parallel [options] [command [arguments]] < list_of_arguments
parallel [options] [command [arguments]] ( ::: arguments | :::+ arguments | :::: argfile(s) | ::::+ argfile(s) ) ...

{}: Full input line
{.}: Input line without extension
{/}: Basename (Filename without dir)
{//}: Directory name
{/.}: Basename without extension

--colsep: Column separator, then can use {1} {2} {3} ... to refer to each column
--colsep '\t' works

--halt now,fail=1: Stop on first error
--progress
```
