#include <iostream>
#include <vector>
#include "init.cpp"
#include "init_worker.cpp"

using namespace std;

int main(){

    unsigned int t, tmax;

    tmax=50;

    std::vector<product> list_of_products = init_products();
    std::vector<worker> list_of_workers = init_workers();
    //cout<<list_of_products.size()<<endl;
    //cout<<list_of_workers.size()<<endl;
    unsigned int number_of_products=list_of_products.size();
    unsigned int number_of_workers=list_of_workers.size();
    string current_status;
    unsigned int current_prod_status;



    cout<<"beginning main loop"<<endl;
    for (t=0;t<=tmax;++t){

        for (int i=0;i<number_of_products;i++){
	  cout<<list_of_products[i].name<<" is "<< list_of_products[i].status<<" in minute "<< t << " worked by "<< list_of_products[i].worked_by <<endl;
	}
        for (int i=0;i<number_of_workers;i++){
	  cout<<list_of_workers[i].name<<" is "<< list_of_workers[i].status <<" in minute "<< t << " and still needs "<<list_of_workers[i].minute <<endl;
	}
	
	cout<<"t"<<t<<endl;
      //Loop for products to look for free workers and set their status to occupied and engaged
      for (int i=0;i<number_of_products;i++){
	if(list_of_products[i].status=="looking"){
	  //cout<<list_of_products[i].name<< " has to find worker with skill "<< current_prod_status+1 <<endl;

	  for (int j=0;j<number_of_workers;j++){
	    if (list_of_products[i].prod_status+1==list_of_workers[j].skill){
	      if (list_of_workers[j].status=="free"){
		list_of_workers[j].status="occupied";
		list_of_products[i].status="engaged";
		list_of_products[i].worked_by=list_of_workers[j].name;
	      }// if free
	    }// if skill
	  }//for workers
	}// if looking
      }// for products
    
      //Loop that reduces the minutes still needed of occupied workers and setting free ready workers and products
     for (int j=0;j<number_of_workers;j++){
       if (list_of_workers[j].status=="occupied"){
	 list_of_workers[j].minute-=1;
        // cout<<list_of_workers[j].name<< " is "<< list_of_workers[j].status<<endl;
       }
       if (list_of_workers[j].minute==0){
	list_of_workers[j].status="free";
	list_of_workers[j].minute=10;
        for (int i=0;i<number_of_products;i++){
	  if (list_of_products[i].worked_by==list_of_workers[j].name){
	    list_of_products[i].prod_status+=1;
	    list_of_products[i].status="looking";
	    list_of_products[i].worked_by="noone";
	  }
	 }
	}
      
      }


  }//tmax
    
       return 0;
  cout<<__LINE__<<endl;
}
