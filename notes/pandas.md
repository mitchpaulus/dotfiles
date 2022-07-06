# Excel

```python
pd.read_excel('file.xlsx', sheet_name='Sheet', usecols=['My col 1', 'Col 2'])

df.to_markdown(index=False, floatfmt='.1f') # index=False removes the row labels in the first column

df.loc[row_indexer, column_indexer]

# Filtering by custom function
df.loc[df['Field'].map(lambda v: custom_function(v))]
```

## DataFrame

- "index" (row labels)
- "columns" (column labels)
