#ifndef BRUTE_FORCE_DICTIONARY_H
#define BRUTE_FORCE_DICTIONARY_H

#include <string>
#include <unordered_set>

// Load English words from dictionary file
std::unordered_set<std::string>
loadDictionary(const std::string& filename);

// Calculate number of valid dictionary words
int dictionaryScore(
    const std::string& plaintext,
    const std::unordered_set<std::string>& dictionary
);

// Perform dictionary-based cryptanalysis
int dictionaryAttack(
    const std::string& ciphertext,
    const std::unordered_set<std::string>& dictionary,
    std::string& bestPlaintext
);

#endif