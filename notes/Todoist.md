```
tl | jq -r '.[] | [.content, .project_id] | @tsv'
```
