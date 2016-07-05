#include <iostream>
#include <vector>
#include <string>

using namespace std;

class product{  
  public:
   
    product(const string nm, int prod_stat, string stat, string wb, string wbn):name(nm),prod_status(prod_stat),status(stat),worked_by(wb), worked_by_next(wbn){
   }

    string name;
    unsigned int prod_status;
    string status;
    string worked_by;
    string worked_by_next;

    string get_name(){
      return name;
    }

    void set_name(string x){
      name=x;
    }
    
    unsigned int get_prod_status(){
      return prod_status;
    }

    void set_prod_status(){
      prod_status+=1;
    }
    
};
