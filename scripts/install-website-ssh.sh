ssh-keygen -t rsa -b 4096
ssh-copy-id root@199.192.25.72
printf "Adding 'psy' as a known host to ~/.ssh/config...\n"
printf "Host psy\n    User root\nHostname 199.192.25.72\n" >> ~/.ssh/config
