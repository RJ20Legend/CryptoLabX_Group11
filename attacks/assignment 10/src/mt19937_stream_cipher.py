
import random
import secrets
import string


# Generate one 8-bit keystream value per byte
def generate_keystream(seed, length):
    rng = random.Random(seed)
    return bytes(rng.getrandbits(8) for _ in range(length))


# Same function performs both encryption and decryption
def xor_cipher(data, seed):
    keystream = generate_keystream(seed, len(data))
    return bytes(a ^ b for a, b in zip(data, keystream))


# Brute-force all possible 16-bit seeds
def recover_seed(ciphertext, known_text):
    known = known_text.encode()
    matches = []

    for seed in range(65536):
        keystream = generate_keystream(seed, len(ciphertext))
        plaintext = bytes(a ^ b for a, b in zip(ciphertext, keystream))

        # Search for known plaintext at any position
        if known in plaintext:
            matches.append((seed, plaintext))

    return matches


def main():
    print("===== MT19937 STREAM CIPHER =====")

    # Basic encryption and decryption test
    test_message = b"Hello Cryptography"
    test_seed = 12345

    encrypted = xor_cipher(test_message, test_seed)
    decrypted = xor_cipher(encrypted, test_seed)

    print("\nEncryption/Decryption Test")
    print("Original :", test_message.decode())
    print("Ciphertext:", encrypted.hex())
    print("Decrypted:", decrypted.decode())

    # Generate random prefix followed by 14 A's
    prefix_length = secrets.randbelow(16) + 5
    characters = string.ascii_letters + string.digits + string.punctuation

    prefix = ''.join(
        secrets.choice(characters) for _ in range(prefix_length)
    )

    plaintext = (prefix + "A" * 14).encode()

    # Select random 16-bit seed
    original_seed = secrets.randbelow(65536)

    ciphertext = xor_cipher(plaintext, original_seed)

    print("\n===== SEED RECOVERY ATTACK =====")
    print("Original plaintext:", plaintext.decode())
    print("Original seed:", original_seed)
    print("Ciphertext (hex):", ciphertext.hex())

    # Attacker knows only 14 consecutive A's
    matches = recover_seed(ciphertext, "A" * 14)

    if matches:
        recovered_seed, recovered_plaintext = matches[0]

        print("\nRecovered seed:", recovered_seed)
        print("Recovered plaintext:", recovered_plaintext.decode())

        # Verify complete decryption
        verification = xor_cipher(ciphertext, recovered_seed)

        print("Full plaintext verification:",
              verification == plaintext)
        print("Known sequence found:",
              "A" * 14 in verification.decode())

        print("Total matching seeds:", len(matches))
    else:
        print("No matching seed found.")


if __name__ == "__main__":
    main()

