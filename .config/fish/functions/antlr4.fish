function antlr4
    if count $ANTLR_JAR > /dev/null
        java -jar $ANTLR_JAR[1] $argv
    else
        printf "The ANTLR jar file was not found. Usually should be at /usr/local/lib/antlr-xx-complete.jar\n"
    end
end
