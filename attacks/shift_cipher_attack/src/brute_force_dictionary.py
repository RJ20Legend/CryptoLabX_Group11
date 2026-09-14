# Brute Force + Dictionary Scoring Attack
# Assignment 4 - Shift Cipher Cryptanalysis

import os
import sys

# Allow importing shift_cipher.py from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import decrypt


def load_dictionary(dictionary_file):
    """
    Load English words from the dictionary file.
    """
    words = set()

    try:
        with open(dictionary_file, "r") as file:
            for line in file:
                word = line.strip().lower()

                if word:
                    words.add(word)

    except FileNotFoundError:
        print("Dictionary file not found!")
        return set()

    return words


def dictionary_score(text, dictionary):
    """
    Calculate dictionary score.

    Score = number of words in the decrypted
    text that are present in the English dictionary.
    """
    words = text.lower().split()

    score = 0

    for word in words:
        # Remove punctuation
        clean_word = ""

        for ch in word:
            if ch.isalpha():
                clean_word += ch

        if clean_word in dictionary:
            score += 1

    return score


def brute_force_attack(ciphertext, dictionary_file):
    """
    Try all 26 possible Shift Cipher keys
    and select the key with the highest
    dictionary score.
    """

    dictionary = load_dictionary(dictionary_file)

    if not dictionary:
        return None, "", 0

    best_key = 0
    best_text = ""
    best_score = -1

    print("\n========================================")
    print("   BRUTE FORCE + DICTIONARY ATTACK")
    print("========================================")

    print("\nCiphertext:", ciphertext)
    print("\nTrying all possible keys...\n")

    for key in range(26):

        decrypted_text = decrypt(ciphertext, key)

        score = dictionary_score(
            decrypted_text,
            dictionary
        )

        print(
            f"Key {key:2d} -> "
            f"Score: {score:2d} -> "
            f"{decrypted_text}"
        )

        if score > best_score:
            best_score = score
            best_key = key
            best_text = decrypted_text

    return best_key, best_text, best_score


def main():

    print("========================================")
    print("      SHIFT CIPHER DICTIONARY ATTACK")
    print("========================================")

    ciphertext = input("\nEnter ciphertext: ")

    # Find dictionary relative to project root
    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    dictionary_file = os.path.join(
        current_dir,
        "..",
        "dictionary",
        "english_words.txt"
    )

    best_key, best_text, best_score = brute_force_attack(
        ciphertext,
        dictionary_file
    )

    if best_key is None:
        return

    print("\n========================================")
    print("              RESULT")
    print("========================================")

    print("Predicted Key      :", best_key)
    print("Dictionary Score   :", best_score)
    print("Decrypted Text     :", best_text)


if __name__ == "__main__":
    main()
