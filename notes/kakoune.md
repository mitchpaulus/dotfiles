<https://www.reddit.com/r/kakoune/comments/grlu0s/kakrc_config_for_begginers/>

# Normal mode:

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
z: ??

## Regex

```
(?i) # case insensitive
```
