# Time Zones

- Reference: https://stackoverflow.com/tags/timezone/info

- Windows Database: Microsoft maintains their own database.

  - Example Id: "Central Standard Time"

  - Viewing:
    - Examine the Windows registry key at: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones
    - `tzutil.exe /l`
    - `TimeZoneInfo.GetSystemTimeZones` in .NET
    - `EnumDynamicTimeZoneInformation` Win32 Function.

- Olson/IANA: Main time zone database now controlled by the IANA, and can be found
  at https://www.iana.org/time-zones


