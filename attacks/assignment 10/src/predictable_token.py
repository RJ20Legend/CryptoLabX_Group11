
import random
import time


# Generate a 16-byte token using MT19937
def generate_token(timestamp):
    rng = random.Random(timestamp)

    token = bytes(
        rng.getrandbits(8) for _ in range(16)
    )

    return token


def main():
    print("===== PREDICTABLE RESET TOKEN ATTACK =====")

    # Generate simulated reset token
    timestamp = int(time.time())

    token = generate_token(timestamp)

    print("\nToken Generation")
    print("Timestamp:", timestamp)
    print("Token (hex):", token.hex())

    # Attacker knows generation happened within +/- 300 seconds
    start = timestamp - 300
    end = timestamp + 300

    print("\n===== TOKEN PREDICTION ATTACK =====")
    print("Search interval:", start, "to", end)

    recovered_timestamp = None
    tested = 0

    # Test every possible timestamp
    for candidate in range(start, end + 1):
        tested += 1

        candidate_token = generate_token(candidate)

        if candidate_token == token:
            recovered_timestamp = candidate
            break

    print("Timestamps tested:", tested)

    if recovered_timestamp is not None:
        print("Recovered timestamp:", recovered_timestamp)

        # Verify recovered token
        verified_token = generate_token(recovered_timestamp)

        print("Regenerated token:", verified_token.hex())
        print("Token verification:",
              verified_token == token)
    else:
        print("No matching timestamp found.")


if __name__ == "__main__":
    main()

