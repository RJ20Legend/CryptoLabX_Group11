#ifndef CHI_SQUARE_ATTACK_H
#define CHI_SQUARE_ATTACK_H

#include <string>

// Calculate Chi-Square score
double calculateChiSquare(const std::string& text);

// Perform Chi-Square cryptanalysis
int chiSquareAttack(
    const std::string& ciphertext,
    std::string& bestPlaintext
);

#endif