#!/usr/bin/awk -E

BEGIN {

    for (i = 1; i <= ARGC; i++) {
        if (ARGV[i] == "--help" || ARGV[i] == "-h") {
            printf "slr.awk - Simple Linear Regression from the Terminal\n\nUSAGE:\nslr.awk <file>\n\nThe file should be a whitespace delimited text file with X values\nin the first column and Y values in the second column.\n"
            early_exit = 1
            exit 0
        }
    }
}

# SLR

NF == 2 && $1 != "" && $2 != "" {
    sum_x += $1
    sum_y += $2
    x[NR] = $1
    y[NR] = $2
    n++
}

END {
    if (early_exit) { exit 0 }
    x_bar = sum_x / n
    y_bar = sum_y / n

    for (i in x) {
        num += (x[i] - x_bar) * (y[i] - y_bar)
        denom += (x[i] - x_bar) * (x[i] - x_bar)
    }

    slope = num / denom

    intercept = y_bar - slope * x_bar

    print intercept
    print slope
    print n
}
