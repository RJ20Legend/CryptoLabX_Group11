# Chi-Square Cryptanalysis of Shift Cipher
# Assignment 4

import os
import sys
import math

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import decrypt


# Standard English letter frequencies
ENGLISH_FREQUENCIES = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02360,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}


def calculate_letter_frequency(text):
    """
    Count occurrences of each alphabet letter.
    """

    counts = {letter: 0 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    total = 0

    for ch in text.upper():

        if ch.isalpha():

            counts[ch] += 1
            total += 1

    return counts, total


def chi_square_score(text):
    """
    Calculate Chi-Square statistic.

    Lower score means the text is more similar
    to normal English.
    """

    counts, total = calculate_letter_frequency(text)

    if total == 0:
        return float('inf')

    score = 0.0

    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':

        observed = counts[letter]

        expected = (
            ENGLISH_FREQUENCIES[letter] * total
        )

        if expected > 0:

            score += (
                (observed - expected) ** 2
            ) / expected

    return score


def chi_square_attack(ciphertext):
    """
    Try all 26 keys and select the key
    having the lowest Chi-Square score.
    """

    best_key = 0
    best_text = ""
    best_score = float('inf')

    print("\n========================================")
    print("       CHI-SQUARE CRYPTANALYSIS")
    print("========================================")

    print("\nCiphertext:", ciphertext)
    print("\nTrying all possible keys...\n")

    for key in range(26):

        decrypted_text = decrypt(ciphertext, key)

        score = chi_square_score(decrypted_text)

        print(
            f"Key {key:2d} -> "
            f"Chi-Square: {score:10.4f} -> "
            f"{decrypted_text}"
        )

        if score < best_score:

            best_score = score
            best_key = key
            best_text = decrypted_text

    return best_key, best_text, best_score


def main():

    print("========================================")
    print("       SHIFT CIPHER CHI-SQUARE ATTACK")
    print("========================================")

    ciphertext = input("\nEnter ciphertext: ")

    key, text, score = chi_square_attack(ciphertext)

    print("\n========================================")
    print("                RESULT")
    print("========================================")

    print("Predicted Key     :", key)
    print("Chi-Square Score  :", round(score, 4))
    print("Decrypted Text    :", text)


if __name__ == "__main__":
    main()
