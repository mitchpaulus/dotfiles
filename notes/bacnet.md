# BACnet

## Segmentation:
([link](https://store.chipkin.com/articles/segmentation-in-bacnet))
BACnet messages that don’t fit in a single packet use segmentation.
Ethernet frames have a max length of 1500 bytes (1526 for the ethernet
header [SO](https://networkengineering.stackexchange.com/a/5059)). MS/TP
may have even smaller packet size.

For large responses, both requester and device need to support
segmentation.