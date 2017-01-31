#!/bin/bash
python driver.py bfs 1,2,5,3,4,0,6,7,8
#python driver.py dfs 1,2,3,5,4,0,6,7,8 returns maximum recursion depth overflow
#python driver.py bfs 2,3,6,4,5,1,5,8,0 run over 5 mins...
#python driver.py bfs 3,1,2,0,4,5,6,7,8
#python driver.py dfs 3,1,2,0,4,5,6,7,8
python driver.py dfs 1,2,5,3,4,0,6,7,8
