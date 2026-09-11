#ifndef VIGENERE_H
#define VIGENERE_H

#include <string>

using namespace std;

string vigenere_decrypt(const string& ciphertext, const string& key);
string vigenere_encrypt(const string& plaintext, const string& key);

bool verify(const string& originalCiphertext,
            const string& plaintext,
            const string& key);

#endif