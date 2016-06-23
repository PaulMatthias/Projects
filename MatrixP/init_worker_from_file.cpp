#include <iostream>
#include <string>
#include <vector>
#include "worker.h"
#include "read_csv.cpp"

using namespace std;

std::vector<worker> init_workers_from_file() {

std::vector<worker> workVec;
//TODO put vectors in a matrix
std::vector<string> names;
std::vector<string> ap1;
std::vector<string> ap2;
std::vector<string> minute1;
std::vector<string> minute2;
std::vector<string> efficiency;
std::vector<string> separ;

// init worker (Name, status, skillset, time for skillset)  TODO adjust time to individual skills
read_csv(names, ap1, ap2, minute1, minute2, efficiency);

for (int i=0; i<names.size(); i++){
  worker workers(names[i], "free", stoi(ap1[i]), stoi(ap2[i]), stoi(minute1[i]), stoi(minute2[i]), stod(efficiency[i]), "nothing");
  workVec.push_back(workers);
}

#if 0
for (int i=0;i<workVec.size();i++){
  cout<<workVec[i].name<<" "<<workVec[i].skill1<<endl;

}
#endif
return workVec;
}
