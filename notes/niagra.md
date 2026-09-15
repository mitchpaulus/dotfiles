# Exporting CSV data out of Niagra

Video explaining
- <https://www.youtube.com/watch?v=rWxsedYc5M8>


## Extracting .dist backup files

1. Just rename as zip
2. `niagra_user_home/stations/{station}/config.bog` - zip file of the main object tree
3. `niagra_user_home/stations/{station}/shared/BCP/{num}/Project.gfx` - Programming

Old

~~1. Best way was to use `jar xvf file.dist`. Still failed at the end for missing end-of-file marker for zip, but did extract files along the way.~~

## other .dist format

Yes—Niagara and Distech are separate systems that integrate closely, but neither fundamentally depends on the other.

Tridium develops the Niagara Framework. Distech manufactures controllers and sells its own Niagara-based product line under the EC-Net name. Distech describes EC-Net as “powered by the Niagara Framework,” while Niagara itself is designed as a vendor-neutral integration platform. [Tridium Niagara overview](https://www.tridium.com/us/en/Products/niagara), [Distech EC-Net overview](https://www.distech-controls.com/en-gb/who-we-are/our-news-room/distech-controls-launches-ec-net)

## The physical hierarchy

A typical installation looks like this:

```text
Building operator
       │
       ▼
Niagara Supervisor              Optional enterprise-level server
       │
       ▼
Niagara station / JACE / EC-BOS Supervisory controller
       │
       ├── BACnet/IP
       ├── BACnet MS/TP
       ├── LonWorks
       └── Modbus
              │
              ▼
Distech field controllers       FCU, AHU, plant controllers, etc.
              │
              ▼
Sensors and actuators           Temperature, valves, fans, dampers
```

The Niagara station supervises many controllers. The Distech controllers perform the actual local equipment control.

For example:

```text
Niagara station
└── BcpBacnetNetwork
    └── FCU8
        ├── RoomTemp
        ├── FanCmd
        ├── CoolingOutput
        └── OccupiedMode
```

Those Niagara points generally represent, or act as proxies for, BACnet objects located in the physical FCU8 controller.

## The Niagara ontology

Niagara models practically everything as a component in an object graph:

```text
Station
├── Services
│   ├── AlarmService
│   ├── HistoryService
│   ├── UserService
│   └── ScheduleService
│
├── Drivers
│   └── BcpBacnetNetwork
│       ├── FCU8
│       │   ├── health
│       │   ├── address
│       │   ├── points
│       │   └── BcpParameters
│       └── AHU1
│
└── Application objects
    ├── Schedules
    ├── Control logic
    ├── PX views
    └── Tags and relations
```

The important Niagara terms are:

| Niagara concept | Meaning |
|---|---|
| Station | One running Niagara application/database |
| Component | An object in the station tree |
| Slot | A named property, child component, or action |
| Network | A driver-managed communications network |
| Device component | Niagara’s representation of a physical controller |
| Proxy point | Niagara’s representation of a value in that controller |
| Extension | Added behavior such as alarming or history collection |
| ORD | Niagara’s addressing mechanism for finding components and files |
| Handle | Internal persistent identity, such as `3ab67` |
| PX view | Niagara operator-interface graphic |
| BOG | Serialized Niagara object graph |

For example:

```text
station:|slot:/Drivers/BcpBacnetNetwork/FCU8/points/RoomTemp
```

Conceptually means:

```text
this station
→ find the Drivers component
→ find the BcpBacnetNetwork
→ find the FCU8 device
→ find its RoomTemp point
```

## The Distech ontology

Inside a Distech controller, the structure is different:

```text
Physical Distech controller
├── Hardware inputs and outputs
├── BACnet objects
├── Internal variables
├── Control application
│   ├── Function blocks
│   ├── PID loops
│   ├── Logic
│   ├── Schedules
│   └── Sequences
└── Network and device configuration
```

The `.gfx` file is the controller application developed with Distech’s EC-gfxProgram. Despite the name, “gfx” here means graphical control programming, not merely an operator graphic. EC-gfxProgram is a block-oriented programming environment for Distech ECB and ECY controllers. [Distech EC-gfxProgram](https://www.distech-controls.com/en-US/ec-gfxprogram)

In this backup:

```text
shared/Bcp/3ab67/Project.gfx
```

is the backed-up application for the physical controller represented in Niagara as:

```text
/Drivers/BcpBacnetNetwork/FCU8
```

The application executes in the controller—not in the Niagara `Project.gfx` file stored on disk. Niagara’s copy is used for backup, editing, comparison, and download.

## How the two object models meet

The integration boundary is usually BACnet:

```text
Distech controller                         Niagara station
------------------                         ---------------
BACnet device 10114       ◄──────────────► FCU8 device component
analogInput:1             ◄──────────────► RoomTemp proxy point
binaryOutput:101          ◄──────────────► FanCmd proxy point
analogValue:3             ◄──────────────► CoolingSetpoint proxy
```

There are therefore two related but distinct objects:

1. The real BACnet object in the controller.
2. The proxy component in Niagara representing it.

For example, your station contains data like:

```xml
<p n="objectId"
   t="bac:BacnetObjectIdentifier"
   v="binaryOutput:101"/>

<p n="deviceId"
   t="bac:BacnetObjectIdentifier"
   v="device:10114"/>
```

That tells Niagara that a proxy point maps to BACnet binary output 101 in BACnet device 10114.

Niagara can then add supervisory behavior around it:

```text
Controller BACnet point
        │
        ▼
Niagara proxy point
        ├── History extension
        ├── Alarm extension
        ├── Schedule link
        ├── Niagara control logic
        └── PX display binding
```

## What the Distech-specific Niagara module adds

A generic Niagara BACnet driver can discover and communicate with ordinary BACnet objects. The Distech integration adds richer manufacturer-specific tooling.

Your station uses:

```xml
t="bcs3:BcpBacnetDevice"
```

and:

```text
/Drivers/BcpBacnetNetwork
```

That is the Distech BCP integration layer. It appears to provide functions such as:

- Distech controller discovery
- Internal-point generation
- EC-gfx project backup/storage
- Controller model recognition
- Application upload and download
- Distech-specific commissioning
- Better synchronization between the GFX project and Niagara proxies

That is why each device has:

```text
BcpParameters
├── deviceHandle = 3ab67
├── modelType = ...
└── proxyGeneratorFileOrd =
    file:^Bcp/3ab67/InternalPoints.xml
```

The folder is associated with the Niagara device through its handle, while the physical device is identified over BACnet by its BACnet device ID and address.

## Can Distech controllers work without Niagara?

Yes.

Distech explicitly states that EC-gfxProgram can be used with EC-Net or standalone using BACnet, LNS, or ECLYPSE BACnet/IP. [Distech EC-gfxProgram](https://www.distech-controls.com/en-US/ec-gfxprogram)

Once downloaded, a Distech controller normally runs its local application independently:

```text
Sensor → Distech control logic → Output
```

That control loop should continue even if:

- The Niagara station is stopped
- The JACE/EC-BOS is offline
- The IP network is unavailable
- The supervisor is unavailable

What may be lost while Niagara is offline includes:

- Central graphics
- Central alarm routing
- Niagara histories
- Supervisory scheduling
- Cross-controller logic implemented in Niagara
- Remote access

A controller may still depend operationally on Niagara if the system designer put essential logic, setpoint distribution, or scheduling in the Niagara station. That is a design choice rather than an inherent product dependency.

## Can Niagara work without Distech?

Also yes.

Niagara supports numerous manufacturers and protocols. It can integrate:

- Other BACnet controllers
- LonWorks devices
- Modbus equipment
- OPC systems
- Metering systems
- Lighting systems
- Custom drivers and APIs

Tridium describes Niagara as an open, vendor-neutral platform with drivers for open and proprietary protocols. [Niagara drivers](https://www.tridium.com/us/en/Products/niagara-drivers)

A Niagara station might contain no Distech equipment at all.

## Why they are often paired

They are commonly paired because Distech offers an integrated Niagara ecosystem:

```text
Distech controllers
        +
Distech Niagara modules
        +
EC-Net / EC-BOS
        +
EC-gfxProgram
```

This gives an integrator one engineering environment for:

- Programming controllers
- Discovering points
- Building operator graphics
- Creating histories and alarms
- Scheduling
- Managing multiple protocols
- Supervising an entire building

The useful mental model is:

> Distech controls the equipment; Niagara organizes, integrates, supervises, records, and presents the overall system.

There can be overlap—Niagara can execute control logic, and some Distech ECLYPSE devices have their own web interfaces and supervisory capabilities—but that separation is the basic architecture represented in this backup.
