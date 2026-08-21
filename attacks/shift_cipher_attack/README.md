# Assignment 4 - Shift Cipher Cryptanalysis

## Purpose

The purpose of this assignment is to perform cryptanalysis of
the Shift Cipher using brute force, dictionary scoring and
Chi-Square analysis.

## Algorithms

### 1. Brute Force + Dictionary Scoring

All 26 possible Shift Cipher keys are tested. Each ciphertext
is decrypted using every key and the resulting plaintext is
compared with an English dictionary.

The key producing the highest dictionary score is selected.

### 2. Chi-Square Analysis

All 26 possible keys are tested. The letter frequency of each
decrypted text is compared with standard English letter
frequencies using the Chi-Square statistic.

The key having the lowest Chi-Square value is selected.

## Execution

Run the main program:

```bash
python3 attacks/shift_cipher_attack/src/main.py
