#!/usr/bin/awk -E

BEGIN {   }

NR == 1 {
    class_name = $0
    printf "public class %s \n{\n", upperFirstLetter(class_name)
}

NR > 1 {
    type = $1

    if (type == "s") type = "string"
    else if (type == "d") type = "double"

    printf "    public %s %s { get; }\n", type, upperFirstLetter($2)

    parameters[$2] = type

}

END {
    printf "\n    public %s(",  class_name

    first = 1
    for (parameter in parameters) {
        if (first) {
            printf "%s %s", parameters[parameter], lowerFirstLetter(parameter)
        }
        else {
            printf ", %s %s", parameters[parameter], lowerFirstLetter(parameter)
        }
        first = 0
    }

    printf ")\n    {\n"

    for (parameter in parameters) {
        printf "        %s = %s\n", parameter, lowerFirstLetter(parameter)
    }

    printf "    }\n}\n"

}

function upperFirstLetter(str) {
    return toupper(substr(str, 1, 1)) substr(str, 2)
}

function lowerFirstLetter(str) {
    return tolower(substr(str, 1, 1)) substr(str, 2)
}
