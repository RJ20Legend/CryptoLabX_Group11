#include "vigenere.h"
#include <cctype>

using namespace std;

string vigenere_encrypt(const string& plaintext, const string& key)
{
    string ciphertext;
    int keyIndex = 0;

    for (char ch : plaintext)
    {
        if (isalpha(ch))
        {
            char p = toupper(ch);
            char k = toupper(key[keyIndex % key.length()]);

            char encrypted = 'A' + (p - 'A' + k - 'A') % 26;

            ciphertext += encrypted;
            keyIndex++;
        }
    }

    return ciphertext;
}