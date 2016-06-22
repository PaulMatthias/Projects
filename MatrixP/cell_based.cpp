#include <iostream>
#include <vector>
#include "init.cpp"
//#include "init_worker.cpp"
#include "init_worker_from_file.cpp"

using namespace std;

int main(){

    unsigned int t, tmax;

    tmax=20;

    std::vector<product> list_of_products = init_products();
    std::vector<worker> list_of_workers = init_workers_from_file();
    std::vector<int> worker_times;
    worker_times.resize(list_of_workers.size());

    //cout<<list_of_products.size()<<endl;
    //cout<<list_of_workers.size()<<endl;
    unsigned int number_of_products=list_of_products.size();
    unsigned int number_of_workers=list_of_workers.size();
    string current_status;
    unsigned int current_prod_status;


    unsigned int max_minute = 10;


    //create array with initial times of cells for resetting 
    for (int i=0; i<worker_times.size(); i++){
      worker_times[i]=list_of_workers[i].minute1;
    }

/**************************************************************************************************
 *
 * BEGIN MAIN LOOP
 * 
 * *********************************************************************************************/

    cout<<"beginning main loop"<<endl;
    for (t=0;t<=tmax;++t){

	

	cout<<"t"<<t<<endl;
      //Loop cells to look for free cells and send waiting or looking products to them
      for (int i=0;i<list_of_workers.size();i++){
	if(list_of_workers[i].status=="free"){
	  //cout<<list_of_products[i].name<< " has to find worker with skill "<< current_prod_status+1 <<endl;
	  for (int j=0;j<list_of_products.size();j++){
	    if (((list_of_products[j].worked_by_next==list_of_workers[i].name && list_of_products[j].status=="waiting" ) ||\
		(list_of_products[j].prod_status+1==list_of_workers[i].skill1 && list_of_products[j].status=="looking" )) && \
	       	list_of_workers[i].status=="free"){
	      list_of_workers[i].status="occupied";
	      list_of_workers[i].work_next="nothing";
	      list_of_products[j].status="engaged";
	      list_of_products[j].worked_by=list_of_workers[i].name;
	      list_of_products[j].worked_by_next="noone";
	      list_of_products[j].prod_status+=1;
	    }// if status + skill1
	  }//for products
	} 
      }//for workers 
      
      //plan ahead here
      for (int i=0;i<list_of_workers.size();i++){
	for (int to=0; to<max_minute; to++){
	  if(list_of_workers[i].minute1 == to && list_of_workers[i].work_next=="nothing" && list_of_workers[i].status=="free"){
	    int j=0;
	    int looking=1;
	    do{
	      if(list_of_products[j].prod_status+1==list_of_workers[i].skill1 && \
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
     for (int j=0;j<number_of_workers;j++){
       if (list_of_workers[j].status=="occupied"){
	 list_of_workers[j].minute1-=1;
        // cout<<list_of_workers[j].name<< " is "<< list_of_workers[j].status<<endl;
       }
       if (list_of_workers[j].minute1==0){
	list_of_workers[j].status="free";
	list_of_workers[j].minute1=worker_times[j];
        for (int i=0;i<number_of_products;i++){
	  if (list_of_products[i].worked_by==list_of_workers[j].name){
	    //list_of_products[i].prod_status+=1;
	    if(list_of_products[i].worked_by_next=="noone"){
	      list_of_products[i].status="looking";
	    } else {
	      list_of_products[i].status="waiting";
	    }
	    list_of_products[i].worked_by="noone";
	  }
	 }
	}
      }
#if 1
    for (int i=0;i<number_of_products;i++){
      if (list_of_products[i].worked_by_next!="noone"){
      cout<<list_of_products[i].name<<" is "<< list_of_products[i].status<<" in minute "<< t << " worked by "<< list_of_products[i].worked_by <<" "<<"worked on next by "<<list_of_products[i].worked_by_next<<endl;
      cout<<"Current prod status: "<<list_of_products[i].prod_status<<endl;
      }
    }
#endif
    for (int i=0;i<number_of_workers;i++){
      if(list_of_workers[i].status=="occupied" || list_of_workers[i].work_next!="nothing" ){
      cout<<list_of_workers[i].name<<" is "<< list_of_workers[i].status <<" in minute "<< t << " and still needs "<<list_of_workers[i].minute1 <<" working next on "<<list_of_workers[i].work_next<<endl;
      }
    }

  }//tmax
    
  return 0;
}
