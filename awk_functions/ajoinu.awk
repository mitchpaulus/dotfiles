# Array join, unordered.
# EX:
# array[1] = "hello"
# array[2] = "there"
# ajoinu(array, ",") == "hello,there"
function ajoinu(array, join_str,                    first, new_string) {
    first = 1
    new_string = ""
    for (i in array) {
        if (first) {
            new_string = (new_string array[i])
            first = 0
        }
        else {
            # I don't believe there is a way to get around this way of append string data.
            # I am not sure of the performance impacts of doing it this way.
            new_string = (new_string join_str array[i])
        }
    }
    return new_string
}
