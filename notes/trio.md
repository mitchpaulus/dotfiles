# Trio (text record input/output)

 - entities are separated by lines beginning with "-", the lines can have as many dashes as you want
 - each entity is defined by one or more tags
 - one line is used per tag formatted as "name:val"
 - if no value is specified, the value is assumed to be Marker
 - the value is encoded using the same grammar as Zinc
 - string values may be left unquoted if they begin with a non-ASCII Unicode character or contain only the "safe" chars: A-Z, a-z, or underbar
 - if a newline follows the colon, then the value is an indented multi-line string terminated by the first non-indented line
 - nested data may be encoded with Zinc or Trio as a multi-line string prefixed with the string value "Zinc:" or "Trio:" on the tag line
 - nested lists may be encoded in Zinc as a multi-line string prefixed with "[" on the tag line; the multi-line string should be parsed as follows: 1) skip lines starting with "//", 2) strip newlines, and 3) parse a zinc <val> production
 - can use // as line comment

# Zinc Literals

 - Null: N
 - Marker: M
 - Remove: R
 - NA: NA
 - Bool: T or F (for true, false)
 - Number: 1, -34, 10_000, 5.4e-45, 9.23kg, 74.2°F, 4min, INF, -INF, NaN
 - Str: "hello", "foo\nbar\" (uses all standard escape chars as C like languages)
 - Uri: `http://project-haystack.com/`
 - Ref: @17eb0f3a-ad607713, @xyz "Display Name"
 - Symbol: ^hot-water
 - Date: 2010-03-13 (YYYY-MM-DD)
 - Time: 08:12:05 (hh:mm:ss.FFF)
 - DateTime: 2010-03-11T23:55:00-05:00 New_York or 2009-11-09T15:39:00Z
 - Coord: C(37.55,-77.45)
 - XStr: Type("value")
 - List: [1, 2, 3]
 - Dict: {dis:"Building" site area:35000ft²}
 - Grid: <<ver:"3.0" ... >>
