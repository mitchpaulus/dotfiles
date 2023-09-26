# Date Algorithms

## Leap Years

Every year that is exactly divisible by four is a leap year,
except for years that are exactly divisible by 100,
but these centurial years are leap years if they are exactly divisible by 400.

```
is_leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
```

if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)

Latest leap years are divisible by 4, including 2000.

1988
1992
1996
2000
2004
2008
2012
2016
2020
2024
2028

## Day of the Week Algorithm

[Wikipedia Entry](https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#cite_note-20)

[From Zeller Algorithm](https://web.cs.dal.ca/~jamie/CS3172/Course/assig/zeller.html)

Let

month be
    the month of the year, with March=1, April=2,…, December=10, January=11, February=12
    N.B.: January and February are considered to be part of the previous year.  If the month is January or February then you must subtract one from year (which is defined below).
day be
    the day of the month
century be (digits up until the last 2)
    the century
year be
    the year within the century (the last 2 digits of the year)
    See the note (above) about how the months of January and February change the value of year
weekday be
    0 for Sunday, 1 for Monday, 2 for Tuesday,…, 6 for Saturday

then

weekday = ((13 × month − 1) ÷ 5 +
            year ÷ 4 +
            century ÷ 4 +
            day +
            year −
            2 × century) % 7

I find the Sakamoto method to be better:

```c
dayofweek(y, m, d)	/* 1 <= m <= 12,  y > 1752 (in the U.K.) ,  1 <= d <= 31 */
{
    static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
    if ( m < 3 ) { y = y - 1; }
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}
```

```python
def dayofweek(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y = y - 1
    return (y + int(y/4) - int(y/100) + int(y/400) + t[m-1] + d) % 7
```

Or from: <https://www.tondering.dk/claus/cal/chrweek.php#calcdow>

To calculate the day on which a particular date falls, the following algorithm may be used. (Click here for a description of the symbols   and   and the operator ‘mod’.)

```
a	=	floor(14 – month / 12)
y	=	year – a
m	=	month + 12a – 2

# For the Julian calendar:
d	=	( 5 + day + y + floor(y/4) + floor(31*m/12) mod 7

# For the Gregorian calendar:
d	=	(day + y +  floor(y/4)  –  floor(y/100) + floor(y/400)  +  floor(31*m / 12) mod 7

```
The value of d is 0 for a Sunday, 1 for a Monday, 2 for a Tuesday etc.
Example: On what day of the week was the author born?

My birthday is 2 August 1953 (Gregorian, of course).

a	= floor((14 – 8) / 12) = 0
y	=	1953 – 0 = 1953
m	=	8 + 12 × 0 – 2 = 6
d	=	( 2 + 1953 +  1953 4  –  1953 100  +  1953 400  +  31 × 6 12) mod 7
  =	(2 + 1953 + 488 – 19 + 4 + 15) mod 7
  =	2443 mod 7
  =	0

I was born on a Sunday.


Books:

From [Calendar FAQ](https://www.tondering.dk/claus/cal/faqfaq.php),

Edward M. Reingold & Nachum Dershowitz: Calendrical Calculations. Third Edition. Cambridge University Press 2008. ISBN 978-0-521-70238-6


## Calendrical Calculations

```
# Months 1 - 12
# Days 1 - 31

fixed-from-gregorian =
    365 * (year - 1) + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year -1)/400) + floor((367 * month - 362) / 12) + adj + day

adj = if (month <= 2) then 0
      else if (is-leap-year(year)) then -1
      else -2


gregorian-year-from-fixed = if (n_100 == 4 or n_1 == 4) year
                            else year + 1

where:

d0 = date - gregorian_epoch
n_400 = floor(d0 / 146097)
d1 = d0 mod 146097



```
