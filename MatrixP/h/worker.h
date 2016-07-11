#pragma once

#ifndef _WORKER_INCLUDE_
#define _WORKER_INCLUDE_

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class worker{
  public:
    worker(string nm, string stat, int sk1, int sk2, int ti1, int ti2, double eff, string wn, int csu):name(nm),status(stat),skill1(sk1),skill2(sk2),minute1(ti1), minute2(ti2), efficiency(eff), work_next(wn), current_skill_used(csu){
    }

    string name;
    string status;
    unsigned int skill1;
    unsigned int skill2;
    unsigned int minute1;
    unsigned int minute2;
    double efficiency;
    string work_next;
    int current_skill_used;


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

#endif
