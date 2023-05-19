# JSON

Useful tool for building and escaping JSON from raw text: `jo`.  [link](https://github.com/jpmens/jo)

## `jq`

Also `jq` for querying and filtering data.

- When using the @tsv or @csv, the input has to be an iterable of
  arrays, not an array of arrays.

- The `-r` option is usually necessary for using `@tsv` or `@csv` to get
  the actual output, not an escaped version.

- Example:

```sh
jq -r '.[] | [.full_name, .created_at] | @tsv' 2021-05-20repos.json | sort -k2,2 -r
```

## Newtonsoft

```
var myobj = JsonConvert.DeserializeObject(json)
```

Types:

JObject for object

## Python

`dumps`, `dump`, `loads`, `load`
