# XML serialization C\#

From [MS](https://docs.microsoft.com/en-us/dotnet/standard/serialization/introducing-xml-serialization#items-that-can-be-serialized)

Items that can be serialized:

- Public read/write properties and fields of public classes.
- Classes that implement ICollection or IEnumerable. Note: Only collections are serialized, not public properties.
- XmlElement objects.
- XmlNode objects.
- DataSet objects.

Also:

The following should be considered when using the XmlSerializer class:

- The Sgen.exe tool is expressly designed to generate serialization assemblies for optimum performance.
- The serialized data contains only the data itself and the structure of your classes. Type identity and assembly information are not included.
- Only public properties and fields can be serialized. Properties must have public accessors (get and set methods). If you must serialize non-public data, use the DataContractSerializer class rather than XML serialization.
- *A class must have a parameterless constructor to be serialized by XmlSerializer.*
- Methods cannot be serialized.
- XmlSerializer can process classes that implement IEnumerable or ICollection differently if they meet certain requirements, as follows.
- A class that implements IEnumerable must implement a public Add method that takes a single parameter. The Add method's parameter must be consistent (polymorphic) with the type returned from the IEnumerator.Current property returned from the GetEnumerator method.
- A class that implements ICollection in addition to IEnumerable (such as CollectionBase) must have a public Item indexed property (an indexer in C#) that takes an integer and it must have a public Count property of type integer. The parameter passed to the Add method must be the same type as that returned from the Item property, or one of that type's bases.
- For classes that implement ICollection, values to be serialized are retrieved from the indexed Item property rather than by calling GetEnumerator. Also, public fields and properties are not serialized, with the exception of public fields that return another collection class (one that implements ICollection). For an example, see Examples of XML Serialization.
