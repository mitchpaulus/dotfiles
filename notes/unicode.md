# Unicode

## Unicode Normalization

From https://dencode.com/en/string/unicode-normalization:

	Unicode normalization is the decomposition and composition of characters. Some
	Unicode characters have the same appearance but multiple representations. For
	example, "â" can be represented as one code point for "â" (U+00E2), and two
	decomposed code points for "a" (U+0061) and " ̂" (U+0302). It can also be
	expressed as (base character + combining character). The former is called a
	precomposed character and the latter is called a combining character sequence
	(CCS).

There are 4 different normalization forms (if it ends with D, ends up with
decomposed text, if it ends with C everything is composed to single code
point):

1. Normalization Form D (NFD): Characters are decomposed by canonical equivalence
2. Normalization Form KD (NFKD): Characters are decomposed by compatibility
3. Normalization Form C (NFC): Characters are decomposed and then re-composed by canonical equivalence
4. Normalization Form KC (NFKC): Characters are decomposed by compatibility, then re-composed by canonical equivalence


## BOM

The BOM character is FEFF at the beginning of the data stream. The
actual bytes that you will find depend on the encoding.

See [Unicode Page on BOM](https://www.unicode.org/faq/utf_bom.html#BOM)

Bytes       | Encoding Form
------------|---------------
00 00 FE FF | UTF-32, big-endian
FF FE 00 00 | UTF-32, little-endian
FE FF       | UTF-16, big-endian
FF FE       | UTF-16, little-endian
EF BB BF    | UTF-8


## Overhats and overbars

0302: Overhat
0305: Overbar

## Common mutlibyte characters

```
U+00A0	 	c2 a0	NO-BREAK SPACE
U+00B0	°	c2 b0	DEGREE SIGN
```
