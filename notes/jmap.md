In Email/get, maxBodyValueBytes cannot be 0, it needs to be omitted in that case.

### JMAP “cheat sheet” (Fastmail + Mail)

- `GET https://api.fastmail.com/jmap/session`
- Grab **`apiUrl`** (where you POST) + **mail `accountId`**.


`POST {apiUrl}` with JSON:
  * `using: [...]` (capabilities)
  * `methodCalls: [ [methodName, args, callId], ... ]`

* **Method calls are batched**

  * One POST can do: `Mailbox/query` → `Email/query` → `Email/get`, etc.
  * Response is `methodResponses` in the same callId order.

* **Mailbox IDs vs “Inbox”**

  * Filters usually need **mailbox id**, not the string “Inbox”.
  * Find Inbox by role:

    * `Mailbox/query` with `filter: { "role": "inbox" }` → ids like `"P-F"`.

* **Search/list emails**

  * `Email/query` returns **email ids** (paged), not bodies.
  * Page with `position` + `limit`.
  * Use `sort` (e.g. `receivedAt desc`).

* **Fetch email details**

  * `Email/get` returns exactly the fields you request via `properties`.
  * For bodies:

    * ask for `textBody`, `htmlBody`, `bodyValues`
    * set `fetchTextBodyValues: true`, `fetchHTMLBodyValues: true`

* **Bodies are keyed by `partId`**

  * `bodyValues` keys are **`partId` strings**, not “1 means text”.
  * Determine which is which by:

    * `textBody[*].partId` (usually `text/plain`)
    * `htmlBody[*].partId` (usually `text/html`)
  * Then read: `bodyValues[partId].value`.

* **Result references (wiring calls together)**

  * Use `#`-prefixed args like `"#ids"` to pull output from a prior call:

    * `"#ids": { "resultOf": "q", "name": "Email/query", "path": "/ids" }`
  * `name` is a safety check to ensure you referenced the right method.

* **Large content / attachments**

  * Each body part has `blobId` (+ `type`, `size`). Use blob download when you want streaming/attachments.

* **Syncing**

  * Many responses include `state` / `queryState`. Use these to do incremental changes later (instead of re-listing everything).

# Filters



```
["Email/query" {
            "accountId": @accountId,
            "filter": {
                "inMailbox": "P-F",
                "subject": "Ordered:"
                "after": "2026-01-24T00:00:00Z"
                "before": "2026-01-24T00:00:00Z"
            },
            "sort": [{ "property": "receivedAt", "isAscending": false }],
            "position": 0,
            "limit": 20
        } "q"]
```
