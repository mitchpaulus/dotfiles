#!/usr/bin/awk -E

# SLR

NF == 2 {
    sum_x += $1
    sum_y += $2
    x[NR] = $1
    y[NR] = $2
    n++
}

END {
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
}
