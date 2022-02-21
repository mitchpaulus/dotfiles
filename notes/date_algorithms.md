# Date Algorithms

## Leap Years

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
