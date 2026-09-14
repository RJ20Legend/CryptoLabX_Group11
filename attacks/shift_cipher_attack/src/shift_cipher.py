# Shift Cipher Implementation
# Assignment 4 - Cryptanalysis of Shift Cipher

def encrypt(text, key):
    """
    Encrypt plaintext using Shift Cipher.
    key: integer from 0 to 25
    """
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))

        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

        else:
            result += ch

    return result


def decrypt(text, key):
    """
    Decrypt ciphertext using Shift Cipher.
    """
    return encrypt(text, -key)


def main():
    print("===================================")
    print("       SHIFT CIPHER")
    print("===================================")

    choice = input("Enter E for Encryption or D for Decryption: ").upper()

    text = input("Enter text: ")
    key = int(input("Enter key (0-25): "))

    if key < 0 or key > 25:
        print("Error: Key must be between 0 and 25.")
        return

    if choice == "E":
        result = encrypt(text, key)
        print("\nEncrypted Text:", result)

    elif choice == "D":
        result = decrypt(text, key)
        print("\nDecrypted Text:", result)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
