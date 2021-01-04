# Reverse string
function rev(input,               result, str_length) {
    result = ""

    str_length = length(input)

    for (i = str_length; i >= 1; i--) {
        result = result substr(input, i, 1)
    }
    return result
}
