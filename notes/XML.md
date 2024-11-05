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

# Generating CS from XML/XSD

<https://johnnyreilly.com/xsdxml-schema-generator-xsdexe-taking>

```
C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\x64\xsd.exe
xsd.exe schema.xsd /c /namespace:MyNamespace


using System.IO;
using System.Linq;
using System.Text;
using System.Xml.Serialization;

namespace My.Helpers
{
    public static class XmlConverter<T>
    {
        private static XmlSerializer _serializer = null;

        #region Static Constructor

        /// <summary>
        /// Static constructor that initialises the serializer for this type
        /// </summary>
        static XmlConverter()
        {
            _serializer = new XmlSerializer(typeof(T));
        }

        #endregion

        #region Public

        /// <summary>
        /// Deserialize the supplied XML into an object
        /// </summary>
        /// <param name="xml"></param>
        /// <returns></returns>
        public static T ToObject(string xml)
        {
            return (T)_serializer.Deserialize(new StringReader(xml));
        }

        /// <summary>
        /// Serialize the supplied object into XML
        /// </summary>
        /// <param name="obj"></param>
        /// <returns></returns>
        public static string ToXML(T obj)
        {
            using (var memoryStream = new MemoryStream())
            {
                _serializer.Serialize(memoryStream, obj);

                return Encoding.UTF8.GetString(memoryStream.ToArray());
            }
        }

        #endregion
    }
}
```
