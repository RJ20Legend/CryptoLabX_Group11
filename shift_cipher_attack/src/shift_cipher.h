#ifndef SHIFT_CIPHER_H
#define SHIFT_CIPHER_H

#include <string>

std::string encryptText(const std::string& text, int key);

std::string decryptText(const std::string& text, int key);

void bruteForce(const std::string& ciphertext);

#endif