#!/bin/sh

# Need to calculate linear resets all the time in Excel. This helps me
# build the expression directly from the inputs. No more mismatched parenthesis.

# $1 = INPUT
# $2 = X1
# $3 = Y1
# $4 = X2
# $5 = Y2

printf "=IF($1 < $2, $3, IF($1 > $4, $5, $3 + (($5 - $3)/($4 - $2)*($1 - $2))))\n"
