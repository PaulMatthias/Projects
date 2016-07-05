#!/bin/bash

cd src/
g++ -o matrix_prod -std=c++0x main.cpp  
mv matrix_prod ..
cd ..
./matrix_prod

