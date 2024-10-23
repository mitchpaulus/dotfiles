
```python
import fitz

doc = fitz.open("test.pdf")

bookmarks = doc.get_toc()
# List of lists: [level, title, page, dest]
# level: indentation level (1 is top level)
# page: 1-based page number


# insert_pdf(docsrc, from_page=-1, to_page=-1, start_at=-1, rotate=-1, links=True, annots=True, show_progress=0, final=1)
# from_page/to_page: 0-based, inclusive
```

# Insert PDF example

```python
doc1 = fitz.open("file1.pdf")          # must be a PDF
doc2 = fitz.open("file2.pdf")          # must be a PDF
pages1 = len(doc1)                     # save doc1's page count
toc1 = doc1.get_toc(False)     # save TOC 1
toc2 = doc2.get_toc(False)     # save TOC 2
doc1.insert_pdf(doc2)                   # doc2 at end of doc1
for t in toc2:                         # increase toc2 page numbers
        t[2] += pages1                     # by old len(doc1)
doc1.set_toc(toc1 + toc2)               # now result has total TOC


for page in doc1:
    page.get_text("text")
    page.get_text("blocks")
    page.get_text("words")

```

```
Method Description page get_text or search method

extractText()    extract plain text “text”
extractTEXT()    synonym of previous “text”
extractBLOCKS()  plain text grouped in blocks “blocks”
extractWORDS()   all words with their bbox “words”
extractHTML()    page content in HTML format “html”
extractXHTML()   page content in XHTML format “xhtml”
extractXML()     page text in XML format “xml”
extractDICT()    page content in dict format “dict”
extractJSON()    page content in JSON format “json”
extractRAWDICT() page content in dict format “rawdict”
extractRAWJSON() page content in JSON format “rawjson”
search()         Search for a string in the page Page.search_for()
```

```
blocks:
(x0, y0, x1, y1, "lines in the block", block_no, block_type)

words:
(x0, y0, x1, y1, "word", block_no, line_no, word_no)
```

Coordinates are in points (1/72 inch). y-axis 0 is at top.


<https://pymupdf.readthedocs.io/en/latest/document.html#Document.get_toc>

## Get TOC

Creates a table of contents (TOC) out of the document’s outline chain.

PARAMETERS:
simple (bool) – Indicates whether a simple or a detailed TOC is required. If False, each item of the list also contains a dictionary with linkDest details for each outline entry.

RETURN TYPE:
list

RETURNS:
a list of lists. Each entry has the form [lvl, title, page, dest]. Its entries have the following meanings:

lvl – hierarchy level (positive int). The first entry is always 1. Entries in a row are either equal, increase by 1, or decrease by any number.
title – title (str)
page – 1-based source page number (int). -1 if no destination or outside document.
dest – (dict) included only if simple=False. Contains details of the TOC item as follows:

    kind: destination kind, see Link Destination Kinds.
    file: filename if kind is LINK_GOTOR or LINK_LAUNCH.
    page: target page, 0-based, LINK_GOTOR or LINK_GOTO only.
    to: position on target page (Point).
    zoom: (float) zoom factor on target page.
    xref: xref of the item (0 if no PDF).
    color: item color in PDF RGB format (red, green, blue), or omitted (always omitted if no PDF).
    bold: true if bold item text or omitted. PDF only.
    italic: true if italic item text, or omitted. PDF only.
    collapse: true if sub-items are folded, or omitted. PDF only.
    nameddest: target name if kind=4. PDF only. (New in 1.23.7.)


## Definitions

```
rect-like: sequence of 4 numbers: x1, y1, x2, y2, in pts.
```
