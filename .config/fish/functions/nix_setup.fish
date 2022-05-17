function nix_setup --description 'This is a porting of the file /home/mp/.nix-profile/etc/profile.d/nix.sh to fish'
    if test -n $HOME && test -n $USER
        # Set up the per-user profile.
        # This part should be kept in sync with nixpkgs:nixos/modules/programs/shell.nix
        set NIX_LINK $HOME/.nix-profile

        # Set up environment.
        # This part should be kept in sync with nixpkgs:nixos/modules/programs/environment.nix
        set -gx NIX_PROFILES "/nix/var/nix/profiles/default $HOME/.nix-profile"

        # Set $NIX_SSL_CERT_FILE so that Nixpkgs applications like curl work.
        if test -e /etc/ssl/certs/ca-certificates.crt  # NixOS, Ubuntu, Debian, Gentoo, Arch
            set -gx NIX_SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
        else if [ -e /etc/ssl/ca-bundle.pem ] # openSUSE Tumbleweed
            set -gx NIX_SSL_CERT_FILE /etc/ssl/ca-bundle.pem
        else if [ -e /etc/ssl/certs/ca-bundle.crt ] # Old NixOS
            set -gx NIX_SSL_CERT_FILE /etc/ssl/certs/ca-bundle.crt
        else if [ -e /etc/pki/tls/certs/ca-bundle.crt ] # Fedora, CentOS
            set -gx NIX_SSL_CERT_FILE /etc/pki/tls/certs/ca-bundle.crt
        else if [ -e "$NIX_LINK/etc/ssl/certs/ca-bundle.crt" ] # fall back to cacert in Nix profile
            set -gx NIX_SSL_CERT_FILE "$NIX_LINK/etc/ssl/certs/ca-bundle.crt"
        else if [ -e "$NIX_LINK/etc/ca-bundle.crt" ] # old cacert in Nix profile
            set -gx NIX_SSL_CERT_FILE "$NIX_LINK/etc/ca-bundle.crt"
        end

        # Only use MANPATH if it is already set. In general `man` will just simply
        # pick up `.nix-profile/share/man` because is it close to `.nix-profile/bin`
        # which is in the $PATH. For more info, run `manpath -d`.
        if test -n "$MANPATH"
            set -gx MANPATH "$NIX_LINK/share/man:$MANPATH"
        end

        path_prepend $NIX_LINK/bin
    end
end
