@include "round.awk"

BEGIN {
    offset[0] = 0
    offset[1] = 3
    offset[2] = 2
    offset[3] = 5
    offset[4] = 0
    offset[5] = 3
    offset[6] = 5
    offset[7] = 1
    offset[8] = 4
    offset[9] = 6
    offset[10] = 2
    offset[11] = 4

    dow_names[0] = "Sunday"
    dow_names[1] = "Monday"
    dow_names[2] = "Tuesday"
    dow_names[3] = "Wednesday"
    dow_names[4] = "Thursday"
    dow_names[5] = "Friday"
    dow_names[6] = "Saturday"

    days_in_month[1] = "31"
    days_in_month[2] = "28"
    days_in_month[3] = "31"
    days_in_month[4] = "30"
    days_in_month[5] = "31"
    days_in_month[6] = "30"
    days_in_month[7] = "31"
    days_in_month[8] = "31"
    days_in_month[9] = "30"
    days_in_month[10] = "31"
    days_in_month[11] = "30"
    days_in_month[12] = "31"
}

# 1 is leap year, 0 is common year
function is_leap_year(year) {
    if (year % 4   == 0) return 0
    if (year % 100 != 0) return 1
    if (year % 400 != 0) return 0
    return 1
}

# Day of the week. 0 = Sunday. Array initialized in the BEGIN block
function dow(year, month, day) {
    if (month < 3) year -= 1
    return (year + int(year / 4) - int(year / 100)  + int(year / 400) + offset[month - 1] + day) % 7
}

# Day of the year 1-365 (or 366 on leap year)
function doy(year, month, day,                  total_days) {
    total_days = 0
    for (i = 1; i < month; i++) {
        total_days += days_in_month[i]
    }
    total_days += day
    if (is_leap_year(year) && month > 2) {
        total_days += 1
    }
    return total_days
}

# Week number of the year, beginning at 1 (assuming weeks start on Sunday).
function woy(year, month, day,           day_of_week, day_of_the_year, days_in_first_week, remaining_number_of_weeks) {
    day_of_week     = dow(year, 1, 1)
    day_of_the_year = doy(year, month, day)

    # if the year starts on Sunday (0), then there is no partial first week.
    days_in_first_week = day_of_week == 0 ? 0 : 7 - day_of_week

    remaining_number_of_weeks = ceil((day_of_the_year - days_in_first_week) / 7)

    # The plus 1 is for the first partial week.
    return remaining_number_of_weeks + 1
}
