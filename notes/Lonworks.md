[Source](https://library.e.abb.com/public/9eff8304e07742fcba266f6e0f7d4ed1/Technical_Note_092_LonWorks_101.pdf)

Definitions:

- Lon: Local Operating Network.
- LonWorks: the general term applied to all things Lon.
- LonTalk®: a twisted pair, transformer-isolated, free (open) network that operates at 78 kbps.
- LNS®: LonWorks Network Service. The term is used in the context of set-up and configuration of the network.
- LonMaker®: the original Echelon network configuration and commissioning tool.
- IzoT CT®: the current Echelon network tool.
- SCPT: refers to Standard Configuration Property Type. Network Configurable Inputs (nci:).
- SNVT: refers to the System Network Variable Type. There are three different types defined: SNVT_switch,
  SNVT_lev, SNVT_count. They are further identified as Network Variable Inputs (nvi) and Network Variable
  Outputs (nvo).
- Neuron ID: the unique number imbedded in each Neuron chip.
- Neuron chip: the Echelon proprietary processor.
  These chip(s) are identified as 3120 or 3150 in Lon documentation.
  The Neuron ID number resides in this processor.
- Service Pin: a switch used to broadcast the Neuron ID to the LNS. See Figure 1
- Transceiver: the proprietary isolation transformer, such as the model FT-X1 shown in Figure 2.
  This part connects the processor to the network.
- Chip set: a generic term for the Neuron chip and transceiver device.
  See Figure 2. Together, this pair of devices make up the chip set.
  Every Lon device requires this chip set.

# Network differences

In listing differences between LonWorks and other RS-485 HVAC protocols such as Modbus or BACnet MS/TP, we can start with the specified wire.
By definition, EIA-485 requires shielded, twisted wire pair with 2 or 3 conductors for proper wiring.
Additional properties are identified in the TIA/EIA-485 wire recommendations.
In contrast, the original LonWorks requirement was for unshielded twisted wire pair.
And other wire properties were different than wire used in RS-485 networks.
This wiring did create noise issues at early application sites.
Over time, Echelon refined the specifications for network cabling.
Their list of acceptable wire types includes more types, including some shielded wire.

Other network differences include:

- There is no wire polarity, ( A- or B+) when connecting to the LNS. This is unique for HVAC networks.
- There is no parity such as: 8EVEN1, 8NONE1.
- There is no node ID, device address, or network ID to enter.

Although this format differs from other open protocols like BACnet, it could be seen that start-up is more plug and play and less setup.

# Network ID

The most notable is difference is how the Lon device(s) are identified on the network.
In most networks, an address is predefined and assigned to each node or location.
That ID address is then associated with a specific piece of equipment.
As an example: let’s select AHU-1S on the 4th floor.
An assigned address of 0401S will always be associated with AHU-1S.
If the equipment fails or goes offline, a technician will repair or replace parts as needed.
And if that repair includes any parts used in network comms, re-establishing that network connection is easy and logical.
This network ID for AHU-1S of 04010S is entered or programmed into the new part(s).
The network address is the same as before and is accessed at that local device.

The difference in LonWorks is how or where the network ID is created and assigned.
We must start by stating that no two Neuron IDs in the world are the same.
During commissioning, that Neuron ID number is broadcast on the network by pressing a “service pin” on the Lon device.
Once the controller reads that Neuron ID, the LNS controller associates or ties that ID to a specific Lon device and its equipment profile.
That marriage or association occurs at the network level.
Network identification and changing of network assignments is not accessible at the local device level, only at the network level.

In this example using AHU-1S, the LNS controller will always tie that Neuron ID to the AHU-1S controller.
Suppose the AHU-1S drops off the network, but an identical unit - AHU-2S, is still working.
To trouble-shoot this problem, a technician could replace the Lon device on AHU-1S.
That change means the original Neuron ID must be removed or untied from AHU-1S at the network level.
Then, the new Lon device/Neuron ID can be replaced or commissioned using the network controller.
A new network ID is created for AHU-1S, different than the previous Lon device network ID.
As stated above, this requires coordination with the LNS operator.
As another approach in troubleshooting, the technician could swap the Lon devices from AHU-1S and AHU-2.
However, the controller does not know that these devices were moved.
It only sees the Neuron IDs and identifies them as AHU-1S or AHU-2S.
The identification travels with the Lon Device or module.
Which means swapping Lon modules may be of little or no help.
If the issue with AHU-1S resides in the Lon device, the LNS operator will have to recommission that node.

There are other ways to get the Neuron ID recognized by the LNS controller.

- The Neuron ID number is usually printed on the device label or the shipping box.
  Instead of pressing the service pin, that ID can be entered into the LNS controller (by hand) during the commissioning process.

- Some newer Lon network tools have incorporated an identification method that asks the network devices:
  Who is there? or Who is new? This feature allows commissioning without pressing the service pin function.

# Commissioning

LonWorks as a network, experienced their share of growing pains.
With the network bugs worked out, the most common issues today occur at commissioning.
The hurdle for Lon implementation has been where to get the mapping files for each Lon device.
The simple and mistake-proof answer is to use the files from the Lon device.
The next paragraphs will elaborate on how to apply this rule to the commissioning process.

During the commissioning process, all LonWorks tools will ask for the source of External Interface File or XIF file.

That is the device mapping file. The choices are:

- Load the XIF files supplied by the device manufacturer, or
- Load files from another source (a network list or other memory location), or Load from device.

These three selections are non-existent in other protocols.

Figure 3 shows a screenshot from the Izot CT (Izot Commissioning Tool).
Always select Upload from device when making this choice.
Although this paragraph over-simplifies the commissioning process, this one detail has the most impact on successful implementation.

# Observations about LonWorks

Because every Lon device requires an Echelon chip, there is always added cost and space demands.
This factor prevents LonWorks from being supplied as a standard BAS protocol on an equipment supplier’s base model.
In the case of VFDs, an option card is required.
Echelon uses Microsoft Visio as part of their network tools.
Starting the network tool also opens Visio.
Echelon adds a suite of Lon basic shapes to the existing Visio selections.
Since Visio is not free, this could be seen as an added cost burden compared to other BAS protocols.
LonWorks uses variables that include: network inputs and outputs, both analog and digital.
However, some variables include both a digital portion and an analog portion.
And both functions operate independently. Here is one example:

nviDrvSpeedStpt.

- This variable is used to send both speed reference and run-stop commands.
- The value for 0.0% speed and Off is: 0.0 0. The value for 100% speed and On is: 100.0 1.
- In addition, some variables use % as their units; others use the actual engineering units of that variable.

There is a unique group of variables used in LonWorks.
The nci variables are only accessible using a LNS network tool.
Their value(s) can be sent to an individual network device and stored there.
However, they are not accessible by the actual device.

# Conclusions regarding LonWorks

LonWorks is an active protocol in building management systems.
Because LonWorks was the first open protocol, it is still popular with users who do not want to use “proprietary” protocols.
These customers chose to take advantage of the open topology benefits.
Which means existing systems built on the Lon platform will continue to need products that speak LonTalk®.
Although different from other protocols like BACnet®, LonWorks has a place in our HVAC world.
The system designers and integrators that use Lon are very proficient compared to the original system operators.
The hardware and interfaces are greatly improved.
More importantly, the users and operators understand how to implement and use the protocol.
