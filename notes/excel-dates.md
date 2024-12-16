# Excel Dates

Makes my head hurt. Often described as OLE Automation dates, although it doesn't quite seem to match up.

In Excel, the date time:

1900-01-01 00:00

is given the value of 1. This is midnight between the day Dec 31, 1899 and Jan 1, 1900.

All other days are considered based on the floating point number of days past that.

**BIG NOTE**: There is a bug that breaks the normal date subtraction.
The year 1900 was incorrectly assumed to be a leap year. It is not.
This means a naive subtraction from 1900-01-01 will result in an extra day.

Links:
 - <https://docs.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year>
 - <https://www.myonlinetraininghub.com/excel-date-and-time>
 - <https://www.kirix.com/stratablog/excel-date-conversion-days-from-1900.html>

So either:

  1. Subtract extra day from result if dates is past Feb 29, 1900 (which didn't exist)
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


`m` is also used for months, so be careful.

## Formulas

RD

```
=LAMBDA(year, month, day,
    365 * (year - 1) + FLOOR.MATH((year - 1)/4) - FLOOR.MATH((year - 1)/100)
    + FLOOR.MATH((year - 1)/400) + FLOOR.MATH((367 * month - 362)/12)
    + IF(month <= 2, 0,
        IF(AND(MOD(D4,4)=0,LET(mod_400,MOD(D4,400), NOT(OR( mod_400=100,mod_400=200,mod_400=300)))), -1, -2)
        )
    + day)

=LAMBDA(year, month, day, 365 * (year - 1) + FLOOR.MATH((year - 1)/4) - FLOOR.MATH((year - 1)/100) +FLOOR.MATH((year - 1)/400) + FLOOR.MATH((367 * month - 362)/12) +IF(month <= 2, 0, IF(AND(MOD(D4,4)=0,LET(mod_400,MOD(D4,400), NOT(OR( mod_400=100,mod_400=200,mod_400=300)))), -1, -2)) +day)

# gregorian-year-from-fixed

=LAMBDA(rddate,
    LET(
       g_d0, rddate -1,
       g_n400,FLOOR.MATH(g_d0/146097),
       g_d1,MOD(g_d0,146097),
       g_n100, FLOOR.MATH(g_d1/36524),
       g_d2, MOD(g_d1,36524),
       g_n4, FLOOR.MATH(g_d2/1461),
       g_d3, MOD(g_d2, 1461),
       g_n1, FLOOR.MATH(g_d3/365),
       g_year, 400*g_n400 + 100*g_n100 + 4*g_n4 + g_n1,
       IF(OR(g_n100=4,g_n1=4),g_year,g_year+1)
       )
    )(H4)


# gregorian-month-from-fixed

=LAMBDA(rddate,
   LET(
      g_year, gregorianYearFromFixed(rddate),
      g_prior_days, rddate - fixedFromGregorian(g_year,1,1),
      correction, IF(rddate < fixedFromGregorian(g_year,3,1),
                         0,
                         IF(isLeapYear(g_year), 1,2)),
    FLOOR.MATH((12*(g_prior_days + correction) + 373)/367)
   )
)


=LAMBDA(rddate, LET( g_year, gregorianYearFromFixed(rddate), g_prior_days, rddate - fixedFromGregorian(g_year,1,1), correction, IF(rddate < fixedFromGregorian(g_year,3,1), 0, IF(isLeapYear(g_year), 1,2)), FLOOR.MATH((12*(g_prior_days + correction) + 373)/367)))

# gregorian-day-from-fixed

=LAMBDA(rddate,
   LET(
    g_year, gregorianYearFromFixed(rddate),
    g_month, gregorianMonthFromFixed(rddate),
    rddate - fixedFromGregorian(g_year, g_month, 1) + 1
   )
)


=LAMBDA(rddate, LET( g_year, gregorianYearFromFixed(rddate), g_month, gregorianMonthFromFixed(rddate), rddate - fixedFromGregorian(g_year, g_month, 1) + 1))



# is-leap-year

=LAMBDA(g_year, AND(MOD(g_year,4)=0,LET(mod_400,MOD(g_year,400),   NOT(OR( mod_400=100,mod_400=200,mod_400=300)))))

```
