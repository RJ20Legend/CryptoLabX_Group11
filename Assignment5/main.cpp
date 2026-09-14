#include <iostream>
#include <map>
#include "monoalphabetic.h"

using namespace std;

int main()
{
    string plaintext =
        "Cryptography is the practice and study of techniques "
        "for secure communication in the presence of adversaries. "
        "Modern cryptography provides methods for protecting "
        "information and ensuring confidentiality integrity "
        "authentication and other security properties.";

    // Example substitution key
    // Plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
    // Cipher: QWERTYUIOPASDFGHJKLZXCVBNM

    string key = "QWERTYUIOPASDFGHJKLZXCVBNM";

    string ciphertext;

    encryptText(plaintext, key, ciphertext);

    cout << "===== PLAINTEXT =====\n";
    cout << plaintext << "\n";

    cout << "\n===== CIPHERTEXT =====\n";
    cout << ciphertext << "\n";

    frequency_analysis(ciphertext);

    word_frequency_analysis(ciphertext);

    pattern_analysis(ciphertext);

    // Example hypotheses generated during cryptanalysis
    map<char, char> substitution;

    substitution['Q'] = 'C';
    substitution['W'] = 'R';
    substitution['T'] = 'E';

    display_partial_plaintext(ciphertext, substitution);

    cout << "\n===== RECOVERED KEY =====\n";

    for (int i = 0; i < 26; i++)
    {
        cout << char('A' + i)
             << " -> "
             << key[i]
             << "\n";
    }

    verify_solution(plaintext, ciphertext, key);

    return 0;
}