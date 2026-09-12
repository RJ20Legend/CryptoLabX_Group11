#include "vigenere.h"

using namespace std;

string vigenere_decrypt(const string& ciphertext, const string& key)
{
    string plaintext;
    int keyIndex = 0;

    for (char ch : ciphertext)
    {
        int cipherValue = ch - 'A';

        int keyValue = key[keyIndex % key.length()] - 'A';

        int plainValue = (cipherValue - keyValue + 26) % 26;

        plaintext += char('A' + plainValue);

        keyIndex++;
    }

    return plaintext;
}

string vigenere_encrypt(
    const string& plaintext,
    const string& key)
{
    string ciphertext;

    for (int i = 0; i < plaintext.length(); i++)
    {
        int plainValue = plaintext[i] - 'A';

        int keyValue =
            key[i % key.length()] - 'A';

        int cipherValue =
            (plainValue + keyValue) % 26;

        ciphertext += char('A' + cipherValue);
    }

    return ciphertext;
}

bool verify(
    const string& originalCiphertext,
    const string& plaintext,
    const string& key)
{
    string regeneratedCiphertext =
        vigenere_encrypt(plaintext, key);

    return regeneratedCiphertext == originalCiphertext;
}