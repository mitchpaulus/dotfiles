# Adding yourself to the sudoers file

- Prefer to add file to the `/etc/sudoers.d` directory instead of
  modifying the main file.
- Like using this command: `echo "username  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/username`
- Made fish function `add2sudoers` to automatically add this
- Reference: [https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/](https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/)

