#!/usr/bin/awk -E

# PURPOSE: Form fill templates
# USAGE:
# awk templatefile recordsfile
# Template file is typically an idf file that has '#N' placeholders.
# The 'templates' is a tab separated data file. For each row, a new instance of the template is created.
BEGIN {
    FS = "\t"
    # awk program name counts as the first argument.
    if (ARGC < 3) {
        print "2 Arguments required. " (ARGC - 1) " provided.\n\nUSAGE:\nawk -f fill_template.awk template records_file"
        exit 1
    }

    template = ARGV[1]
    ARGV[1] = ""

    while (getline < template > 0 ) {
        form[++n] = $0
    }
}

# Each line in the input/records file creates a new template,
# so this serves like another for loop.
{
    filename = ""

    # Loop over lines of the template
    for (i = 1; i <= n; i++) {
        template_line = form[i]

        # Go backwards, in case there are multiple digit substiuttions.
        # Example, if you did #1 befor #10, you'd be left with the #1
        # substitution with a 0 populated at the end.
        for (j = NF; j >= 1; j--) {
            # Clean commas from substitution (this is for numbers like 1,000)
            #gsub(/,/, "", $j)

            gsub("#" j, $j, template_line)
        }

        if (template_line ~ /FILENAME/) {
            split(template_line, split_filename, "\t")
            filename = split_filename[2]
            continue
        }

        if (filename == "") { print template_line }
        else { print template_line > filename }
    }

    close(filename)
}

