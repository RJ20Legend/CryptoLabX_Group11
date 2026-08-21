#include "brute_force_dictionary.h"
#include "shift_cipher.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <cctype>

using namespace std;

unordered_set<string> loadDictionary(const string& filename) {

    unordered_set<string> dictionary;

    ifstream file(filename);

    if (!file.is_open()) {

        cerr << "Error: Could not open dictionary file: "
             << filename << '\n';

        return dictionary;
    }

    string word;

    while (file >> word) {

        string cleaned;

        for (char ch : word) {

            if (isalpha(static_cast<unsigned char>(ch))) {

                cleaned += static_cast<char>(
                    tolower(static_cast<unsigned char>(ch))
                );
            }
        }

        if (!cleaned.empty()) {

            dictionary.insert(cleaned);
        }
    }

    file.close();

    return dictionary;
}


int dictionaryScore(
    const string& plaintext,
    const unordered_set<string>& dictionary
) {

    stringstream ss(plaintext);

    string word;

    int score = 0;

    while (ss >> word) {

        string cleaned;

        for (char ch : word) {

            if (isalpha(static_cast<unsigned char>(ch))) {

                cleaned += static_cast<char>(
                    tolower(static_cast<unsigned char>(ch))
                );
            }
        }

        if (!cleaned.empty() &&
            dictionary.find(cleaned) != dictionary.end()) {

            score++;
        }
    }

    return score;
}


int dictionaryAttack(
    const string& ciphertext,
    const unordered_set<string>& dictionary,
    string& bestPlaintext
) {

    int bestKey = 0;

    int bestScore = -1;

    cout << "\n========== DICTIONARY SCORING ATTACK ==========\n";

    for (int key = 0; key < 26; key++) {

        string plaintext = decryptText(ciphertext, key);

        int score = dictionaryScore(
            plaintext,
            dictionary
        );

        cout << "Key " << key
             << " | Score = " << score
             << " | " << plaintext
             << '\n';

        if (score > bestScore) {

            bestScore = score;

            bestKey = key;

            bestPlaintext = plaintext;
        }
    }

    return bestKey;
}