#pragma once
#include <string>
#include <vector>

void read_csv(std::vector<std::string>& names, std::vector<std::string>& ap1,std::vector<std::string>& ap2,\
	      std::vector<std::string>& minute1, std::vector<std::string>& minute2, std::vector<std::string>& efficiency) ;

void separation(std::string line, std::vector<std::string>& vect);
