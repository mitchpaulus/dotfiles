# Go

## Install

```sh
# https://go.dev/doc/install
# Download latest: https://go.dev/dl/
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.22.1.linux-amd64.tar.gz
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
```
