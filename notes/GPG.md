# GPG

- Gnu Privacy Guard. Uses techniques from the Open Pretty Good Privacy Standard (OpenPGP)

- Revocation Certificate more important than expiry ([Source](https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security))
- [Sharing key across devices][]

```
gpg -a --export-secret-key
gpg --import
```

- [Digital Ocean Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages)

[Sharing key across devices]: https://security.stackexchange.com/questions/44470/what-is-the-best-way-to-manage-gpg-keys-across-multiple-devices
