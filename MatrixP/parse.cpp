#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

std::vector<string> separate(string line)
{
    std::vector<string> vect;
    std::string word;

    std::stringstream ss(line);

    while (getline(ss,word, ','))
    {
      vect.push_back(word);
    }

    return vect;
}
