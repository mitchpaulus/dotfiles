#!/usr/bin/awk -E

# Produce coefficients for simple linear regression across whitespace delimited file
# OUTPUT:
#  intercept
#  slope
#  n

BEGIN {
    OFS="\t"
    xcol = 1
    ycol = 2
    skip = 0
    for (i = 1; i <= ARGC; i++) {
        if (ARGV[i] == "--help" || ARGV[i] == "-h") {
            printf "slr.awk - Simple Linear Regression from the Terminal\n\nUSAGE:\nslr.awk <file>\n\nThe file should be a whitespace delimited text file with X values\nin the first column and Y values in the second column.\nReturns\n\nIntercept\nSlope\nCount\n"
            early_exit = 1
            exit 0
        }
        else if (ARGV[i] == "-x") {
            xcol = ARGV[i + 1]
            ARGV[i] = ""
            ARGV[i + 1] = ""
            i++
        }
        else if (ARGV[i] == "-y") {
            ycol = ARGV[i + 1]
            ARGV[i] = ""
            ARGV[i + 1] = ""
            i++
        }
        else if (ARGV[i] == "--skip") {
            skip = ARGV[i + 1]
            ARGV[i] = ""
            ARGV[i + 1] = ""
            i++
        }
        else if (ARGV[i] == "-d") {
            FS = ARGV[i + 1]
            ARGV[i] = ""
            ARGV[i + 1] = ""
            i++
        }
    }
}



# SLR

NF >= 2 && $xcol != "" && $ycol != "" && NR > skip {
    sum_x += $xcol
    sum_y += $ycol
    x[NR] = $xcol
    y[NR] = $ycol
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
