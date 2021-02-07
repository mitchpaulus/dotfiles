# Vim

## Mapping Ctrl-Space or Ctrl-@/Finding what key sequence Vim receives

I found this great tip from [here](https://www.reddit.com/r/vim/comments/dn7dtb/how_to_rebind_ctrlspace_in_vim_running_inside/).
To find what sequence Vim is receiving, can use CTRL-V, then sequence,
and see what Vim prints. This helped me find that Vim received Ctrl -
Space as `<C-Space>`, not `<C-@>` as I had expected.



## Syntax Highlighting

See `:h group-name` for standard group names like 'Comment' and
'Constant'

See `:h syn-match` for syntax matching. It's in `syntax.txt`

General process is:

1. Match things using `syntax keyword`, `syntax match`, or `syntax
   region`.

2.

## Constantly Reload File for Demo

From [link](https://www.reddit.com/r/vim/comments/ktd2kw/run_a_vim_command_in_loop_each_n_seconds/):

```viml
:call timer_start( 2000, { id -> execute( 'e!' ) }, { 'repeat': -1 } )
```

However, combining it with this function for restoring the cursor
position is even better ([link](https://stackoverflow.com/a/50476532/5932184)):

```viml
:call timer_start( 2000, { id -> execute('let l:winview=winsaveview() | checktime | call winrestview(l:winview) ' ) }, { 'repeat': -1 } )
```

