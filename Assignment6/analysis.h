#ifndef ANALYSIS_H
#define ANALYSIS_H

#include <string>
#include <vector>

using namespace std;

string clean_ciphertext(const string& ciphertext);

vector<pair<string, vector<int>>> find_repeated_patterns(const string& ciphertext);

#endif