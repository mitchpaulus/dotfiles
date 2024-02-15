# Antlr

## Installation

Download from link at <www.antlr.org>, Complete ANTLR x.x.x java binaries jar.
Single JAR file. Put in `/usr/local/lib/`. Dotfiles will search for that dir.


- Forcing Java classes to be built:
```
antlr4 -Dlanguage=Java *.g4
javac *.java
```

```sh
antlr4() {
    java -jar /usr/local/lib/antlr-4.x-complete.jar "$@"
}
```

```sh
grun() {
    java org.antlr.v4.runtime.misc.TestRig "$@"
}
```

Run `grun` like:
```sh
grun GrammarName rule [-tree] [-tokens] ..
```

Make sure the java classes have been compiled.

- Add visitor classes `-visitor` CLI option

## Installing the Java Development Kit for WSL on Windows OS

- Used Open Source version from <https://jdk.java.net>
- Extract to desired directory
    - Installed to `/usr/java/jdk-14.0.2/`
    - Added `/usr/java/jdk-14.0.2/bin` to `PATH`
    - Dotfiles also now search for `~/.local/jdk-XX.X.X/`


Followed instructions for Antlr


## C\#

- Best directions for getting the required runtime is on the [downloads page](https://www.antlr.org/download.html).
  There they specify that you need the `Antlr4.Runtime.Standard` package from NuGet.

  ```sh
  dotnet add package 'Antlr4.Runtime.Standard'
  ```

- The language name for the grammar file or on the command line is:
  `CSharp`

  ```
  -Dlanguage CSharp
  # or
  options {
    language = CSharp
  }
  ```


## Arch/Manjaro

- Believe I used package `jdk-openjdk`

## Associativity

The location of the `<assoc=right/left>` token has moved from the time of
the book. It now gets put right at the beginning of the alternative,
rather than after the binary operator. It only seems to affect the
binary case, not the prefix or suffix.

[Note on left recursion](https://github.com/antlr/antlr4/blob/master/doc/left-recursion.md)

[Technical Paper with Details](https://www.antlr.org/papers/allstar-techreport.pdf)

 - Binary expressions are expressions which contain a recursive
   invocation of the rule as the first and last element of the
   alternative.
 - Suffix expressions contain a recursive invocation of the rule as the
   first element of the alternative, but not as the last element.
 - Prefix expressions contain a recursive invocation of the rule as the
   last element of the alternative, but not as the first element.

## Lexing/Parsing Examples

```C#
ANTLRInputStream inputStream = new ANTLRInputStream(Stream stream);
// or
ANTLRInputStream inputStream = new ANTLRInputStream(string contents);


NameLexer lexer = new NameLexer(inputStream);

CommonTokenStream tokens = new CommonTokenStream(lexer);

NameParser parser = new NameParser(tokens);

var tree = parser.rule();

MyListener listener = new MyListener();
ParseTreeWalker walker = new Walker();
walker.Walk(listener, tree)
```

## Matching Strings

```antlr
// See pg. 78 of Definitive ANTLR Reference.
STRING : '"' (ESC|.)*? '"' ;
fragment ESC : '\\"'  | '\\\\' ;
```

## Recursive Lexing for Tokens

[Great example](https://stackoverflow.com/questions/2555818/).

## `ClassCastException` on split parser and lexer grammars

- [GitHub issue](https://github.com/antlr/antlr4/issues/859)

When running `grun`, if you have split lexer/parser like GrammarParser.g4 and GrammarLexer.g4,
you still run `grun` *without* the `Parser` or `Lexer` text.

Like:

```
grun Grammar entryRule
```


## Error Handlers

```C#
lexer.RemoveErrorListeners()
parser.RemoveErrorListeners()
```

## Additional code in lexers/parsers

```
@lexer::members {
   // code in target language...
}
@parser::members {
  //
}
```

## Test Rig Code

Once you have some semantic predicates or other member code that isn't in the Java language,
you might have to incorporate the `grun` testing features into whatever target language you're working on.
The code for the `grun` TestRig is at: `tool/src/org/antlr4/v4/gui/TestRig.java`.

Showing tokens (`--tokens`):

```java
if ( showTokens ) {
  for (Token tok : tokens.getTokens()) {
    if ( tok instanceof CommonToken ) {
      System.out.println(((CommonToken)tok).toString(lexer));
    }
    else {
      System.out.println(tok.toString());
    }
  }
}
...

if ( printTree ) {
  System.out.println(tree.toStringTree(parser));
}
if ( gui ) {
  Trees.inspect(tree, parser);
}
if ( psFile!=null ) {
  Trees.save(tree, parser, psFile); // Generate postscript
}
```

## Token `toString`

From `runtime/Java/src/org/antlr/v4/runtime/CommonToken.java`

```java
public String toString(Recognizer r) {

  String channelStr = "";
  if ( channel>0 ) {
    channelStr=",channel="+channel;
  }
  String txt = getText();
  if ( txt!=null ) {
    txt = txt.replace("\n","\\n");
    txt = txt.replace("\r","\\r");
    txt = txt.replace("\t","\\t");
  }
  else {
    txt = "<no text>";
  }
  String typeString = String.valueOf(type);
  if ( r!=null ) {
    typeString = r.getVocabulary().getDisplayName(type);
  }
  return "[@"+getTokenIndex()+","+start+":"+stop+"='"+txt+"',<"+typeString+">"+channelStr+","+line+":"+getCharPositionInLine()+"]";
}
```

## CLS Warnings

Can remove with a file called `AssemblyInfo.cs` (Don't think it actually matters what the name is):

```C#
// This is to remove Antlr compiler warnings.
// References:
//https://github.com/tunnelvisionlabs/antlr4cs/issues/10#issuecomment-66999851

[assembly: CLSCompliant(false)]
```

## Rewriting Token Stream

See pg. 54 in "Cool Lexical Features" section
See pg. 208 For example of accessing hidden channels in the rewriting.
