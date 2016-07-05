#include <iostream>
#include <string>
#include <vector>
#include "../h/worker.h"

using namespace std;

std::vector<worker> init_workers() {

std::vector<worker> workVec;

// init worker (Name, status, skillset, time for skillset)  TODO adjust time to individual skills
worker worker1("Tim", "free", 1, 5, "nothing"); 
worker worker2("Jan", "free", 2, 6, "nothing"); 
worker worker3("Mark", "free", 3, 7, "nothing"); 

    workVec.push_back(worker1);
    workVec.push_back(worker2);
    workVec.push_back(worker3);

return workVec;
}
