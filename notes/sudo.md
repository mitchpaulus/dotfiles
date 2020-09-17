# Adding yourself to the sudoers file

- Prefer to add file to the `/etc/sudoers.d` directory instead of
  modifying the main file.
- Like using this command: `echo "username  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/username`
- Reference: [https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/](https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/)

