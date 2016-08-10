#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include "../h/init.h"
#include "../h/var.h"
#include "../h/output.h"
#include "../h/core_functions.h"
#include "../h/init_worker_from_file.h"


int plan_ahead(vector<worker> workers, vector<product> products, vector<int> worker_times, vector<int> worker_times2, int max_minute, int t, int max_prod_status){

  int prod_finish=0;
  int time_of_rest=0;

  for (int t=0; t<=max_minute;t++){
      for (unsigned int i=0;i<workers.size();i++){
	if ((workers[i].skill1==1 || workers[i].skill2==1) && workers[i].status=="free"){
	  init_product(products, workers[i]);
	}
      }
      
      assign_prod_to_cell(workers, products);
  
      for (unsigned int j=0;j<workers.size();j++){
	if(workers[j].status=="free"){
	  time_of_rest++;
	}
      }

      prod_finish=red_and_set_free(workers, products, worker_times, worker_times2, prod_finish, max_prod_status);
  }
  return time_of_rest;
}

int optimize_mc(vector<worker> workers, vector<worker>& workers_opt, vector<product> products, vector<product>& products_opt, vector<int> worker_times, vector<int> worker_times2, int max_minute, int t, int max_prod_status, int& rest_opt){

  int prod_finish=0;
  int time_of_rest=0;
  int number_of_configs=30;

  for (int t=0; t<=max_minute;t++){
    std::vector<int> time_configs;
    std::vector<vector<worker>> worker_configs; 
    std::vector<vector<product>> product_configs; 

    time_configs.resize(number_of_configs);

    for (int conf=0; conf<number_of_configs;conf++){

      for (unsigned int i=0;i<workers.size();i++){
	if ((workers[i].skill1==1 || workers[i].skill2==1) && workers[i].status=="free"){
	  init_product(products, workers[i]);
	}
      }
      
      assign_prod_to_cell_mc(workers, products);
    
      
      for (unsigned int j=0;j<workers.size();j++){
	if(workers[j].status=="free"){
	  time_configs[conf]++;
	}
      }

      prod_finish=red_and_set_free(workers, products, worker_times, worker_times2, prod_finish, max_prod_status);

      worker_configs.push_back(workers);
      product_configs.push_back(products);
    }
    auto min_time = std::min_element(std::begin(time_configs), std::end(time_configs));
    auto min_time_pos= std::distance(std::begin(time_configs), min_time);
    //TODO think about how to evolve multiple time strings to evade landing in a local minimum
    //
    workers=worker_configs[min_time_pos];
    products=product_configs[min_time_pos];
    time_of_rest+=*min_time;
    //save first step in _opt for eventual use
    if(t==0){
      products_opt=products;
      workers_opt=workers;
    }
  }
  rest_opt=time_of_rest;
  return time_of_rest;

}
