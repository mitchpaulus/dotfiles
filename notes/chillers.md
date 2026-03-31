# Chillers

## Trane

Installation/Operation/Maintenance Guides:
XXXX-SVX01[Rev]-[Lang]
like CDHF-SVX01N-EN

From CDHF-SVX01N-EN document.

Trane Model Number Descriptions:

Digit 1, 2, 3: Unit Function
Digit 4: Development Sequence
Digit 5,6,7,8: Nominal Tonnage
Digit 9: Unit Voltage
Digit 10,11: Design Sequence
Digit 12: Compressor Motor Power Left-Hand Circuit
Digit 13: Compressor Motor Power Right-Hand Circuit
Digit 14,15,16—Compressor Impeller Diameter Left-Hand Circuit
Digit 17,18,19—Compressor Impeller Diameter Right-Hand Circuit
Digit 20: Evaporator Tube Bundle (Nominal Tons)
Digit 21: Evaporator Tubes
Digit 22: Control Power Transformer
Digit 23: Evaporator Waterbox
Digit 24: Evaporator Waterbox Connection
Digit 25: Unit Type
Digit 26: Condenser Tube Bundle Size
Digit 27: Condenser Tubes
Digit 28: Rupture Guard™
Digit 29: Condenser Waterbox
Digit 30: Condenser Waterbox Connection
Digit 31: Control Enclosure
Digit 32: Orifice Size Left-Hand Circuit
Digit 33: Orifice Size Right-Hand Circuit
Digit 34: Starter Type Left-Hand
Digit 35: Starter Type Right-Hand
Digit 36: Enhanced Protection
Digit 37: Generic BAS
Digit 38: Water Flow Control
Digit 39: Tracer®Communication Interface
Digit 40: Condenser Refrigerant Control
Digit 41: Extended Operation
Digit 42: Chilled Water Reset:Outdoor Air Temperature Sensor
Digit 43: Operating Status
Digit 44: Gas Powered Chiller
Digit 45: Compressor Motor Frame Size Left-Hand Circuit
Digit 46: Compressor Motor Frame Size Right-Hand Circuit
Digit 47: Unit Insulation
Digit 48: Spring Isolators
Digit 49: Manufacturing Location
Digit 50: Evaporator and Condenser Size
Digit 51: Special Option

## Surge Prevention

Avoiding Centrifugal Chiller Surge ASHRAE Journal November 2018.

Plant control logic should be designed to minimize the chance for surge to occur,
which also often enhances energy performance at the same time.
For instance:

• Chilled water supply temperature should be reset upward at low loads to reduce lift.
  The reset logic should be based on chilled water valve position,
  as required by Standard 90.1, to ensure coils are not starved, which can result in loss of temperature and humidity control.
• Condenser water supply temperature should be reset downward,
  where possible, based on ambient conditions to reduce lift.
• Staging points for variable speed chillers must be adjusted as a function of current operating lift.
  It is well known that variable speed chillers can be more efficient at low load and low lift,
  but staging on more chillers to operate at low load can push the chillers into surge if the current lift is not low enough.
• Minimum tower flow must be maintained at the rate recommended by the tower manufacturer to ensure the fill remains fully wetted at the air entry,
  thus avoiding scaling on the fill which will decrease tower efficiency over time.
  The optimum control logic for cooling towers is to enable as many cells as possible without causing flow to fall below the recommended minimum.
• If condenser water flow rate is being reduced dynamically,
  avoid reducing the flow rate when the outdoor air wet-bulb temperature is high.
