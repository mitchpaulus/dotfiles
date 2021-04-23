# Antlr


- Forcing Java classes to be built:
```
antlr4 -Dlanguage=Java *.g4
javac *.java
```

```sh
antlr4() {
    java -jar /usr/local/lib/antlr-4.x-complete.jar
}
```

```
grun() {
    java org.antlr.v4.runtime.misc.TestRig
}
```

Run grun like:
```
grun GrammarName rule options..
```

- Add visitor classes `-visitor` CLI option


## Installing the Java Development Kit for WSL on Windows OS

- Used Open Source version from [https://jdk.java.net/14/](https://jdk.java.net/14/)
- Extract to desired directory
    - Installed to /usr/java/jdk-14.0.2/
    - Added `/usr/java/jdk-14.0.2/bin` to `PATH`

Followed instructions for Antlr


## C\#

- Best directions for getting the required runtime is on the [downloads page](https://www.antlr.org/download.html).
  There they specify that you need the `Antlr4.Runtime.Standard`
  package.


## Arch/Manjaro

- Believe I used package `jdk-openjdk`
