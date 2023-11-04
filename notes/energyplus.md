# EnergyPlus

There are no `Branch` objects on the demand side of an AirLoop.

For a typical single duct air system there will be one
`AirLoopHVAC:SupplyPath` and one `AirLoopHVAC:ReturnPath`. A typical dual
duct system would have 2 `AirLoopHVAC:SupplyPaths` one for the hot air and
one for the cold air and 1 `AirLoopHVAC:ReturnPath`.


## Viewing Results

<https://drajmarsh.bitbucket.io/data-view2d.html>

## Schedule Creation

Can use web app <https://drajmarsh.bitbucket.io/schedule-editor.html> for generating schedules.


```
Schedule:Day:Interval,
  PH AHU Weekend Schedule,   ! Name RefList: [DayScheduleNames], REQ, #1
  ,   ! Schedule Type Limits Name [ScheduleTypeLimitsNames], #2
  No,   ! Interpolate to Timestep Def: No, [Average, Linear, No], #3
  until: 07:00 ,   ! Time 1 {hh:mm}, #4
  0, ! Value Until Time 1 #5
  until: 20:00,
  1,
  until: 24:00,
  0;

! Min Fields: 3
Schedule:Week:Compact,
  PH AHU Weekly Schedule,   ! Name RefList: [WeekScheduleNames], REQ, #1
  Weekdays,   ! DayType List 1 [AllDays, AllOtherDays, Weekdays, Weekends, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Holiday, SummerDesignDay, WinterDesignDay, CustomDay1, CustomDay2], REQ, #2
  PH AHU Weekday Schedule,
  Weekends,
  PH AHU Weekend Schedule;   ! Schedule:Day Name 1 [DayScheduleNames], REQ, #3


! Min Fields: 7
Schedule:Year,
  PH AHU Schedule,   ! Name RefList: [ScheduleNames], REQ, #1
  ,   ! Schedule Type Limits Name [ScheduleTypeLimitsNames], #2
  PH AHU Weekly Schedule,   ! Schedule:Week Name 1 [WeekScheduleNames], REQ, #3
  1,   ! Start Month 1 REQ, #4
  1,   ! Start Day 1 REQ, #5
  12,   ! End Month 1 REQ, #6
  31;   ! End Day 1 REQ, #7
```


## Meters

Facility: Everything
Building: Lighting and Plugs
HVAC: Fans/Electric Reheat Coils
Plant: Chiller Power, CT Power, CHW/HW Pumps


## Weather

