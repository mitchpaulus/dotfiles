# Nix

References:

- [Nix from the Ground Up](https://www.zombiezen.com/blog/2021/12/nix-from-the-ground-up/)
- [Nix dev](https://nix.dev/)

## Installation

Using fish shell and WSL2.

First did:

```sh
curl -L https://nixos.org/nix/install > install.sh
sh install.sh --no-daemon
```

The installation requirements then say to source the file
`~/.nix-profile/etc/profile.d/nix.sh` in your shell.

Unfortunately, this expects to be running a POSIX-like shell like bash.
I still want to use fish.
So I rewrote that shell script as a fish function.

## Haskell

packages:
  - ghc
  - cabal-install
