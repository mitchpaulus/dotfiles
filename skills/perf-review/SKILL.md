---
name: perf-review
description: Do a total and thorough review for performance conditions
---

Please review this branch/PR for performance considerations.
Think about:
  - data locality
  - CPU cache
  - reducing memory allocations and GC pressure.
  - Whether small functions are properly inlined by the compiler.
  - exponential algorithms (n²)

Use the correct data structures for maximum performance.
Test everything to prove your assumptions. Trust experiments over heuristics.
Be prepared to present trade-offs when there's not a clear winning method.
