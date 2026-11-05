
import random
import string
import time


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


# ==========================================
# PART B: PREDICTABLE RESET TOKEN
# ==========================================

def generate_reset_token(timestamp):

    rng = random.Random(timestamp)

    token = bytes(
        rng.getrandbits(8) for _ in range(16)
    )

    return token


def part_b():

    print("\n========== PART B ==========")

    # Generate token using current Unix timestamp
    timestamp = int(time.time())

    token = generate_reset_token(timestamp)

    print("\nOriginal Timestamp:", timestamp)
    print("Generated Token:", token.hex())

    # Attacker searches within +/- 300 seconds
    start_time = timestamp - 300
    end_time = timestamp + 300

    recovered_timestamp = None
    candidates_tested = 0

    print("\n--- Timestamp Prediction Attack ---")
    print("Search Interval:", start_time, "to", end_time)

    for candidate in range(start_time, end_time + 1):

        candidates_tested += 1

        candidate_token = generate_reset_token(candidate)

        if candidate_token == token:
            recovered_timestamp = candidate
            break

    print("Candidates Tested:", candidates_tested)
    print("Recovered Timestamp:", recovered_timestamp)

    # Verify recovered timestamp
    if recovered_timestamp is not None:

        verification_token = generate_reset_token(
            recovered_timestamp
        )

        print("Regenerated Token:", verification_token.hex())

        print("Token Verification:",
              verification_token == token)


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    part_a()
    part_b()
