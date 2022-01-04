#ifndef UTILS_H
#define UTILS_H

#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int edit_distance(const string &s1, const string &s2);

vector<string> read_file(const string &name);

void printResult(const vector<pair<string, int>> &result);


#endif
