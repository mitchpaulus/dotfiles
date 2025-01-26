```go
package main

import (
  "testing"
)

func TestFunction(t *testing.T) {
  // code
}

/*
A test function is one named TestXxx (where Xxx does not start with a
lower case letter) and should have the signature,

	func TestXxx(t *testing.T) { ... }

A benchmark function is one named BenchmarkXxx and should have the signature,

	func BenchmarkXxx(b *testing.B) { ... }

A fuzz test is one named FuzzXxx and should have the signature,

	func FuzzXxx(f *testing.F) { ... }
*/
```
