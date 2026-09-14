#ifndef MONOALPHABETIC_H
#define MONOALPHABETIC_H

#include <string>
#include <vector>
#include <map>

using namespace std;

void encryptText(const string& plaintext, const string& key, string& ciphertext);

void frequency_analysis(const string& ciphertext);

void word_frequency_analysis(const string& ciphertext);

void pattern_analysis(const string& ciphertext);

string apply_substitution(const string& ciphertext,
                          const map<char, char>& substitution);

void display_partial_plaintext(const string& ciphertext,
                               const map<char, char>& substitution);

bool verify_solution(const string& plaintext,
                     const string& ciphertext,
                     const string& key);

string getPattern(const string& word);

#endif