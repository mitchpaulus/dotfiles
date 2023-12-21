```
parallel [options] [command [arguments]] < list_of_arguments
parallel [options] [command [arguments]] ( ::: arguments | :::+ arguments | :::: argfile(s) | ::::+ argfile(s) ) ...

{}: Full input line
{.}: Input line without extension
{/}: Basename (Filename without dir)
{//}: Directory name
{/.}: Basename without extension
```
