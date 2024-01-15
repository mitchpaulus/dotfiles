
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
```
