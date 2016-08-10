#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "../h/init.h"
#include "../h/var.h"
#include "../h/output.h"
#include "../h/optimize.h"
#include "../h/core_functions.h"
#include "../h/init_worker_from_file.h"

#define DEFINE_VARIABLES

using namespace std;

int main(){

    unsigned int t, out_start;

    unsigned int tmax=100;  //default value
    unsigned int max_minute = 10;
    unsigned int max_prod_status = 3;
    unsigned int products_finished = 0;
    //TODO put this value in sys_param
    unsigned int limit_of_rest = 2;
    out_start=100;

    std::vector<product> list_of_products; 
    init_products(list_of_products);
    std::vector<worker> list_of_workers;
    init_workers_from_file(list_of_workers);

    std::vector<int> worker_times;
    std::vector<int> worker_times2;
    worker_times.resize(list_of_workers.size());
    worker_times2.resize(list_of_workers.size());

    string current_status;

    init_sys_params("sys_params.dat", tmax, max_minute, max_prod_status, out_start);

    unsigned int time_of_rest = 0;
    std::vector<int> out_time;
    std::vector<int> out_prod;


    //create array with initial times of cells for resetting after they finished one working package (ap1 or ap2)
    for (unsigned int i=0; i<worker_times.size(); i++){
      worker_times[i] =(int) list_of_workers[i].minute1*list_of_workers[i].efficiency;
      worker_times2[i]=(int) list_of_workers[i].minute2*list_of_workers[i].efficiency;
    }

/**************************************************************************************************
 *
 * BEGIN MAIN LOOP
 * 
 * *********************************************************************************************/
    cout<<endl;
    cout<<"********************************************"<<endl;
    cout<<"Beginning Main Loop"<<endl;
    cout<<"********************************************"<<endl;
    cout<<endl;

    for (t=0;t<=tmax;++t){

     if(t%50==0) cout<<"Timestep t="<<t<<" of "<<tmax<<endl;

      //look for free worker with ap1 or ap2  =1 to start on a new product
      for (unsigned int i=0;i<list_of_workers.size();i++){
	if ((list_of_workers[i].skill1==1 || list_of_workers[i].skill2==1) && list_of_workers[i].status=="free"){
	  init_product(list_of_products, list_of_workers[i]);
	}
      }

      //Loop cells to look for free cells and send looking products to them
      assign_prod_to_cell(list_of_workers, list_of_products);
      
      //optimize future steps and avoid too much freetime and production
      //atm the optimal config is just a config with a low enough free time rate
      //try out best solution approach later on
      int rest_orig=plan_ahead(list_of_workers, list_of_products, worker_times, worker_times2, max_minute, t, max_prod_status);
      if(rest_orig>=limit_of_rest){
	int j=0;
	int rest_opt;
	std::vector<worker> workers_opt;
	std::vector<product> products_opt;
	while(optimize_mc(list_of_workers, workers_opt, list_of_products, products_opt, worker_times, worker_times2, max_minute, t, max_prod_status, rest_opt)>=limit_of_rest){
	  j++;
	  if(j>=20) break;
	}
	if(j<20 && rest_opt<rest_orig){
	  list_of_workers=workers_opt;
	  list_of_products=products_opt;
	} else{
	  cout<<"Rest Time before: "<<rest_orig<<endl;
	  cout<<"Rest Time after opt: "<<rest_opt<<endl;
	}
      }
	
      //Integral Time of Rest
      for (unsigned int j=0;j<list_of_workers.size();j++){
	if(list_of_workers[j].status=="free"){
	  time_of_rest++;
	}
      }

      //Reduce time needed here and set free finished working cells      
      products_finished=red_and_set_free(list_of_workers, list_of_products, worker_times, worker_times2, products_finished, max_prod_status);




#if 0 //This is debug output which shows every occupied worker and engaged product
    for (int i=0;i<list_of_products.size();i++){
      if (list_of_products[i].worked_by_next!="noone"){
      cout<<list_of_products[i].name<<" is "<< list_of_products[i].status<<" in minute "<< t << " worked by "<< list_of_products[i].worked_by <<" "<<"worked on next by "<<list_of_products[i].worked_by_next<<endl;
      cout<<"Current prod status: "<<list_of_products[i].prod_status<<endl;
      }
    }
    for (int i=0;i<list_of_workers.size();i++){
      if(list_of_workers[i].status=="occupied" || list_of_workers[i].work_next!="nothing" ){
      cout<<list_of_workers[i].name<<" is "<< list_of_workers[i].status <<" in minute "<< t << " and still needs "<<list_of_workers[i].minute1 <<" working next on "<<list_of_workers[i].work_next<<endl;
      }
    }
#endif
    


    //Creating output arrays
    out_time.push_back(time_of_rest);
    out_prod.push_back(products_finished);

    if(t>=out_start){
      std::vector<vector<int> > out_run;
      //give status an int value
      for(unsigned int cell=0; cell<list_of_workers.size(); cell++){
	std::vector<int> row;
	int status;
	if(list_of_workers[cell].status=="occupied") {
	  status=0;
	} else if(list_of_workers[cell].status=="waiting") {
	  status=1;
	} else if(list_of_workers[cell].status=="free"){
	  status=2;
	} else {
	  cout<<"UNrecognized cell status"<<endl;
	}
	row.push_back(t);
	row.push_back(cell);
	row.push_back(status);
	out_run.push_back(row);
      }
      output_run(out_run, list_of_workers.size(), t);
    }

  }//tmax

  cout<<endl;
  cout<<"********************************************"<<endl;
  cout<<"Ending Main Loop"<<endl;
  cout<<"********************************************"<<endl;
  cout<<endl;
    

  output(out_time, out_prod, list_of_workers);

  cout<<"After timestep t="<<t<<" are "<<products_finished<<" products finished"<<endl;
  cout<<endl;
    
  return 0;
}
