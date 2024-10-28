# Xmllint

<https://www.baeldung.com/linux/xmllint>

Ubuntu: `libxml2-utils` package

## Escapes

```
&lt; <
&gt; >
&quot; "
&apos; '
&amp; &
&#xA; LF
&#xD; CR
```

These have to be escaped within the attribute values.

## XPath

Expression | Description
-----------|------------------------------------------------------------------------------------------------------
nodename   | Selects all nodes with the name "nodename"
/          | Selects from the root node
//         | Selects nodes in the document from the current node that match the selection no matter where they are
.          | Selects the current node
..         | Selects the parent of the current node
@          | Selects attributes



## Python

```python
import xml.etree.ElementTree as ET
import sys

file = sys.argv[1]

# Parse the XML file
tree = ET.parse(file)

# Get the root element
root = tree.getroot()

for child in root:
    child.find('element').text = 'new value'

# find and findall are not recursive by default
```
