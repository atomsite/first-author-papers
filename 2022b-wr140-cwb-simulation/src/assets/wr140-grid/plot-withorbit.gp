set terminal cairolatex standalone size 5in,3in
set output "grid-orbit.tex"
load "turbo.pal"


autocm=6.6845871e-14

set size ratio 0.5

set xrange [-25:25]
set yrange [-12.5:12.5]

set xlabel "X (AU)"
set ylabel "Y (AU)"

plot "mesh_structure.dat" using ($1*autocm):($2*autocm) w l lc rgb "black" notitle ,\
     "orbit.dat" using 2:3 w l ls 1 dt "." notitle  ,\
     "orbit.dat" using 4:5 w l ls 2 dt "." notitle ,\
     "orbit-sim.dat" using 2:3 w l ls 1 title "WR" ,\
     "< echo '4.665546766443406490e+00 -4.074109352257654137e+00'" lt 2 lw 4 lc rgb '#1f77b4' notitle ,\
     "< echo '-2.066356367310589359e+00 1.804410548771495648e+00'" lt 2 lw 4 lc rgb '#ff7f0e' notitle ,\
     "orbit-sim.dat" using 4:5 w l ls 2 title "OB"