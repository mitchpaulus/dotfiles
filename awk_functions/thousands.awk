BEGIN {
    # Test cases
    # print rev("123456789.123456789")
    # print thousands("123456789.123456789")
    # print thousands("")
    # print thousands("1")
    # print thousands("12")
    # print thousands("123")
    # print thousands("1234")
    # print thousands("12345")
    # print thousands("123456")
    # print thousands("1234567")
    # print thousands("12345678")
    # print thousands("123456789")
}

# Add thousands separator to number
function thousands(input,             integer_part, reversed, num_commas, num_parts, output) {

    num_parts = split(input, parts, /\./)

    integer_part = parts[1]

    num_commas = int((length(integer_part)-1) / 3)

    reversed = rev(integer_part)

    output = ""
    for (i = 1; i <= num_commas; i++) {
        output = output substr(reversed, (i - 1)*3 + 1, 3) ","
    }
    # paste remaining digits
    output = output substr(reversed, (num_commas)*3 + 1, 3)

    if (num_parts > 1) {
        return rev(output) "." parts[2]
    }
    else {
        return rev(output)
    }
}

# Reverse string
function rev(input,               result, str_length) {
    result = ""

    str_length = length(input)

    for (i = str_length; i >= 1; i--) {
        result = result substr(input, i, 1)
    }
    return result
}
