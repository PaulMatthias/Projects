#!/bin/bash

cd src/
rm matrix_prod

make clean
make

./main
cd ..

