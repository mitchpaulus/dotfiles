# Getting Started

What worked for me: <https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux>

```sh
# Ubuntu
sudo apt install libasound2-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev libxcursor-dev libxinerama-dev libwayland-dev libxkbcommon-dev
git clone --depth 1 https://github.com/raysan5/raylib.git raylib
cd raylib/src/
make PLATFORM=PLATFORM_DESKTOP # To make the static version.
make PLATFORM=PLATFORM_DESKTOP RAYLIB_LIBTYPE=SHARED # To make the dynamic shared version.

sudo make install # Static version.
sudo make install RAYLIB_LIBTYPE=SHARED # Dynamic shared version.

sudo make uninstall
sudo make uninstall RAYLIB_LIBTYPE=SHARED

```
