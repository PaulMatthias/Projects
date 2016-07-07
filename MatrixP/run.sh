#!/bin/bash

cd src/
rm matrix_prod
g++ -o matrix_prod -std=c++0x main.cpp  
#mv matrix_prod ..
./matrix_prod
cd ..

