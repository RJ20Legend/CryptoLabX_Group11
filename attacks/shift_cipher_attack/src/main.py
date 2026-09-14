# Main Program
# Assignment 4 - Shift Cipher Cryptanalysis

import os
import sys

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

sys.path.append(CURRENT_DIR)

from shift_cipher import encrypt, decrypt
from brute_force_dictionary import brute_force_attack
from chi_square_attack import chi_square_attack


def main():

    while True:

        print("\n========================================")
        print("      SHIFT CIPHER CRYPTANALYSIS")
        print("========================================")

        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force + Dictionary")
        print("4. Chi-Square Analysis")
        print("5. Run Both Attacks")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            text = input("Enter plaintext: ")
            key = int(input("Enter key (0-25): "))

            print(
                "Encrypted Text:",
                encrypt(text, key)
            )

        elif choice == "2":

            text = input("Enter ciphertext: ")
            key = int(input("Enter key (0-25): "))

            print(
                "Decrypted Text:",
                decrypt(text, key)
            )

        elif choice == "3":

            ciphertext = input("Enter ciphertext: ")

            dictionary_file = os.path.join(
                CURRENT_DIR,
                "..",
                "dictionary",
                "english_words.txt"
            )

            key, text, score = brute_force_attack(
                ciphertext,
                dictionary_file
            )

            print("\nPredicted Key:", key)
            print("Dictionary Score:", score)
            print("Decrypted Text:", text)

        elif choice == "4":

            ciphertext = input("Enter ciphertext: ")

            key, text, score = chi_square_attack(
                ciphertext
            )

            print("\nPredicted Key:", key)
            print("Chi-Square Score:", round(score, 4))
            print("Decrypted Text:", text)

        elif choice == "5":

            ciphertext = input("Enter ciphertext: ")

            dictionary_file = os.path.join(
                CURRENT_DIR,
                "..",
                "dictionary",
                "english_words.txt"
            )

            print("\n===== DICTIONARY ATTACK =====")

            d_key, d_text, d_score = brute_force_attack(
                ciphertext,
                dictionary_file
            )

            print("\nDictionary Predicted Key:", d_key)
            print("Dictionary Decryption:", d_text)

            print("\n===== CHI-SQUARE ATTACK =====")

            c_key, c_text, c_score = chi_square_attack(
                ciphertext
            )

            print("\nChi-Square Predicted Key:", c_key)
            print("Chi-Square Decryption:", c_text)

            print("\n========================================")
            print("              COMPARISON")
            print("========================================")

            print("Dictionary Key :", d_key)
            print("Chi-Square Key :", c_key)

            if d_key == c_key:
                print("Both attacks predicted the same key.")
            else:
                print("The attacks predicted different keys.")

        elif choice == "6":

            print("\nExiting...")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()
