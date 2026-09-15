---
name: mshell
description: |
  `mshell` is a programming language that is meant to replace usages of traditional shells like bash or programming languages for short scripts like Python.
  It excels at running external processes and having consise syntax for efficient token usage.

---

`mshell` is a concatenative programming language to replace usages of traditional shells like bash or programming languages for short scripts like Python.

When using this skill, please review the documentation thoroughly because you have not been trained on it's usage to date.

You can find documentation in Markdown form in this directory at `mshell.md`.

If you find a pain point during the usage of this skill, you MUST TELL ME SO I CAN FIX IT AND MAKE IT BETTER.
I am in total control of this programming language.

## Anti Patterns

These are anti-patterns that I've seen you, the LLM, do in the past.

- Use `1 nth` instead of `:1:`. The previous forces two evaluations versus 1 and takes 2 extra characters.
- Using "\n" join instead of `unlines`. `unlines` also gives you the final newline, which I want with my files.

## Common Mistakes

You make this mistake nearly EVERY time. Please note in your response that you read and comprehend this.
For storing multiple variables using the comma operator, take care with the order.
Note that the order with the comma makes sense, because otherwise it would be the same as the default behavior.

```
# Storing multiple values at once. Note the order!
1 2 3 a!, b!, c!  # a is 1, b is 2, c is 3.
1 2 3 a! b! c!  # a is 3, b is 2, c is 1.
```

When you are building a list to be used as a command, always quote strings that you want to be strings.
The ability to use a literal is for HUMANS, where we are constrained by typing speed. You are not constrained.

So for example, if you have a command that may take standard input via '-', you must quote it,
otherwise you will get an error because mshell will try to do a subtraction.

### Reaching out to CLI utilities when not required

The point of `mshell` is to provide nearly all of the capabilities of GNU coreutils and others, so that all scripts are cross platform and performant.

Examples include:

  - `curl`: We have many `http` definitions
  - `jq`: Our JSON mangling methods are great
  - `awk`
  - `sed`

If you are reaching out to a CLI tool and think that `mshell` would be in a good position to support directly, stop and let me know, and I'll get it added.