[Required weather variables](https://unmethours.com/question/32238/documentation-on-required-epw-variables-to-run-energyplus/)

[Climate.OneBuilding.Org](https://climate.onebuilding.org/)

[Weather sources](https://unmethours.com/question/21291/what-sources-are-available-for-typical-weather-data-beyond-energyplusnet/)

<https://unmethours.com/question/1/what-are-the-available-sources-for-historical-weather-data/>


# Scheduling

1.26.1.0.1 Schedules And Availability Manager Regarding component schedules,
the general rule is don’t schedule any components except the supply fan and the corresponding availability manager(s).
Beyond that, every component should always be available and let the controls determine what runs or doesn’t run.
If a component other than the supply fan is scheduled off, then it will remain off even if the night cycle manager turns on the system.

The output from each System Availability Manager is an availability status flag.
This flag can have the values `NoAction`, `ForceOff`, `CycleOn`, or `CycleOnZoneFansOnly`.
The availability status flags for the System Availability Managers referenced by an air or plant loop are used to set the availability status flag for each loop.
For the air loops and zone components, `ForceOff` takes precedence: if any of the loop’s (or zone component’s) availability managers are showing status `ForceOff`,
the loop (or zone component fan) status will be `ForceOff`.
Next in precedence is `CycleOnZoneFansOnly` (only for air loop), followed by `CycleOn`, and `NoAction`.
For the plant loops, there is no precedence among the System Availability Manager status flag values.
Instead, the first availability manager giving a status flag value other than `NoAction` sets the status for the loop.
The System Availability Managers are executed in `AvailabilityManagerAssignmentList` order.
The actual action of turning on or off a loop is taken by the loop prime movers: fans for `AirLoopHVACs` and zone components, and pumps for plant loops.
For instance when a fan is deciding whether it is on or off, it checks its on/off schedule and whether the loop availability status flag is `CycleOn` or `ForceOff`.
If the schedule is on and the status flag is `ForceOff`, the fan will be off.
If the fan schedule says off and the status flag is `CycleOn`, the fan will be on.
Thus the availability managers overrule the fan on/off schedule.
The availability managers, air loops, and plant loops all have output variables which may be used to verify the action of the loop.

Example:

```
AirLoopHVAC,
    VAV_1,                   !- Name
    ,                        !- Controller List Name
    VAV_1 Availability Manager List,  !- Availability Manager List Name
    AUTOSIZE,                !- Design Supply Air Flow Rate {m3/s}
. . .

AvailabilityManagerAssignmentList,
    VAV_1 Availability Manager List,  !- Name
    AvailabilityManager:NightCycle,  !- Availability Manager 1 Object Type
    VAV_1 Availability Manager;  !- Availability Manager 1 Name

AvailabilityManager:NightCycle,
    VAV_1 Availability Manager,  !- Name
    ALWAYS_ON,               !- Applicability Schedule Name
    HVACOperationSchd,       !- Fan Schedule Name
    CycleOnAny,              !- Control Type
    1.0,                     !- Thermostat Tolerance {deltaC}
    FixedRunTime,            !- Cycling Run Time Control Type
    1800;                    !- Cycling Run Time {s}

Fan:SystemModel,
    VAV_1_Fan,               !- Name
    HVACOperationSchd,       !- Availability Schedule Name
    VAV_1_HeatC-VAV_1_FanNode,  !- Air Inlet Node Name
    VAV_1 Supply Equipment Outlet Node,  !- Air Outlet Node Name

Schedule:Compact,
    HVACOperationSchd,       !- Name
    On/Off,                  !- Schedule Type Limits Name
    Through: 12/31,          !- Field 1
    For: Weekdays SummerDesignDay, !- Field 2
    Until: 06:00,0.0,        !- Field 3
    Until: 22:00,1.0,        !- Field 5
    Until: 24:00,0.0,        !- Field 7
    For: Saturday WinterDesignDay, !- Field 9
    Until: 06:00,0.0,        !- Field 10
    Until: 18:00,1.0,        !- Field 12
    Until: 24:00,0.0,        !- Field 14
    For: AllOtherDays,       !- Field 16
    Until: 24:00,0.0;        !- Field 17

```



# General Surface matching


1. Given at least 3 points, calculate the equation of the plane, and normal to plane.
    - Get the two lines/vectors in the plane
        - B - A
        - C - A
        - Normal is cross product
2. Plane equation in point-normal form:
    - If normal vector is (a, b, c) and point on plane is (x0, y0, z0) then
    - a(x-x0) + b(y-y0) + c(z-z0) = 0
    - d = -ax0 - by0 - cz0
    - ax + by + cz + d = 0
3. Group by planes

4. Get new basis to transform all to 2 dimensions.
    - Use normal
    - Use 1st edge
    - Take cross product to get 3rd orthogonal vector

5. Get change of basis matrix
    - Inverse of matrix with new basis vectors as columns
        - `C [a]_c = a` in std basis
        - `D [a]_d = b` in std basis
        - Therefore `C [a]_c = D [b]_d` = `D^-1 C [a]_c = [a]_d`

5. Transform points to new basis
    - Whatever coordinate was related to normal should be 0 if things worked right

6. Now can do 2d polygon overlap check.


## Chillers


`Chiller:Electric:EIR`

```
P = Pref (ChillerCapFTemp) (ChillerEIRFTemp) (ChillerEIRFPLR)

P = Pref (1) (a + b Tchw + c Tchw² + d Tcw + e Tcw² + f Tchw tcw) (g + h PLR + i PLR²)

P = Pref (

Tchw*b*g+
Tchw*f*g*tcw+
Tchw^2*c*g+
Tcw*d*g+
Tcw²*e*g +
a*g
PLR*Tchw*b*h+
PLR*Tchw*f*h*tcw+
PLR*Tchw^2*c*h+
PLR*Tcw*d*h +
PLR*Tcw²*e*h+
PLR*a*h+
PLR^2*Tchw*b*i +
PLR^2*Tchw*f*i*tcw+
PLR^2*Tchw^2*c*i+
PLR^2*Tcw*d*i+
PLR^2*Tcw²*e*i +
PLR^2*a*i+
```

18 equations, 9 unknowns, so over determined system. Can solve in 2 stage process.
