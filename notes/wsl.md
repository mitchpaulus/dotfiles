# Upgrading to WSL 2

- They have backported to 1909, however, need to be on minor build
  number 1049 or greater. As of Sunday 2020-09-06, was on 1016.

- This has caused issues since I upgraded to Ubuntu 20.04, because I'm
  still stuck on WSL1. There is an issue with the `nanosleep` system
  call that breaks libc6.
  [https://discourse.ubuntu.com/t/ubuntu-20-04-and-wsl-1/15291](https://discourse.ubuntu.com/t/ubuntu-20-04-and-wsl-1/15291).


## Time issues

There have been issues regarding the clock in WSL2. Running the command

`sudo hwclock -s` based on this post seems to generally fix this issue.

`https://github.com/microsoft/WSL/issues/4245#issuecomment-510238198`


## Internet issues with WSL 2

Cisco Anyconnect and WSL2 do not play well with each other. See GitHub
issue: https://github.com/microsoft/WSL/issues/4277.

Internet seems to work as long as WSL2 is started *before* the VPN is
started. Got that hint from:

https://askubuntu.com/a/1264985

Here's a related YouTube video?
https://www.youtube.com/watch?v=yR2NsssY7z8

## File Permissions

There are two important blog posts discussing files and file
permissions within WSL.

[chmod and chown improvements Jan 12, 2018](https://devblogs.microsoft.com/commandline/chmod-chown-wsl-improvements/)
[automatically configuring WSL Feb 7, 2018](https://devblogs.microsoft.com/commandline/automatically-configuring-wsl/)

After manually adding `metadata` to my D: drive, this was the output of
`mount -l`. Recording this in case I want to force drives to what was
the previous default.

```
C:\ on /mnt/c type drvfs (rw,noatime,uid=1000,gid=1000,case=off)
D: on /mnt/d type drvfs (rw,relatime,metadata,case=off)
```
