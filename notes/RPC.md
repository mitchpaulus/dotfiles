# RPC (Remote Procedure Call)

- [Wikipedia](https://en.wikipedia.org/wiki/Remote_procedure_call): When a computer program causes a procedure to execute in a different address space,
  which is coded as if it were a normal (local) procedure call,
  without the programmer explicitly coding the details for the remote interaction.

## JSON RPC

Requests have 3 members:

- `method`
- `params`
- `id`?

Response has 3 members:

- `result`: Is in the "JSON stat" format, another format standard. [JSON-stat](https://json-stat.org/format/)
- `error`
- `id`


