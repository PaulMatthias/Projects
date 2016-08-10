#include <fstream>
#include <sstream>
#include <vector>

void assign_prod_to_cell(vector<worker>& workers, vector<product>& products);

void assign_prod_to_cell_mc(vector<worker>& workers, vector<product>& products);

int red_and_set_free(vector<worker>& workers, vector<product>& products, vector<int> worker_times, vector<int> worker_times2, int products_finished, int max_prod_status);
