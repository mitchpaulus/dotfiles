function s1
    touch ~/.config/mp/dirs.txt
    awk -v dir=(pwd) '{ data[NR] = $0; lines++ } END { data[1] = dir; if (1 > lines) { end = 1 } else { end =lines}   for (i = 1; i <= end; i ++) { print data[i] } }' ~/.config/mp/dirs.txt > tmp
    and mv tmp ~/.config/mp/dirs.txt
end
