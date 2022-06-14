# BACnet

## Segmentation:
([link](https://store.chipkin.com/articles/segmentation-in-bacnet))
BACnet messages that don’t fit in a single packet use segmentation.
Ethernet frames have a max length of 1500 bytes (1526 for the ethernet
header [SO](https://networkengineering.stackexchange.com/a/5059)). MS/TP
may have even smaller packet size.

For large responses, both requester and device need to support
segmentation.

## Port

Default port is 47808 (BAC0 in hex). Protocol is IP/UDP.

## BACnet SC

<http://www.bacnet.org/Bibliography/B-SC-Whitepaper-v15_Final_20190521.pdf>

## Alarming

Most alarming should happen through 'Notification Class' objects.

Deals with 3 events:

1. To-Offnormal - outside of specified bounds
2. To-Fault - can't determine state because sensor is offline, etc.
3. To-Normal - inside of the specified bounds.

Priority can be assigned to the object as well.
0 - 255. 0 is meant to be highest priority, most important to get resolved.

<https://docs.johnsoncontrols.com/bas/api/khub/documents/MUhtDESPd0jfXeDioMsQ4w/content>
