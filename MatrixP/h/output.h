#pragma once

#include "product.h"
#include "worker.h"

void output(std::vector<int> out_time, std::vector<int> out_prod, std::vector<worker> workvec );

void output_run(std::vector<vector<int> > out_run, unsigned int number_of_cells, int t);
