#ifndef ANALYSIS_H
#define ANALYSIS_H

#include <string>
#include <vector>

using namespace std;

string clean_ciphertext(const string& ciphertext);

vector<pair<string, vector<int>>> find_repeated_patterns(
    const string& ciphertext);

vector<pair<string, vector<int>>> calculate_distances(
    const vector<pair<string, vector<int>>>& patterns);

vector<pair<int, vector<int>>> find_factors(
    const vector<pair<string, vector<int>>>& distances);

vector<int> kasiski_analysis(
    const vector<pair<int, vector<int>>>& factors);

vector<string> split_into_groups(
    const string& ciphertext,
    int keyLength);
vector<vector<int>> frequency_analysis(
    const vector<string>& groups);
int find_shift(const vector<int>& frequency);

string find_key(const vector<vector<int>>& frequencies);

#endif