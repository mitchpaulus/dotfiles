#!/usr/bin/awk -E
{
     result = match($0, /INCLUDE/)
     if (result) { system("cat " substr($0, RSTART + RLENGTH)) }
     else { print }
}
