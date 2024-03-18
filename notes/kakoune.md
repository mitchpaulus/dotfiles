<https://www.reddit.com/r/kakoune/comments/grlu0s/kakrc_config_for_begginers/>

# Normal mode:

See `normal.cc` in code.

a: enter insert mode after each selection
b: select preceding whitespaces and the word on the left of selection end
c: yank and delete each selection and enter insert mode
d: yank and delete each selection
e: select preceding whitespaces and the word on the right of selection end
f: select to (including) the next occurrence of the given character
g: GOTO commands
h: select the character on the left of selection end
i: enter insert mode before each selection
j: select the character below the selection end
k: select the character below the selection end
l: select the character on the right of selection end
m: select to matching character
n: select next match
o: enter insert mode in one (or given count) new lines below each selection end
p: paste after each selection end
q: play a recorded macro
s: create a selection for each match of the given regex (selects the count capture if it is given)
t: select until (excluding) the next occurrence of the given character
u: undo last change
v: VIEW commands
w: select the word and following whitespaces on the right of selection end
x: expand selections to contain full lines (including end-of-lines)
y: yank selections
z: restore selections from the register

A: enter insert mode at each selection end line end
B: Extend 'b' left.
C: Duplicate selections on the lines that follow them
D: NOP
E: Extend 'e' right.
F: Extend selection to the next occurrence of the given character exclusive (extending 'f')
G: Extend GOTO commands
H: Extend 'h' left.
I: enter insert mode at each selection start line start
J: Extend 'j' down.
K: Extend 'k' up.
L: Extend 'l' right.
M: Extend the current selection to the next sequence enclosed by matching
N: add a new selection with next match after the main selection
O: enter insert mode in a new line (or in a given `count` of new lines)
P: Paste before the beginning of each selection
Q: Start or end macro recording
R: Replace selections with yanked text
S: Split selections with the given regex
T: Extend selection to the next occurrence of the given character inclusive (extending 't')
U: Redo last change
V: Lock view mode
W: Extend 'w' right.
X: NOP?
Y: NOP?
Z: Save selections to the register


%: select whole buffer
;: reduce selections to their cursor
,: clear selections, select the last selection

ALT + a: enter outer text object selection mode
ALT + c: delete selections and enter insert mode (not yanking)
ALT + i: enter inner text object selection mode
ALT + .: repeat last object or f/t selection command.

## Regex

```
(?i) # case insensitive
```

## Scopes:

- global, buffer, window

## Mapping

```
map [-docstring 'doc string'] <scope> <mode> <key> <keys>
<scope> = global | buffer | window
<mode> = insert | normal | prompt | user | goto | view | object
```

## Highlighters

```
add-highlighter [-override] <scope>/[path]/[name] <type> <parameters>..
<scope> = global | buffer | window | shared
```

## Debugging

echo -debug "message" is your friend.
Look at "*debug*" buffer.

## References

<https://blog.trinket.icu/articles/writing-your-first-kakrc>
<https://zork.net/~st/jottings/Intro_to_Kakoune_highlighters.html>
