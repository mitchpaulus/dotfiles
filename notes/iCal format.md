# iCal format

```
contentline   = name *(";" param ) ":" value CRLF
name          = iana-token | x-name
iana-token    = 1*(ALPHA | DIGIT | "-")
vendorid      = 3*(ALPHA | DIGIT)
param         = param-name "=" param-value *("," param-value)
param-name    = iana-token | x-name
param-value   = paramtext | quoted-string
paramtext     = *SAFE-CHAR
value         = *VALUE-CHAR
quoted-string = DQUOTE *QSAFE-CHAR DQUOTE
QSAFE-CHAR    = WSP / %x21 / %x23-7E / NON-US-ASCII ; Any character except controls and DQUOTE
SAFE-CHAR     = WSP / %x21 / %x23-2B / %x2D-39 / %x3C-7E / NON-US-ASCII ; Anything besides controls DQUOTE, ";", ":", and ","
VALUE-CHAR    = WSP / %x21-7E / NON-US-ASCII
```
