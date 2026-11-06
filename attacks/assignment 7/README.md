# Assignment 7: Padding Oracle Attack

## Aim
To understand and demonstrate how a Padding Oracle Attack can recover plaintext from AES-CBC encrypted ciphertext without knowing the encryption key.

## Objectives
- Understand AES-CBC encryption.
- Understand PKCS#7 padding.
- Implement a padding oracle.
- Recover plaintext bytes from right to left.
- Calculate the total number of oracle queries.
- Study prevention techniques.

## Technologies Used
- Python 3
- PyCryptodome
- AES-CBC

## Theory

**AES-CBC:** AES-CBC is a block cipher mode in which each plaintext block is XORed with the previous ciphertext block before encryption.

**PKCS#7 Padding:** Padding bytes are added to make plaintext length a multiple of the AES block size (16 bytes).

**Padding Oracle:** It is a function that indicates whether decrypted ciphertext has valid PKCS#7 padding.

## Attack Methodology
1. Encrypt the original plaintext using AES-CBC.
2. Create a padding oracle.
3. Modify the previous ciphertext block.
4. Send modified ciphertext to the oracle.
5. Recover plaintext bytes from right to left.
6. Repeat for all ciphertext blocks.
7. Remove padding to obtain the original plaintext.

## Experimental Results

**Original Plaintext:**

Padding Oracle Attack recovers plaintext without knowing the AES key.

**Recovered Plaintext:**

Padding Oracle Attack recovers plaintext without knowing the AES key.

**Total Oracle Queries:** 10289

**Result:** Plaintext successfully recovered.

## Security Recommendations
1. Use authenticated encryption such as AES-GCM.
2. Verify authentication before processing decrypted data.
3. Avoid distinguishable padding error messages.
4. Use constant-time cryptographic operations.

## Conclusion
The experiment demonstrates that a Padding Oracle Attack can recover plaintext from AES-CBC ciphertext without knowing the encryption key. It highlights the importance of authenticated encryption and secure error handling.
