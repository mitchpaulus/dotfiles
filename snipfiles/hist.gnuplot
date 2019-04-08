set terminal pngcairo

set boxwidth 50

set xlabel "CHW Plant Tonnage [tons]"
set ylabel "Occurrances"
set style fill transparent solid 0.75 border -1
#set style fillcolor rgbcolor "#004B87"
set xrange [0 < *:1300]

set output "load-hist.png"

plot "binned-load.tsv" using 1:2 with boxes notitle fillcolor rgbcolor "#004B87"

# vim:ft=gnuplot
