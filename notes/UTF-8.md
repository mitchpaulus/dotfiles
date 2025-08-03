Code point ↔ UTF-8 conversion First code point 	Last code point 	Byte 1 	Byte 2 	Byte 3 	Byte 4
U+0000 	U+007F 	0yyyzzzz
U+0080 	U+07FF 	110xxxyy 	10yyzzzz
U+0800 	U+FFFF 	1110wwww 	10xxxxyy 	10yyzzzz
U+010000 	U+10FFFF 	11110uvv 	10vvwwww 	10xxxxyy 	10yyzzzz
