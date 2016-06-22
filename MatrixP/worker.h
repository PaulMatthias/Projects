#include <iostream>
#include <vector>
#include <string>

using namespace std;

class worker{
  public:
    worker(string nm, string stat, int sk, int ti, string wn):name(nm),status(stat),skill(sk),minute(ti), work_next(wn){
    }

    string name;
    string status;
    string work_next;
    unsigned int skill;
    unsigned int minute;

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
      return skill;
    }

    void set_skill(int sk){
      skill=sk;
    }
    
    unsigned int get_minute(){
      return minute;
    }

};
