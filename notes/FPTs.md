Sample Terminal Unit FPT from MLIT

# Verify the unoccupied mode.

1. Document the as found unoccupied setpoints in the details.	Yes-No-NA
2. Through the BAS schedule the equipment to the unoccupied mode and verify that the unoccupied set points are now the active setpoints.	Pass-Fail
3. Decrease the cooling unoccupied space temperature setpoint 5 deg F below the actual space temperature and verify a cooling request has been initiated to the corresponding AHU.	Pass-Fail
4. Verify the damper modulates open and CFM increases to its max cooling flow setpoint to maintain the space temperature setpoint.	Pass-Fail
5. Return unoccupied setpoint to the satisfied unoccupied value.	Pass-Fail
6. Increase the heating unoccupied space temperature setpoint 5 deg F above the actual space temperature and verify a heating request has been initiated to the corresponding AHU.	Pass-Fail
7. Verify the damper modulates open to its minimum heating mode airflow setpoint to maintain the space temperature setpoint.	Pass-Fail
8. Verify the heating hot water reheat valve modulates open to maintain the unoccupied zone temperature setpoint.	Pass-Fail
9. Return to normal operation.	Pass-Fail

# Verify Zone Optimal Start

1. Through the BAS trending verify the unit Start command, run status, active setpoints and the start time to prove that optimal start was initiated.	Pass-Fail

# Verify zone occupied cooling mode operation.

1. Document as-found flow coefficient in the details.	Yes-No-NA
2. Document BAS min/max CFM setpoints in the details.	Yes-No-NA
3. Document the as-found space temperature cooling setpoint in the details.	Yes-No-NA
4. Decrease the space temperature setpoint 5 deg F below the actual space temperature and verify the damper modulates open and CFM increases to its max cooling flow setpoint to maintain the space temperature setpoint.	Pass-Fail
5. Increase the space temperature setpoint 5 deg above the actual space temperature and verify the damper modulates and CFM decreases to its minimum cooling flow setpoint to maintain the space temperature setpoint.	Pass-Fail
6. Restore setpoints to as-found values.	Yes-No-NA

# Verify the zone occupied heating mode operation.

1. Document the as-found space temperature heating setpoint in the details.	Pass-Fail
2. Increase the space temperature setpoint 5 deg above the actual space temperature and verify the damper modulates to maintain the heating airflow setpoint and the heating water coil valve modulates open to maintain the zone temperature setpoint.	Pass-Fail
3. Decrease the space temperature setpoint 5 deg F below the actual space temperature and verify the damper modulates to maintain airflow setpoint and the heating water coil valve modulates close to maintain the zone temperature setpoint.	Pass-Fail
4. Restore setpoints to as-found values.	Pass-Fail

# Verify BAS alarms

1. Verify Space Temperature Sensor Failure.  Document method of simulating  condition in Details.	Pass-Fail
2. Verify Airflow Alarm (Out of range +/- 20%).  Document method of simulating  condition in Details.	Pass-Fail
3. Verify High Zone Temperature Alarms.   Document method of simulating  condition in Details.	Pass-Fail
4. Verify Low Zone Temperature Alarm.   Document method of simulating  condition in Details.	Pass-Fail

# Verify BAS graphics

1. Verify that the BAS graphics package for this system matches the submitted graphics and installed conditions.	Pass-Fail
