#include "chi_square_attack.h"
#include "shift_cipher.h"

#include <iostream>
#include <cmath>
#include <cctype>
#include <limits>

using namespace std;


// Expected English letter frequencies
const double ENGLISH_FREQUENCY[26] = {

    8.167,
    1.492,
    2.782,
    4.253,
    12.702,
    2.228,
    2.015,
    6.094,
    6.966,
    0.153,
    0.772,
    4.025,
    2.406,
    6.749,
    7.507,
    1.929,
    0.095,
    5.987,
    6.327,
    9.056,
    2.758,
    0.978,
    2.360,
    0.150,
    1.974,
    0.074
};


double calculateChiSquare(const string& text) {

    int observed[26] = {0};

    int totalLetters = 0;

    for (char ch : text) {

        if (isalpha(static_cast<unsigned char>(ch))) {

            char lower =
                static_cast<char>(
                    tolower(static_cast<unsigned char>(ch))
                );

            observed[lower - 'a']++;

            totalLetters++;
        }
    }

    if (totalLetters == 0) {

        return numeric_limits<double>::max();
    }

    double chiSquare = 0.0;

    for (int i = 0; i < 26; i++) {

        double expected =
            totalLetters *
            ENGLISH_FREQUENCY[i] /
            100.0;

        if (expected > 0) {

            double difference =
                observed[i] - expected;

            chiSquare +=
                (difference * difference) /
                expected;
        }
    }

    return chiSquare;
}


int chiSquareAttack(
    const string& ciphertext,
    string& bestPlaintext
) {

    int bestKey = 0;

    double bestScore =
        numeric_limits<double>::max();

    cout << "\n========== CHI-SQUARE ATTACK ==========\n";

    for (int key = 0; key < 26; key++) {

        string plaintext =
            decryptText(ciphertext, key);

        double score =
            calculateChiSquare(plaintext);

        cout << "Key " << key
             << " | Chi-Square = "
             << score
             << " | " << plaintext
             << '\n';

        if (score < bestScore) {

            bestScore = score;

            bestKey = key;

            bestPlaintext = plaintext;
        }
    }

    return bestKey;
}