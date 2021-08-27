# Citrix

Getting Citrix to work on Manjaro

1. Downloaded Citrix workspace for Linux, using tarball.
2. Extract in *clean* directory, it has loose files in root
3. Run the setup script.
4. It should associate `.ica` files with a corresponding shell script.
5. It things break because of SSL:
  - I just copied over all the SSL certs that were on my computer,
    cached by Firefox, from the folder `/etc/ssl/certs` to
    `.../ICAClient/linuxx64/keystore/cacerts`, and that seemed to fixed
    the issue.
