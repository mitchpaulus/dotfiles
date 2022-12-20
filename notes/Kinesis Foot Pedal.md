# Kinesis SE2 Foot Pedal

Configuration is simple text file, found at:

```
active/pedals.txt
```

in the hard disk memory.

Comments start with `*` character

Otherwise, main configuration looks like:

```
{lpedal}>{-win}{4}{+win}
{mpedal}>{-win}{2}{+win}
[rpedal]>[enter]
[jack1]>[lmouse]
[jack2]>[rmouse]
[jack3]>[bspace]
{jack4}>{-shift}{t}{+shift}{h}{a}{n}{k}{space}{y}{o}{u}{,}
```

If you don't want a key to repeat, then you need to make it a "macro".
Macros are defined using the `{` instead of the `[`.
