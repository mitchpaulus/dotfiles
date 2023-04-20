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


## Types

25 standard types (Directly from standard Version 2004)

1. ACCUMULATOR
2. ANALOG_INPUT
3. ANALOG_OUTPUT
4. ANALOG_VALUE
5. AVERAGING
6. BINARY_INPUT
7. BINARY_OUTPUT
8. BINARY_VALUE
9. CALENDAR
10. COMMAND
11. DEVICE
12. EVENT_ENROLLMENT
13. FILE
14. GROUP
15. LIFE_SAFETY_POINT
16. LIFE_SAFETY_ZONE
17. LOOP
18. MULTISTATE_INPUT
19. MULTISTATE_OUTPUT
20. MULTISTATE_VALUE
21. NOTIFICATION_CLASS
22. PROGRAM
23. PULSE_CONVERTER
24. SCHEDULE
25. TREND_LOG


### TREND_LOG

O = Optional, R = Required and readable, W = Required and writable

Property Identifier           | Property Datatype                     | Conformance Code
------------------------------|---------------------------------------|-----------------
`Object_Identifier`           | `BACnetObjectIdentifier`              | R
`Object_Name`                 | `CharacterString`                     | R
`Object_Type`                 | `BACnetObjectType`                    | R
`Description`                 | `CharacterString`                     | O
`Log_Enable`                  | `BOOLEAN`                             | W
`Start_Time`                  | `BACnetDateTime`                      | O
`Stop_Time`                   | `BACnetDateTime`                      | O
`Log_DeviceObjectProperty`    | `BACnetDeviceObjectPropertyReference` | O
`Log_Interval`                | `Unsigned`                            | O
`COV_Resubscription_Interval` | `Unsigned`                            | O
`Client_COV_Increment`        | `BACnetClientCOV`                     | O
`Stop_When_Full`              | `BOOLEAN`                             | R
`Buffer_Size`                 | `Unsigned32`                          | R
`Log_Buffer`                  | `List of BACnetLogRecord`             | R
`Record_Count`                | `Unsigned32`                          | W
`Total_Record_Count`          | `Unsigned32`                          | R
`Notification_Threshold`      | `Unsigned32`                          | O
`Records_Since_Notification`  | `Unsigned32`                          | O
`Last_Notify_Record`          | `Unsigned32`                          | O
`Event_State`                 | `BACnetEventState`                    | R
`Notification_Class`          | `Unsigned`                            | O
`Event_Enable`                | `BACnetEventTransitionBits`           | O
`Acked_Transitions`           | `BACnetEventTransitionBits`           | O
`Notify_Type`                 | `BACnetNotifyType`                    | O
`Event_Time_Stamps`           | `BACnetARRAY[3] of BACnetTimeStamp`   | O
`Profile_Name`                | `CharacterString`                     | O
