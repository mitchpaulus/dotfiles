# MS Word

- Refer to the same footnote or endnote more than once:
    - 'Insert cross-reference' -> Change type to Footnote. Will likely
      have to adjust the formatting to make the text supersript.

## Vertical alignment of inline images

This comes up when using images for equations. By default, the inline
figure is treated like any other character and the baseline is put to
the bottom.

The solution is to use the 'Font -> Advanced -> Position -> Lowered ->
Enter Points' dialog to shift the equation by a
certain number of points. Got this tip from [here](https://wordribbon.tips.net/T009827_Vertical_Alignment_of_an_Inline_Graphic.html)


## Find and Replace VBA

MS Word find does have some of the concepts from regular expressions.
These include (from
[https://www.customguide.com/word/how-to-use-wildcards-in-word](https://www.customguide.com/word/how-to-use-wildcards-in-word):

```
Wildcard 	Purpose                               Example
?      Any single character                     h?t will find hat, hot, and h t
*      Any number of characters                 a*d will find ad, ahead, and as compared
[ ]    One of these characters                  t[ai]n will find tan and tin, but not ton
[ - ]  One of these characters in a range       [b-d]ot will find bot, cot, and dot
[! ]   Not the specific characters              [!d]ust will find rust and must, but not dust
<      The beginning of a word                  <(some) will find something, someone, and somewhere
>      The end of a word                        (one)> will find stone, cone, and provolone
@      One or more instances of a character     cor@al will find coral and corral
{n}    Exactly n instances of a character       ^p{2} will find two consecutive paragraph breaks
{n,}   At least n instances of a character      10{2,} will find 100, 1000, and 10000
{n,m}  Between n and m instances of a character 10{2,3} will find only 100 and 1000, not 10000
```

In the replacement, a useful special character sequence is `^c`. This
will replace the value with whatever is currently on the clipboard. This
allows you to do thing like replace with fields for Figure or Table
captions.

Example of this at [this
answer.](https://answers.microsoft.com/en-us/msoffice/forum/msoffice_word-mso_winother-mso_archive/how-to-replace-the-tablefigure-caption-labels-in/23c09913-c813-4868-bf20-8624c50e6f32)

Special find/replacements:


"Find what" box only

Character  String
^1 or ^g Picture (inline pictures only)
^2, ^f (footnote), or ^e (endnote) Auto-referenced footnotes or endnotes
^5 or ^a Annotation/comment mark
^19 or ^d Opening field brace (Use only when you are viewing field codes.) (Selects whole field, not just opening brace.)
^21 or ^d Closing field brace (Use only when you are viewing field codes.) (Selects whole field, not just closing brace.)
^?  Any single character
^# Any digit
^$ Any letter
^u8195 Em space Unicode character value search
^u8194 En space Unicode character value search
^b Section break
^w White space (space, nonbreaking space, tab)
^unnnn Word 2000 Unicode character search, where "n" is a decimal number corresponding to the Unicode character value

"Replace with" Box only

Character String
^& Contents of the "Find what" box
^c Replace with the Clipboard contents

Both "Find what" and "Replace with" boxes

Character String
^9 or ^t Tab
^11 or ^l New line
^12 Page or section break (Replaces a section break with a page break)
^13 or ^p Carriage return/paragraph mark
^14 or ^n Column break
?  Question mark
^- Optional hyphen
^~ Nonbreaking hyphen
^^ Caret character
^+ Em dash
^= En dash
^m Manual page break
^s Nonbreaking space
^nnn Where "n" is an ASCII character number
^0nnn Where "n" is an ANSI character number

## Fixing Spell Check

There are times when the spell check doesn't appear to work. [This
article](https://www.lifewire.com/fix-spell-check-not-working-in-word-4693118)
has a great list of troubleshooting steps.

1.

## Moving Table Rows

One of the best shortcuts of all time
`SHIFT-ALT-<Up|Down>`

## Custom Sequences

- CTRL-F9 to create field
- `seq sequence_name`
- ` { SEQ Identifier [Bookmark] [Switches]... }`
- F9 to update
- Special switches:
  - `\c` Repeats the closest preceding sequence number.
  - `\h`: Hides the field result.
  - `\n`: Inserts the next sequence number for the specified items. Default behavior, don't usually need to specify it.
  - `\r <n>` Resets the sequence number to the specified number *n*.
  - `\s <n>`: Resets the sequence number at the heading level following the "s".
          This means you don't have to have a different field code for the first item vs. the rest with heading numbering.

  - Pattern is:
  - `{seq h1}`
  - `{seq h1 \c}.{seq h2 \s 1}`
  - `{seq h1 \c}.{seq h2 \c}.{seq h3 \s 2}`

## Grammar for MS Word Fields

[Field format specifiers](https://support.microsoft.com/en-us/office/format-field-results-baa61f5a-5636-4f11-ab4f-6c36ae43508c?ui=en-US&rs=en-US&ad=US)
[List of field codes](https://support.microsoft.com/en-us/office/list-of-field-codes-in-word-1ad6d91a-55a7-4a8d-b535-cf7888659a51)

```bnf
<Field>                           :: <Field Name> <Instructions> <Field Specific Switches> <General Switches>
<Field Name>                      :: "seq" | *See list of remaining field codes*

<General Switches>                :: <Format Switch> | <Numeric Format Switch> | <Date-Time format switch>

<Format Switch>                   :: "\*" <Format Switch Type>
<Format Switch Type>              :: <Capitalization Format> | <Number Format> | <Character Format>
<Capitalization Format>           :: "Caps" | "FirstCap" | "Upper" | "Lower"
<Number Format>                   :: "alphabetic" | "ALPHABETIC" | "Arabic" | "CardText" | "DollarText" | "Hex" | "OrdText" | "Ordinal" | "roman"
<Character Format>                :: "CharFormat" | "MERGEFORMAT"

<Numeric Format Switch>           :: "\#" <Numeric Format Switch Specifier>
<Numeric Format Switch Specifier> :: *Combination of lots of format items, can use quotations to surround the value here*

<Date-Time format switch>         :: "\@" <Date-Time Format Specifier>

<Date-Time Format Specifier>      :: *Normal date time specifiers, can use quotations to surround the value here*
```

## Changing Macro Shortcuts

File -> Options -> Customize Ribbon -> Keyboard Shortcuts: Customize ->
Change Categories to Macros, Select Macro on right


## Indenting and Tabs for Numeric Lists

```
Tab Stop = Left Indent + Hanging Indent.
```

Hanging Indent usually needs to be at least 0.3" to look appropriate and
work well when the numeric numbers get large.

For SOO documents, usually go with:

Level1: Tab stop 0.3 = 0 + 0.3
Level2: Tab stop 0.675 = 0.375 + 0.3
Level3: Tab stop 1.05
Level4: 1.425
Level5: 1.8
Level6: 2.175

## Numbering Explained

[Great site](https://wordmvp.com/FAQs/Numbering/WordsNumberingExplained.htm)

### Related VBA

[`Lists` object](https://docs.microsoft.com/en-us/office/vba/api/word.lists)

[List object](https://docs.microsoft.com/en-us/office/vba/api/word.list)


```vba
For Each li In ActiveDocument.Lists
 MsgBox li.CountNumberedItems
Next li
```

## Insert paragraph before table

Put cursor in upper left hand cell. CTRL-SHIFT-ENTER.


## Hard Reset Settings

When my autosave wasn't working, cleared the following things and had Word rebuild them:

- Registry key: `Computer\HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Word`
- `C:\Users\mpaulus\AppData\Roaming\Microsoft\Templates\Normal.dotm`
