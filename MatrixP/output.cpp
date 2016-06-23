#include <iostream>
#include <vector>

using namespace std;

void output(std::vector<int> out_time, std::vector<int> out_prod ){

    std::ofstream mytime;
    mytime.open("rest_time.dat",fstream::out);
    for (int i=0; i<out_time.size();i++){
      mytime <<i<<" "<< out_time[i]<<endl;
    }
    mytime.close();

    std::ofstream myprod;
    myprod.open("products.dat", fstream::out);
    for (int i=0; i<out_prod.size();i++){
      myprod <<i<<" "<< out_prod[i]<<endl;
    }
    myprod.close();

    std::ofstream rt_per_prod;
    rt_per_prod.open("rt_per_prod.dat", fstream::out);
    for (int i=0; i<out_prod.size();i++){
      rt_per_prod<<i<<" "<< (double) out_time[i]/out_prod[i]<<endl;
    }
    rt_per_prod.close();
}
