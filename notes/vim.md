# Vim

## Mapping Ctrl-Space or Ctrl-@/Finding what key sequence Vim receives

I found this great tip from [here](https://www.reddit.com/r/vim/comments/dn7dtb/how_to_rebind_ctrlspace_in_vim_running_inside/).
To find what sequence Vim is receiving, can use CTRL-V, then sequence,
and see what Vim prints. This helped me find that Vim received Ctrl -
Space as `<C-Space>`, not `<C-@>` as I had expected.


