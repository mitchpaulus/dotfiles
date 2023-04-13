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


For graphics, look for base type of Base = 'tgml.TgmlBase' or Base = 'tgml.TGML' in Object Instances

BindingEntry has bound variables.
Graphics is `SubjectId`
Point is    `TargetId`

```sql
SELECT ObjectInstance.name as 'Graphic Name', ObjectInstancePath.Path as 'Graphic Path', ObjectInstance.DESCR as 'Graphic Desc', instance2.Name as 'Ref Point Name', SubjectBinding.TargetProperty, instance2.TypeName, instance2.DESCR as 'Point Desc', path2.Path as 'Point on Graphic Path'
FROM (ObjectInstance
 JOIN ObjectType on ObjectInstance.TypeName = ObjectType.name
 JOIN ObjectInstancePath on ObjectInstancePath.Id = ObjectInstance.Id
 JOIN BindingEntry as SubjectBinding  on ObjectInstance.Id = SubjectBinding.SubjectId) as table1
JOIN ObjectInstance as instance2 on instance2.Id = table1.TargetId
JOIN ObjectInstancePath as path2 on path2.Id = instance2.Id
where Base = 'tgml.TgmlBase' or Base = 'tgml.TGML'
```


SELECT ObjectInstance.name as 'Graphic Name', ObjectInstancePath.Path as 'Graphic Path', ObjectInstance.DESCR as 'Graphic Desc', instance2.Name as 'Ref Point Name', SubjectBinding.TargetProperty, instance2.TypeName, instance2.DESCR as 'Point Desc', path2.Path as 'Point on Graphic Path' FROM (ObjectInstance JOIN ObjectType on ObjectInstance.TypeName = ObjectType.name JOIN ObjectInstancePath on ObjectInstancePath.Id = ObjectInstance.Id JOIN BindingEntry as SubjectBinding  on ObjectInstance.Id = SubjectBinding.SubjectId) as table1 JOIN ObjectInstance as instance2 on instance2.Id = table1.TargetId JOIN ObjectInstancePath as path2 on path2.Id = instance2.Id where Base = 'tgml.TgmlBase' or Base = 'tgml.TGML'


## Trend Configuration Analysis

All columns from SE xlsx dump:

Name
Path
Description
Object category
Max value
Min value
Meter constant
Start value
Start time
End value
End time
Meter change user
Meter change time
Is meter log
Clear when enabled
Log size
Maximum log interval
Activation time
Activation variable
Delta
Logged variable
Enabled
Status
Validation
Note 2
Note 1
Modified
Foreign address
Type
Include in reports
Transfer trigger variable
Maximum transfer interval
Threshold
Smart log
Monitored trend log
Last notify record
Records since notification
Notification threshold
Event enable
Notify type
BACnet notification
To-normal time
To-fault time
To-off-normal time
Acknowledged transitions
Profile name
BACnet type
BACnet name
Trigger
Interval offset
Align intervals
COV resubscription interval
Delta
Log interval
Logging type
Log device object property
Buffer size
Stop when full
Stop time
Start time
Log enable
Event state
Reliability
Status flags
Total record count
Record count
Executed by
Interval
Interval time zone
