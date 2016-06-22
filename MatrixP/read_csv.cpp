#include <iostream>
#include <fstream>
#include <assert.h>
#include <vector>
#include <typeinfo>
#include "parse.cpp"

using namespace std;

//std::vector<string> main() {
int main() {
    ifstream in;
    in.open("test.csv");
    assert(in.is_open());
    std::vector<string> names;
    std::vector<string> ap1;
    std::vector<string> ap2;
    std::vector<string> efficiency;
    std::vector<string> separ;
    const int MAXSIZE =100; //TODO figure out how big this size has to be
    char thisVal[MAXSIZE];
    int i=0;
    while(in.getline(thisVal,MAXSIZE)){
	string str(thisVal);
	separ=separate(thisVal);
	names.push_back(separ[0]);
	ap1.push_back(separ[1]);
	ap2.push_back(separ[2]);
	efficiency.push_back(separ[3]);
	i++;
    }
    // in.getline(thisVal,MAXSIZE,'\n')) {

    in.close();
    for (string cp: names) cout<<cp<<endl;
    for (string cp: ap1) cout<<cp<<endl;
    for (string cp: ap2) cout<<cp<<endl;
    for (string cp: efficiency) cout<<cp<<endl;
    //return values;
    return 0;
}
