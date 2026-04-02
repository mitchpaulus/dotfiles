
# Zone Loads

Calculated Design Load: Is what you think it is
User Design Load: Calculated Design Load * Sizing Factor (1.15 or 1.25 typically for cooling and heating)

Calculated Design Air: Uses the input about temperature difference or supply temperature to back calculate the required flow.
                       Note density can be calculated from the input humidity ratio, temperature, and total pressure (function of altitude).
User Design Air: Calculated Design Air * Sizing Factor (1.15 or 1.25 typically for cooling and heating)

Note that the ratio that the zone will actually heat at is *not* taken into account here.

- Anywhere a component has an 'autosize', there should be a component sizing summary in the HTML output. Table name like:

`FullName:Component Sizing Summary_Entire Facility_ZoneHVAC:PackagedTerminalHeatPump`
