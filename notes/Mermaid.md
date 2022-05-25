# Gantt Charts

See:
  - <https://github.com/mermaid-js/mermaid/blob/develop/src/diagrams/gantt/ganttDb.js>


```javascript
const tags = ['active', 'done', 'crit', 'milestone'];


// https://github.com/mermaid-js/mermaid/blob/develop/src/diagrams/gantt/ganttDb.js#L281
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
