# `PyPDF`

```python
import PyPDF2
```

 - Pages are 0-based

## PDF Outline Fit Types

Based on documentation from <https://www.pdftron.com/api/xamarinios/pdfnet/api/pdftron.PDF.Destination.FitType.html>, here's what these mean:

 - `/Fit`: Fits the page to the window
 - `/XYZ`: Destination specified as upper left corner point and a zoom factor
 - `/FitH`: Fits the widths of the page into the window
 - `/FitV`: Fits the height of the page into the window
 - `/FitR`: Fits the rectangle specified by its upper left and lower right corner points into the window
 - `/FitB`: Fits the rectangle containing all visible elements on the page into the window
 - `/FitBH`: Fits the width of the bounding box into the window
 - `/FitBV`: Fits the height of the bounding box into the window
