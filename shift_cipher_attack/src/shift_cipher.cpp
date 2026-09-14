#include "shift_cipher.h"

#include <iostream>
#include <cctype>

using namespace std;

string encryptText(const string& text, int key) {

    string result;

    key = (key % 26 + 26) % 26;

    for (char ch : text) {

        if (isalpha(static_cast<unsigned char>(ch))) {

            char base = isupper(static_cast<unsigned char>(ch))
                        ? 'A'
                        : 'a';

            result += static_cast<char>(
                (ch - base + key) % 26 + base
            );
        }
        else {
            result += ch;
        }
    }

    return result;
}

string decryptText(const string& text, int key) {

    return encryptText(text, -key);
}

void bruteForce(const string& ciphertext) {

    cout << "\n========== BRUTE FORCE ATTACK ==========\n";

    for (int key = 0; key < 26; key++) {

        cout << "Key " << key << " : "
             << decryptText(ciphertext, key)
             << '\n';
    }
}