#include <iostream>
#include <vector>
#include <string>

using namespace std;

class worker{
  public:
    worker(string nm, string stat, int sk1, int sk2, int ti1, int ti2, double eff, string wn):name(nm),status(stat),skill1(sk1),skill2(sk2),minute1(ti1), minute2(ti2), work_next(wn){
    }

    string name;
    string status;
    string work_next;
    unsigned int skill1;
    unsigned int skill2;
    unsigned int minute1;
    unsigned int minute2;
    double efficiency;


    //TODO remove all these functions
    string get_name(){
      return name;
    }

    void set_name(string x){
      name=x;
    }
    
    string get_status(){
      return status;
    }

    void set_status(string doing){
      status=doing;
    }

    unsigned int get_skill(){
      return skill1;
    }

    void set_skill(int sk){
      skill1=sk;
    }
    
    unsigned int get_minute(){
      return minute1;
    }

};
