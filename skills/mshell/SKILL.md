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
