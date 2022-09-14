# SSH

- Public Key: On server
- Private Key: Local
- Private key should be read-only to owner: `chmod 400`

1. Generate private/public key pair on local computer. Stores default
   keys at `id_rsa` and `id_rsa.pub`

```
ssh-keygen -t rsa -b 4096
```

2. Transfer the public key to the remote computer that you are
   attempting to ssh into

```
ssh-copy-id user@host
```

3. Modify `~/.ssh/config`

Can do things like:

```
Host psy
    User root
    Hostname 192.168.0.0
    IdentityFile path/to/file.pem
```

## GitHub

1. Add public key via website
2. `ssh -T git@github.com`
3. Accept fingerprint
4. May have to change remote: `git remote set-url origin git@github.com:username/your-repository.git`
