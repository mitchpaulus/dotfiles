function print_york_tools(a, wetbulb, r, lg) {
    coeffs[2] = wetbulb
    coeffs[3] = wetbulb * wetbulb
    coeffs[4] = r
    coeffs[5] = wetbulb * r
    coeffs[6] = wetbulb * wetbulb * r
    coeffs[7] = r * r
    coeffs[8] = wetbulb * r * r
    coeffs[9] = wetbulb * wetbulb * r * r
    coeffs[10] = lg
    coeffs[11] = wetbulb * lg
    coeffs[12] = wetbulb * wetbulb * lg
    coeffs[13] = r * lg
    coeffs[14] = wetbulb * r * lg
    coeffs[15] = wetbulb * wetbulb * r * lg
    coeffs[16] = r * r * lg
    coeffs[17] = wetbulb * r * r * lg
    coeffs[18] = wetbulb * wetbulb * r * r * lg
    coeffs[19] = lg * lg
    coeffs[20] = wetbulb * lg * lg
    coeffs[21] = wetbulb * wetbulb * lg * lg
    coeffs[22] = r * lg * lg
    coeffs[23] = wetbulb * r * lg * lg
    coeffs[24] = wetbulb * wetbulb * r * lg * lg
    coeffs[25] = r * r * lg * lg
    coeffs[26] = wetbulb * r * r * lg * lg
    coeffs[27] = wetbulb * wetbulb * r * r * lg * lg

    printf "%s", a
    for (i = 2; i <= 27; i++) {
        printf "\t%f", coeffs[i]
    }
    printf "\n"
}
