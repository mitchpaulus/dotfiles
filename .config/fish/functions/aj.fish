# Compile Antlr grammar using 'J'ava

function aj
    antlr4 -Dlanguage=Java *.g4
    javac *.java
end
