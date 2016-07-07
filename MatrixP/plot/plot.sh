#!bin/bash

gnuplot -e "load 'plot_run.pl'"
chromium run.gif
