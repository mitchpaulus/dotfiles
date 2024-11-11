# PDF to Text

`pdftotext`: Part of the poppler package

# PDF To PNG

`pdftoppm -png`: Also part of `poppler-utils` package

Example extraction for bookmarks.

```sh
#!/bin/sh

pdftoppm -r 300 -x 4575 -y 2901 -W 438 -H 138 -png 'Spectrum-CUP & Labs-Control Drawings.pdf'  title
pdftoppm -r 300 -x 4575 -y 3105 -W 438 -H 90 -png  'Spectrum-CUP & Labs-Control Drawings.pdf' sheet_num
```
