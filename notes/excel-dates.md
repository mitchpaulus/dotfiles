# Excel Dates

Makes my head hurt. Often described as OLE Automation dates, although it
doesn't quite seem to match up.

In Excel, the date time:

1900-01-01 00:00

is given the value of 1. This is midnight between the day Dec 31, 1899
and Jan 1, 1900.

All other days are considered based on the floating point number of days
past that.

**BIG NOTE**: There is a bug that breaks the normal date subtraction. The
year 1900 was incorrectly assumed to be a leap year. It is not. This
means a naive subtraction from 1900-01-01 will result in an extra day.

Links:
 - <https://docs.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year>
 - <https://www.myonlinetraininghub.com/excel-date-and-time>
 - <https://www.kirix.com/stratablog/excel-date-conversion-days-from-1900.html>

So either:

  1. Subtract extra day from result if dates is past Feb 29, 1900 (which
     didn't exist)

  2. Or use 367 as an epoch for the date 1901-01-01 00:00.


# Format Strings

To display Use this code

Hours as 0–23 h
Hours as 00–23 hh
Minutes as 0–59 m
Minutes as 00–59 mm
Seconds as 0–59 s
Seconds as 00–59 ss
Hours as 4 AM h AM/PM

Time as 4:36 PM h:mm AM/PM
Time as 4:36:03 P h:mm:ss A/P

Elapsed time in hours; for example, 25.02 [h]:mm
Elapsed time in minutes; for example, 63:46 [mm]:ss
Elapsed time in seconds [ss]
Fractions of a second h:mm:ss.00
