Backups stored in xml files

Root XML
ObjectType
  PropertyTab
  Verbs
    Verb[]

PropertyTab
  PropertyGroup[]
    Parameter[]  Attributes: Name, DisplayName, Description, Visibility, Optional, ReadOnly, Static RTWriteable, Unique, Copy, Nullable
      Type
      Unit
      InitValue -> This is usually a sub XML document.


InitValue sub XML document

Seen

Infinet script function
PEObject

Base:
  infinity.infinet.script.Program

  infinity.infinet.script.Function
    Code
    ByteCode
    LocalVars
    BindingVars
    ObjectVars
    FunctionVars
    FunctionArgs



In configuration.db file, the names for the scripts are in the `ObjectInstance` table, column `NAME`. The GUID identifier is the `TypeName` column.

In the `TypeName` column, infinity.infinet.Device are Andover devices.

Types beginning with 'infinity.infinet.point' are the points on devices we normally care about.

Include:
infinity.infinet.point.analog.Input
infinity.infinet.point.analog.Output
infinity.infinet.point.analog.Value
infinity.infinet.point.datetime.Value
infinity.infinet.point.digital.Input
infinity.infinet.point.digital.Output
infinity.infinet.point.digital.PulsedOutput
infinity.infinet.point.digital.Value
infinity.infinet.point.string.Value

There is type 'system.placeholder.Nonexist'

Modbus types:
bacnet.mpx.modbus.network.Modbus
modbus.folder.RSNetworkFolder
modbus.folder.RegisterGroupFolder
modbus.folder.TCPNetworkFolder
modbus.network.MasterDevice
modbus.network.MasterNetwork
modbus.network.TCPClientNetwork
modbus.network.TCPDevice
modbus.point.AnalogInput
modbus.point.AnalogOutput
modbus.point.BinaryInput
modbus.point.BinaryOutput
modbus.point.ModbusRegisterGroup

