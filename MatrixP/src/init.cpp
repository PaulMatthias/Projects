#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <assert.h>
#include "../h/product.h"
#include "../h/worker.h"
#include "../h/var.h"

using namespace std;

void init_products(std::vector<product>& prodVec) {


product product1("Stapler1", 0, "looking", "noone","noone"); 
product product2("Stapler2", 0, "looking", "noone","noone"); 
product product3("Stapler3", 0, "looking", "noone","noone"); 

    prodVec.push_back(product1);
    prodVec.push_back(product2);
    prodVec.push_back(product3);

}

void init_product(std::vector<product>& list_of_products, worker& worker) {

    int prod_count = list_of_products.size();
    product prod("Stapler"+to_string(prod_count), 1, "engaged", worker.name, "noone");
    list_of_products.push_back(prod);
    worker.status="occupied";
    worker.work_next="nothing";
    worker.current_skill_used=1;

}


void init_sys_params(std::string dat, unsigned int& t_max, unsigned int& max_minute, unsigned int& max_prod_status, unsigned int& out_start){

  std::map<string, double> name_to_value;

  ifstream in;
  in.open("../"+dat);
  assert (in.is_open());

  string line;

  while(getline(in, line)){
    stringstream sstr(line);
    string word;
    string value;

    sstr>>word;
    if (word[0]=='#') continue;
    sstr>>value;

    if(word.size()>0 && value.size()>0){
      name_to_value[word]= stod(value);
    }
  }


#define find(x)    \
  if (name_to_value.find(#x) != name_to_value.end()) {\
    x = name_to_value[#x];  \
    cout<< #x << "<-" << name_to_value[#x]<<endl; \
  } else { \
    cout<<"Warning, "<<#x<<" was not found in input.dat. its default value is "<<x<<endl;\
  }


  cout<<endl;
  cout<<"Initialize Parameters from sys_params.dat:"<<endl;
  cout<<endl;
  //List here all values which have to be initialized per file
  cout<<"Maximal Timestep:"<<endl;
  find(t_max);
  cout<<"Maximal Step for planning ahead:"<<endl;
  find(max_minute);
  cout<<"Maximal production step:"<<endl;
  find(max_prod_status);
  cout<<"Timestep for starting output:"<<endl;
  find(out_start);
}
