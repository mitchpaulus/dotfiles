#!/usr/bin/awk -E

{

    header = $0;

    gsub(/²/, "2", header)
    gsub(/³/, "3", header)
    gsub(/°/, "deg", header)
    gsub(/[^a-zA-Z0-9]/, "_", header)
    gsub(/__+/, "_", header)
    gsub(/\#/, "num", header) # Things like 'Package #', 'Issue #', etc.

    # Trim leading and trailing underscores
    gsub(/_$/, "", header)
    gsub(/^_+/, "", header)

    header = tolower(header)

    printf "    %s = $(headers[\"%s\"])\n", header, $0
}
