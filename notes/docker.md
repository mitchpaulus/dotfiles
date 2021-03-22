# Docker

## Installation

On Arch, installed the `docker` package.

Then had to follow [post installation steps
here.](https://docs.docker.com/engine/install/linux-postinstall/).
`docker` group had already been added.

Had to enable and start the `docker.service` and `containerd.service`.


## Common Commands

- List running containers: `docker ps`
- Stop container: `docker container stop <container>`
    - `<container>` can be the hash value
    - Can also neglect the `container` command portion and just use
      `docker stop`?

- List all images: `docker image ls`
- Login - `docker login -u mitchpaulus`
    - Credential storage by default at $HOME/.docker/config.json
    - See [here](https://docs.docker.com/engine/reference/commandline/login/#credentials-store)


