reset

set term gif animate delay 80
set size ratio 1

set autoscale xfix
set autoscale yfix
set xtics 1
set ytics 1

set tics scale 0,0.001
set mxtics 2
set mytics 2
set grid front mxtics mytics lw 1.5 lt -1 lc rgb 'black'

set output 'run.gif'
set palette model RGB defined (0 "red", 1 "blue", 2 "green")
set xrange[-1:10]
set xlabel 'cell position'
set yrange[-1:5]
set ylabel 'cell position'
set cbrange[0:2]
set cbtics 0,1,2
#set cbtics ("occupied" 0, "waiting" 1, "free" 2)
set cbtics ("occupied" 0,"free" 2)
set cblabel 'status of cell'
set grid

do for[i=100:200] {
set title 'timestep '.i
plot 'out/run'.i.'.dat' matrix with image title '' ,\
'ap_of_cell.dat' using 1:2:(sprintf('%s',stringcolumn(3))) with labels font ',2' title ''
}
