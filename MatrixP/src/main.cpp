#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "../h/init.h"
#include "../h/var.h"
#include "../h/output.h"
//#include "init_worker.cpp"
#include "../h/init_worker_from_file.h"

#define DEFINE_VARIABLES

using namespace std;

      //TODO add example for lineproduction
      
int main(){

    unsigned int t, out_start;


    unsigned int tmax=100;  //default value
    unsigned int max_minute = 10;
    unsigned int max_prod_status = 3;
    unsigned int products_finished = 0;
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
	

      //Loop cells to look for free cells and send waiting or looking products to them
      for (unsigned int i=0;i<list_of_workers.size();i++){
	if(list_of_workers[i].status=="free"){
	  for (unsigned int j=0;j<list_of_products.size();j++){
	  //cout<<list_of_products[j].name<< " has to find worker with skill "<< list_of_products[j].prod_status <<endl;
	    if (((list_of_products[j].worked_by_next==list_of_workers[i].name && list_of_products[j].status=="waiting" ) ||\
		((list_of_products[j].prod_status+1==list_of_workers[i].skill1 || list_of_products[j].prod_status+1==list_of_workers[i].skill2) && list_of_products[j].status=="looking" )) && \
	    list_of_workers[i].status=="free"){
	      list_of_workers[i].status="occupied";
	      list_of_workers[i].work_next="nothing";
	      list_of_products[j].status="engaged";
	      list_of_products[j].worked_by=list_of_workers[i].name;
	      list_of_products[j].worked_by_next="noone";
	      list_of_products[j].prod_status+=1;
	      if(list_of_products[j].prod_status==list_of_workers[i].skill1){
		list_of_workers[i].current_skill_used=1;
	      }else if(list_of_products[j].prod_status==list_of_workers[i].skill2){
		list_of_workers[i].current_skill_used=2;
	      }
	    }// if status + skill1
	  }//for products
	} 
      }//for workers 
      
      //plan ahead here
      for (unsigned int i=0;i<list_of_workers.size();i++){
	for (unsigned int to=0; to<max_minute; to++){
	  if(list_of_workers[i].minute1 == to && list_of_workers[i].work_next=="nothing" && list_of_workers[i].status=="free"){
	    unsigned int j=0;
	    int looking=1;
	    do{
	      if((list_of_products[j].prod_status+1==list_of_workers[i].skill1 || list_of_products[j].prod_status+1==list_of_workers[i].skill2) && \
		 list_of_products[j].worked_by_next=="noone" && \
		 list_of_products[j].worked_by!=list_of_workers[i].name && \
		 //list_of_products[j].status=="engaged" && 
		 list_of_workers[i].work_next=="nothing"){
		    list_of_products[j].worked_by_next=list_of_workers[i].name;
		    list_of_workers[i].work_next=list_of_products[j].name;
		    looking=0;
		    //cout<<"Found match"<<endl;
	      }
	      j++;
	      if(j==list_of_products.size()){
		//cout<<"Found no possible match for the next step"<<endl;
		looking=0;
	      }
	    } while (looking); 
	  }
	}
      }
      
         
      //Loop that reduces the minutes still needed of occupied workers and setting free ready workers and products
     for (unsigned int j=0;j<list_of_workers.size();j++){
       if (list_of_workers[j].status=="occupied"){
	 if(list_of_workers[j].current_skill_used==1){
	  list_of_workers[j].minute1-=1;
	 }else if(list_of_workers[j].current_skill_used==2){
	  list_of_workers[j].minute2-=1;
	 }
         //cout<<list_of_workers[j].name<< " is "<< list_of_workers[j].status<<endl;
       }
       if ((list_of_workers[j].minute1==0 && list_of_workers[j].skill1!=0) || (list_of_workers[j].minute2==0 && list_of_workers[j].skill2)) {
	list_of_workers[j].status="free";
	list_of_workers[j].current_skill_used=0;
	list_of_workers[j].minute1=worker_times[j];
	list_of_workers[j].minute2=worker_times2[j];

        for (unsigned int i=0;i<list_of_products.size();i++){
	  if (list_of_products[i].worked_by==list_of_workers[j].name){
	    //list_of_products[i].prod_status+=1;
	    if(list_of_products[i].worked_by_next=="noone"){
	      list_of_products[i].status="looking";
	    } else {
	      list_of_products[i].status="waiting";
	    }
	    list_of_products[i].worked_by="noone";
	    if (list_of_products[i].prod_status==max_prod_status){
	      products_finished++; //count the numbers of finshed products
	    }
	  }
	 }
	}
      }




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
    

  //TODO this is still a pretty naive approach for meassuring the time of non productivity of the cells
  //keep in mind that we start from scratch still, so th time of non productivity may rise till the system is filled
    for (unsigned int j=0;j<list_of_workers.size();j++){
      if(list_of_workers[j].status=="free"){
	time_of_rest++;
      }
    }

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
