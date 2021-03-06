#include <iostream>
#include <fstream>
#include <vector>
#include "../h/worker.h"
#include "../h/product.h"

using namespace std;

void output(std::vector<int> out_time, std::vector<int> out_prod, std::vector<worker> workvec ){

    std::ofstream mytime;
    mytime.open("../out/rest_time.dat",fstream::out);
    for (unsigned int i=0; i<out_time.size();i++){
      mytime <<i<<" "<< out_time[i]<<endl;
    }
    mytime.close();

    std::ofstream myprod;
    myprod.open("../out/products.dat", fstream::out);
    for (unsigned int i=0; i<out_prod.size();i++){
      myprod <<i<<" "<< out_prod[i]<<endl;
    }
    myprod.close();

    std::ofstream rt_per_prod;
    rt_per_prod.open("../out/rt_per_prod.dat", fstream::out);
    for (unsigned int i=0; i<out_prod.size();i++){
      rt_per_prod<<i<<" "<< (double) out_time[i]/out_prod[i]<<endl;
    }
    rt_per_prod.close();


    //TODO put this into output_run and Higlight the active AP
    //and adjust for variable amount of workng cells
    std::ofstream ap;
    ap.open("../out/ap_of_cell.dat", fstream::out);
    for (int i=0;i<10;i++){
      for(int j=0;j<5;j++){
       ap<<i<<" "<<j%6<<" "<<"AP"<<workvec[i*5+j].skill1<<"/"<<workvec[i*5+j].skill2<<endl;
      }
    }

}

void output_run(std::vector<vector<int>> out_run, unsigned int number_of_cells, int t){
    std::ofstream myrun;
    int offset=0;
    unsigned int interval=10;
    unsigned int number_of_cells_init=number_of_cells;
    myrun.open("../out/run"+to_string(t)+".dat", fstream::out);
    //for (int t=0; t<out_run.size();t++){
	 //myrun<< out_run[t][0] << " "<< out_run[t][1] <<" "<<out_run[t][2]<<endl;a
    while(interval<out_run.size()){
      for(unsigned int j=offset;j<interval;j++){
	  myrun<<out_run[j][2]<<" ";
      }
      myrun<<endl;
      offset=interval;
      interval+=10;
      if(interval>=number_of_cells){
	interval=number_of_cells;
	number_of_cells+=number_of_cells_init;
      }
    }


    //}
    myrun.close();

}
