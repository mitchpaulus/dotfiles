# Go

## Install

```sh
# https://go.dev/doc/install
# Download latest: https://go.dev/dl/
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.22.1.linux-amd64.tar.gz

sudo pacman -S go # Arch Linux/Manjaro
```

## Cross compilation

`GOOS` and `GOARCH` environment variables.

```
env GOOS=windows GOARCH=amd64 go build file.go
```

```
GOOS        GOARCH
android     arm
darwin      386
darwin      amd64
darwin      arm
darwin      arm64
dragonfly   amd64
freebsd     386
freebsd     amd64
freebsd     arm
linux       386
linux       amd64
linux       arm
linux       arm64
linux       ppc64
linux       ppc64le
linux       mips
linux       mipsle
linux       mips64
linux       mips64le
netbsd      386
netbsd      amd64
netbsd      arm
openbsd     386
openbsd     amd64
openbsd     arm
plan9       386
plan9       amd64
solaris     amd64
windows     386
windows     amd64
```

```go
token, exists := os.LookupEnv("TODOIST_TOKEN") // Enviornment variables
import "sort"

people := []Person{
	{"Bob", 31},
	{"Alice", 52},
	{"Eve", 24},
	{"Mallory", 42},
	//...
}

sort.Slice(people, func(i, j int) bool {
	return people[i].Age < people[j].Age
})

var i int
var i, j int // zero initializated

if i < 5 {
..
} else if i < 10 {
..
} else {
..
}

type Person struct {
    Name string
    Age  int
}

func (p Person) String() string {
    return fmt.Sprintf("%s: %d", p.Name, p.Age)
}

// Mon Jan 2 15:04:05 MST 2006


var mySlice []int
var myMap map[string]int // Map from string to int
myMap = map[string]int{"one": 1, "two": 2}

```


# Modules

Package: A collection of source files in the same directory that are compiled together.
Repository: Contains one or more modules.
Module: A collection of related Go packages that are versioned together as a single unit.
Module Path: the import path prefix for all packages within the module.
Import Path: String used to import a package. A package's import path is its module path joined with its subdirectory within the module.
