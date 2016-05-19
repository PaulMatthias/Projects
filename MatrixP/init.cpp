#include <iostream>
#include <string>
#include <vector>
#include "product.h"

using namespace std;

std::vector<product> init_products() {

std::vector<product> prodVec;

product product1("Stapler1", 0, "looking", "noone"); 
product product2("Stapler2", 0, "looking", "noone"); 
product product3("Stapler3", 0, "looking", "noone"); 

    prodVec.push_back(product1);
    prodVec.push_back(product2);
    prodVec.push_back(product3);

return prodVec;
}
