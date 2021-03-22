# npm

List all globally installed packages: `npm list -g`

Without any sub-dependencies: `npm list -g --depth=0`

Uninstall global package: `npm uninstall -g <package>`

Before updating on Arch - make sure it wasn't installed through the
package manager. If installed through the package manager, let `pacman` be
the one to do the updating.
