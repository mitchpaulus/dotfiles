package main

import (
	"os"
	"os/exec"
)

func main() {
    if len(os.Args) < 4 {
		os.Stderr.WriteString("Usage: lf-preview-win.exe <path> <width> <height>\n")
        os.Exit(1)
    }

	dotfiles, ok := os.LookupEnv("DOTFILES")
	if !ok {
		os.Stderr.WriteString("Error: DOTFILES environment variable not set\n")
		os.Exit(1)
	}

    // Base args you always want:
    args := []string{ dotfiles + "\\scripts\\lf-preview-win.msh" }

    // Append all the
	args = append(args, os.Args[1:]...)

    cmd := exec.Command("msh.exe", args...)
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr

	err := cmd.Run()

	if err != nil {
		os.Stderr.WriteString("Error: " + err.Error() + "\n")
		os.Exit(1)
	}
}
