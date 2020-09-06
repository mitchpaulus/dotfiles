# Upgrading to WSL 2

- They have backported to 1909, however, need to be on minor build
  number 1049 or greater. As of Sunday 2020-09-06, was on 1016.

- This has caused issues since I upgraded to Ubuntu 20.04, because I'm
  still stuck on WSL1. There is an issue with the `nanosleep` system
  call that breaks libc6.
  [https://discourse.ubuntu.com/t/ubuntu-20-04-and-wsl-1/15291](https://discourse.ubuntu.com/t/ubuntu-20-04-and-wsl-1/15291).

