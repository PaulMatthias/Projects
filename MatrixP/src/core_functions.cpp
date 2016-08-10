#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "../h/init.h"
#include "../h/var.h"
#include "../h/output.h"
#include "../h/init_worker_from_file.h"

void assign_prod_to_cell(vector<worker>& workers, vector<product>& products){
    for (unsigned int i=0;i<workers.size();i++){
      if(workers[i].status=="free"){
	for (unsigned int j=0;j<products.size();j++){
	//cout<<products[j].name<< " has to find worker with skill "<< products[j].prod_status <<endl;
	  if (((products[j].worked_by_next==workers[i].name && products[j].status=="waiting" ) ||\
	      ((products[j].prod_status+1==workers[i].skill1 || products[j].prod_status+1==workers[i].skill2) && products[j].status=="looking" )) && \
	  workers[i].status=="free"){
	    workers[i].status="occupied";
	    workers[i].work_next="nothing";
	    products[j].status="engaged";
	    products[j].worked_by=workers[i].name;
	    products[j].worked_by_next="noone";
	    products[j].prod_status+=1;
	    if(products[j].prod_status==workers[i].skill1){
	      workers[i].current_skill_used=1;
	    }else if(products[j].prod_status==workers[i].skill2){
	      workers[i].current_skill_used=2;
	    }
	  }// if status + skill1
	}//for products
      }//if worker.status free 
    }//for workers 
}


void assign_prod_to_cell_mc(vector<worker>& workers, vector<product>& products){
  
  //TODO figure out how big mc_steps has to be till the result is constant
    int mc_steps=100;
    for (unsigned int m=0;m<mc_steps;m++){
      double r1=(double) rand()/RAND_MAX;
      int i=workers.size()*r1;
      if(workers[i].status=="free"){
	double r2=(double) rand()/RAND_MAX;
	int j=products.size()*r2;
	for (unsigned int n=0;n<mc_steps;n++){
	//cout<<products[j].name<< " has to find worker with skill "<< products[j].prod_status <<endl;
	  if (((products[j].prod_status+1==workers[i].skill1 || products[j].prod_status+1==workers[i].skill2) && products[j].status=="looking" ) && workers[i].status=="free"){
	    workers[i].status="occupied";
	    workers[i].work_next="nothing";
	    products[j].status="engaged";
	    products[j].worked_by=workers[i].name;
	    products[j].worked_by_next="noone";
	    products[j].prod_status+=1;
	    if(products[j].prod_status==workers[i].skill1){
	      workers[i].current_skill_used=1;
	    }else if(products[j].prod_status==workers[i].skill2){
	      workers[i].current_skill_used=2;
	    }
	  }// if status + skill1
	}//for products
      }//if worker.status free 
    }//for workers 
}




int red_and_set_free(vector<worker>& workers, vector<product>& products, vector<int> worker_times, vector<int> worker_times2, int products_finished, int max_prod_status){
    //Loop that reduces the minutes still needed of occupied workers and setting free ready workers and products
   for (unsigned int j=0;j<workers.size();j++){
     if (workers[j].status=="occupied"){
       if(workers[j].current_skill_used==1){
	workers[j].minute1-=1;
       }else if(workers[j].current_skill_used==2){
	workers[j].minute2-=1;
       }
       //cout<<workers[j].name<< " is "<< workers[j].status<<endl;
     }
     if ((workers[j].minute1==0 && workers[j].skill1!=0) || (workers[j].minute2==0 && workers[j].skill2)) {
      workers[j].status="free";
      workers[j].current_skill_used=0;
      workers[j].minute1=worker_times[j];
      workers[j].minute2=worker_times2[j];

      for (unsigned int i=0;i<products.size();i++){
	if (products[i].worked_by==workers[j].name){
	  //products[i].prod_status+=1;
	  if(products[i].worked_by_next=="noone"){
	    products[i].status="looking";
	  } else {
	    products[i].status="waiting";
	  }
	  products[i].worked_by="noone";
	  if (products[i].prod_status==max_prod_status){
	    products_finished++; //count the numbers of finshed products
	  }
	}
       }
      }//if worker finished
    }//for workers
   return products_finished;
}



