# Adding yourself to the sudoers file

- Prefer to add file to the `/etc/sudoers.d` directory instead of
  modifying the main file.
- Like using this command: `echo "username  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/username`
- Made fish function `add2sudoers` to automatically add this
- Reference: [https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/](https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/)

## Sudoers file format

```
file : (alias | user_spec)* ;

alias
  : 'User_Alias' user_alias (':' user_alias)*
  | 'Runas_Alias' runas_alias (':' runas_alias)*
  | 'Host_Alias' host_alias (':' host_alias)*
  | 'Cmnd_Alias' cmnd_alias (':' cmnd_alias)*
  ;

user_alias : NAME '=' USER_LIST ;

user_list : user | user ',' user_list ;

user : '!'* (
     user_name
   | #uid
   | %group
   | %#groupid
   | +netgroup
   | %:+nonunix_group
   | %:#nonunix_groupid
   | user_alias
   ;

user_spec : user_list host_list '=' cmnd_spec_list (':' host_list '=' cmnd_spec_list)* ;
```
