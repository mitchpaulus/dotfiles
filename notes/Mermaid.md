# Mermaid

- extension: `.mmd`
- The recommended MIME type for mermaid media is `text/vnd.mermaid`.
- CLI
    - <https://github.com/mermaid-js/mermaid-cli>
    - `mmdc -i input.mmd -o output.svg`

# Gantt Charts

See:
  - <https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/diagrams/gantt/ganttDb.js>


```javascript
const tags = ['active', 'done', 'crit', 'milestone'];


// https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/diagrams/gantt/ganttDb.js#379
// Task Data formats (note that tag can come before all of this)
// id, startDate, endDate
// id, startDate, length
// id, after x, endDate
// id, after x, length
// startDate, endDate
// startDate, length
// after x, endDate
// after x, length
// endDate
// length
```

```
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :1d
    Functionality added                 :milestone, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
```
