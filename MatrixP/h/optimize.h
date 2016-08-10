#include <fstream>
#include <sstream>
#include <vector>

int plan_ahead(vector<worker> workers, vector<product> products, vector<int> worker_times, vector<int> worker_times2, int max_minute, int t, int max_prod_status);

int optimize_mc(vector<worker> workers, vector<worker>& workers_opt, vector<product> products, vector<product>& products_opt, vector<int> worker_times, vector<int> worker_times2, int max_minute, int t, int max_prod_status, int& rest_opt);
