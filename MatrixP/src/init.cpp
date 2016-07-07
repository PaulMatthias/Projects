#include <iostream>
#include <string>
#include <vector>
#include "../h/product.h"
#include "../h/worker.h"

using namespace std;

std::vector<product> init_products() {

std::vector<product> prodVec;

product product1("Stapler1", 0, "looking", "noone","noone"); 
product product2("Stapler2", 0, "looking", "noone","noone"); 
product product3("Stapler3", 0, "looking", "noone","noone"); 

    prodVec.push_back(product1);
    prodVec.push_back(product2);
    prodVec.push_back(product3);

return prodVec;
}


//INITializes one new product
void init_product(std::vector<product>& list_of_products, worker& worker) {

    int prod_count = list_of_products.size();
    product prod("Stapler"+to_string(prod_count), 1, "engaged", worker.name, "noone");
    list_of_products.push_back(prod);
    worker.status="occupied";
    worker.work_next="nothing";
    worker.current_skill_used=1;

}
