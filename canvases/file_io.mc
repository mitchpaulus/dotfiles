{
  "version": 1,
  "grid": 8.0,
  "preamble": "",
  "page": "2c69914e",
  "pages": [
    {
      "id": "2c69914e",
      "name": "Page 1",
      "view": {
        "x": 152.36416625976562,
        "y": 32.62995910644531,
        "zoom": 1.0000001192092896
      },
      "nodes": [
        {
          "id": "6656a125",
          "type": "typst",
          "x": 512.0,
          "y": 72.0,
          "width": 320.0,
          "height": null,
          "source": "- Atomic writes without tears: https://lwn.net/Articles/974578/"
        },
        {
          "id": "de0bae4c",
          "type": "typst",
          "x": -96.0,
          "y": 160.0,
          "width": 600.0,
          "height": null,
          "source": "#table(\n  columns: 3,\n  table.header([*Layer*], [*Linux*], [*Windows*]),\n  [Per-process reference], [file descriptor], [handle],\n  [Per-open state (position, flags)], [open file description (`struct file`, `linux/include/linux/fs.h`), as many as per `open` calls], [`FILE_OBJECT`],\n  [Per-file state (size, locks)], [inode - 1 per file], [FCB/SCB, owned by the file system driver],\n  [Memory cache], [page cache], [cache manager],\n  [Background flush], [writeback], [lazy writer],\n  [Explicit flush], [`fsync`], [`FlushFileBuffers`],\n)"
        }
      ]
    }
  ]
}
