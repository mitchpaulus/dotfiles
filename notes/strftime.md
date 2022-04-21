Most important:

%F = %Y-%m-%d ISO date
%T = %H:%M:%S Time

%a     The abbreviated name of the day of the week according to the current locale.  (Calculated from tm_wday.)
%A     The full name of the day of the week according to the current locale.  (Calculated from tm_wday.)
%b     The abbreviated month name according to the current locale.  (Calculated from tm_mon.)
%B     The full month name according to the current locale.  (Calculated from tm_mon.)
%c     The preferred date and time representation for the current locale.
%C     The century number (year/100) as a 2-digit integer. (SU) (Calculated from tm_year.)
%d     The day of the month as a decimal number (range 01 to 31).  (Calculated from tm_mday.)
%D     Equivalent to %m/%d/%y.  (Yecch—for Americans only.  Americans should note that in other countries %d/%m/%y is rather common.  This means that in international context this format is ambiguous and should not be used.) (SU)
%e     Like %d, the day of the month as a decimal number, but a leading zero is replaced by a space. (SU) (Calculated from tm_mday.)
%E     Modifier: use alternative format, see below. (SU)
%F     Equivalent to %Y-%m-%d (the ISO 8601 date format). (C99)
%G     The ISO 8601 week-based year (see NOTES) with century as a decimal number.  The 4-digit year corresponding to the ISO  week  number  (see
      %V).   This  has  the  same format and value as %Y, except that if the ISO week number belongs to the previous or next year, that year is
      used instead. (TZ) (Calculated from tm_year, tm_yday, and tm_wday.)
%g     Like %G, but without century, that is, with a 2-digit year (00–99). (TZ) (Calculated from tm_year, tm_yday, and tm_wday.)
%h     Equivalent to %b.  (SU)
%H     The hour as a decimal number using a 24-hour clock (range 00 to 23).  (Calculated from tm_hour.)
%I     The hour as a decimal number using a 12-hour clock (range 01 to 12).  (Calculated from tm_hour.)
%j     The day of the year as a decimal number (range 001 to 366).  (Calculated from tm_yday.)
%k     The hour (24-hour clock) as a decimal number (range 0 to 23); single digits are preceded by a blank.  (See also  %H.)   (Calculated  from
      tm_hour.)  (TZ)
%l     The  hour  (12-hour  clock) as a decimal number (range 1 to 12); single digits are preceded by a blank.  (See also %I.)  (Calculated from
      tm_hour.)  (TZ)
%m     The month as a decimal number (range 01 to 12).  (Calculated from tm_mon.)
%M     The minute as a decimal number (range 00 to 59).  (Calculated from tm_min.)
%n     A newline character. (SU)
%O     Modifier: use alternative format, see below. (SU)
%p     Either "AM" or "PM" according to the given time value, or the corresponding strings for the current locale.  Noon is treated as "PM"  and midnight as "AM".  (Calculated from tm_hour.)
%P     Like %p but in lowercase: "am" or "pm" or a corresponding string for the current locale.  (Calculated from tm_hour.)  (GNU)
%r     The time in a.m. or p.m. notation.  In the POSIX locale this is equivalent to %I:%M:%S %p.  (SU)
%R     The time in 24-hour notation (%H:%M).  (SU) For a version including the seconds, see %T below.
%s     The number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). (TZ) (Calculated from mktime(tm).)
%S     The  second  as  a  decimal  number  (range  00  to 60).  (The range is up to 60 to allow for occasional leap seconds.)  (Calculated from tm_sec.)
%t     A tab character. (SU)
%T     The time in 24-hour notation (%H:%M:%S).  (SU)
%u     The day of the week as a decimal, range 1 to 7, Monday being 1.  See also %w.  (Calculated from tm_wday.)  (SU)
%U     The week number of the current year as a decimal number, range 00 to 53, starting with the first Sunday as the first day of week 01.  See
      also %V and %W.  (Calculated from tm_yday and tm_wday.)
%V     The  ISO 8601 week number (see NOTES) of the current year as a decimal number, range 01 to 53, where week 1 is the first week that has at
      least 4 days in the new year.  See also %U and %W.  (Calculated from tm_year, tm_yday, and tm_wday.)  (SU)
%w     The day of the week as a decimal, range 0 to 6, Sunday being 0.  See also %u.  (Calculated from tm_wday.)
%W     The week number of the current year as a decimal number, range 00 to 53, starting with the first Monday as the  first  day  of  week  01.
      (Calculated from tm_yday and tm_wday.)
%x     The preferred date representation for the current locale without the time.
%X     The preferred time representation for the current locale without the date.
%y     The year as a decimal number without a century (range 00 to 99).  (Calculated from tm_year)
%Y     The year as a decimal number including the century.  (Calculated from tm_year)
%z     The +hhmm or -hhmm numeric timezone (that is, the hour and minute offset from UTC). (SU)
%Z     The timezone name or abbreviation.
%+     The date and time in date(1) format. (TZ) (Not supported in glibc2.)
%%     A literal '%' character.
