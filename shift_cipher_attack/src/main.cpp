#include <bits/stdc++.h>
#include "shift_cipher.h"
#include "brute_force_dictionary.h"
#include "chi_square_attack.h"
using namespace std;

string encryptText(const string& text, int key);
string decryptText(const string& text, int key);
void bruteForce(const string& ciphertext);


unordered_set<string> loadDictionary(const string& filename);
int dictionaryScore(
    const string& ciphertext,
    const unordered_set<string>& dictionary,
    string &bestPlaintext);

double calculateChiSquare(const string& text);

int chiSquareAttack(
    const string& ciphertext,
    string& bestPlaintext
);

int main() {

    cout << "=============================================\n";
    cout << "       SHIFT CIPHER CRYPTANALYSIS\n";
    cout << "=============================================\n";

    string plaintext;
    int actualKey;

    cout << "\nEnter plaintext: ";
    getline(cin, plaintext);

    cout << "Enter key (0-25): ";
    cin >> actualKey;

    actualKey = (actualKey % 26 + 26) % 26;

    // Encrypt
    string ciphertext = encryptText(plaintext, actualKey);

    cout << "\n---------------------------------------------\n";
    cout << "Original Plaintext : " << plaintext << '\n';
    cout << "Actual Key         : " << actualKey << '\n';
    cout << "Ciphertext         : " << ciphertext << '\n';
    cout << "---------------------------------------------\n";


    // =====================================================
    // BRUTE FORCE
    // =====================================================

    bruteForce(ciphertext);


    // =====================================================
    // DICTIONARY ATTACK
    // =====================================================

    cout << "\n=============================================\n";
    cout << "        DICTIONARY SCORING ATTACK\n";
    cout << "=============================================\n";

    unordered_set<string> dictionary =
        loadDictionary("../dictionary/english_words.txt");

    if (dictionary.empty()) {
        cout << "\nDictionary could not be loaded.\n";
        cout << "Make sure english_words.txt exists in:\n";
        cout << "../dictionary/english_words.txt\n";
    }

    string dictionaryPlaintext;

    int dictionaryKey =
        dictionaryAttack(
            ciphertext,
            dictionary,
            dictionaryPlaintext
        );

    cout << "\nDictionary Predicted Key : "
         << dictionaryKey << '\n';

    cout << "Dictionary Plaintext     : "
         << dictionaryPlaintext << '\n';


    // =====================================================
    // CHI-SQUARE ATTACK
    // =====================================================

    cout << "\n=============================================\n";
    cout << "          CHI-SQUARE ATTACK\n";
    cout << "=============================================\n";

    string chiSquarePlaintext;

    int chiSquareKey =
        chiSquareAttack(
            ciphertext,
            chiSquarePlaintext
        );

    cout << "\nChi-Square Predicted Key : "
         << chiSquareKey << '\n';

    cout << "Chi-Square Plaintext     : "
         << chiSquarePlaintext << '\n';


    // =====================================================
    // FINAL COMPARISON
    // =====================================================

    cout << "\n=============================================\n";
    cout << "             FINAL RESULTS\n";
    cout << "=============================================\n";

    cout << left
         << setw(20) << "Method"
         << setw(15) << "Predicted Key"
         << setw(15) << "Correct?"
         << '\n';

    cout << "---------------------------------------------\n";

    cout << left
         << setw(20) << "Dictionary"
         << setw(15) << dictionaryKey
         << setw(15)
         << (dictionaryKey == actualKey ? "Yes" : "No")
         << '\n';

    cout << left
         << setw(20) << "Chi-Square"
         << setw(15) << chiSquareKey
         << setw(15)
         << (chiSquareKey == actualKey ? "Yes" : "No")
         << '\n';

    cout << "=============================================\n";

    return 0;
}