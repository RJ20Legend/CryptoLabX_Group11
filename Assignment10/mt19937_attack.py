
import random
import string


# ==========================================
# PART A: MT19937 STREAM CIPHER
# ==========================================

def mt_stream_cipher(data, seed):
    rng = random.Random(seed)
    result = bytearray()

    for byte in data:
        key_byte = rng.getrandbits(8)
        result.append(byte ^ key_byte)

    return bytes(result)


def part_a():

    print("\n========== PART A ==========")

    # Basic encryption and decryption
    message = b"Cryptography Lab Assignment 10"
    seed = random.randint(0, 65535)

    ciphertext = mt_stream_cipher(message, seed)
    decrypted = mt_stream_cipher(ciphertext, seed)

    print("\nOriginal Message:", message.decode())
    print("Seed:", seed)
    print("Ciphertext (hex):", ciphertext.hex())
    print("Decrypted Message:", decrypted.decode())

    # Generate random prefix followed by 14 A's
    prefix_length = random.randint(5, 20)

    prefix = ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(prefix_length)
    )

    plaintext = (prefix + "A" * 14).encode()

    secret_seed = random.randint(0, 65535)

    encrypted = mt_stream_cipher(plaintext, secret_seed)

    print("\n--- Known Plaintext Attack ---")
    print("Ciphertext (hex):", encrypted.hex())
    print("Known plaintext: AAAAAAAAAAAAAA")
    print("Prefix length:", prefix_length)

    # Brute-force all 16-bit seeds
    recovered_seed = None
    recovered_plaintext = None

    known = b"A" * 14

    for candidate_seed in range(65536):

        decrypted_candidate = mt_stream_cipher(
            encrypted, candidate_seed
        )

        if known in decrypted_candidate:
            recovered_seed = candidate_seed
            recovered_plaintext = decrypted_candidate
            break

    print("\nRecovered Seed:", recovered_seed)

    if recovered_seed is not None:

        print("Recovered Plaintext:",
              recovered_plaintext.decode())

        print("Seed Correct:",
              recovered_seed == secret_seed)

        print("Known Sequence Found:",
              known in recovered_plaintext)

        verification = mt_stream_cipher(
            encrypted, recovered_seed
        )

        print("Full Decryption Verified:",
              verification == plaintext)


if __name__ == "__main__":
    part_a()
