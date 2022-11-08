# Johnson Controls

## N2 communication

This is Johnson Controls specific communication protocol, although it is an open protocol.

See search for 'Metasys N2 Open System Protocol Specification'

- 3 wire RS-485
- max 100 devices over 4,000 ft distance.
- 9,600 bps (baud)
- Master/Slave
- 255 addresses
- Daisy chained, or serial connections.
- 3 types of communication:
  - Offline Poll: An offline device is polled once after every complete scan of all online devices
  - Online Poll: The NCM polls devices continually, according to the priority levels assigned to the devices.
                 Polling is interrupted momentarily when a command is issued through general communication.
  - General Communication: commands and requests that come from
                           application programs or operator devices. These can occur anywhere
                           on the network. This type of communication takes precedence over
                           polling. After general communication finishes, polling of online and
                           offline devices resumes.
- 4 priority levels: 0, 1, 2, and 3. 0 is the highest priority.

## Unitary Controllers (UNT)

Unitary controllers are older style controllers that have to programmed with an old Windows specific program, *HVAC PRO*.

It can make use of 'Sideloop' control, or control loops outside of the
main program.

Types of sideloops available.

● Analog Input (AI) to Analog Output (AO) (or multiple AIs to AO)
● AI to Binary Output (BO) (or multiple AIs to BO)
● Binary Input (BI) to BO
● BI to AO
● Condition single BO

References:

[Sideloops](https://docs.johnsoncontrols.com/bas/api/khub/documents/lDoi_GEQpkD7WFvGN3bY1A/content)

## Other Terminology

- IOM: Input/Output expansion module
- CGM: General purpose controller
- CVM: VAV box controller
- SNC: ?
- SNE: ?
- NAE: Network automation engine
- NCE: Network control engine
- FAC: Advanced application field equipment controller
- FEC: Field equipment controller
- VMA: Variable air volume modular assembly
- CCT: Controller configuration tool.
- SA bus: Sensor Actuator bus
