
import secrets
import time
from sympy import isprime


def generate_candidate(bits):
    """Generate a random odd integer of exactly the requested bit length."""
    candidate = secrets.randbits(bits)
    candidate |= (1 << (bits - 1))
    candidate |= 1
    return candidate


def miller_rabin(n, rounds=40):
    """Perform Miller-Rabin primality testing."""
    if n < 2:
        return False, []

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for p in small_primes:
        if n == p:
            return True, []
        if n % p == 0:
            return False, []

    # Express n - 1 as 2^s * d, where d is odd.
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    used_bases = []

    for _ in range(rounds):
        a = secrets.randbelow(n - 3) + 2
        used_bases.append(a)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False, used_bases

    return True, used_bases


def generate_prime(bits=512, rounds=40):
    """Generate a probable prime of the specified bit length."""

    candidates_tested = 0
    start_time = time.perf_counter()

    while True:
        candidate = generate_candidate(bits)
        candidates_tested += 1

        is_probable_prime, bases = miller_rabin(candidate, rounds)

        if is_probable_prime:
            execution_time = time.perf_counter() - start_time

            return {
                "prime": candidate,
                "bit_length": candidate.bit_length(),
                "candidates_tested": candidates_tested,
                "rounds": rounds,
                "bases": bases,
                "execution_time": execution_time
            }


def main():
    bits = 512
    rounds = 40

    print("Miller-Rabin Cryptographic Prime Generation")
    print("-" * 50)

    result = generate_prime(bits, rounds)

    prime = result["prime"]

    print("\nGenerated Prime:")
    print(prime)

    print("\nExperimental Results:")
    print("Assigned bit length:", bits)
    print("Actual bit length:", result["bit_length"])
    print("Candidates tested:", result["candidates_tested"])
    print("Miller-Rabin rounds:", result["rounds"])
    print("Execution time:", result["execution_time"], "seconds")

    print("\nVerification:")
    print("Exact bit length:", prime.bit_length() == bits)

    passed, verification_bases = miller_rabin(prime, rounds)
    print("Miller-Rabin verification:", passed)
    print("Independent SymPy verification:", isprime(prime))

    print("\nBases used for successful candidate:")
    for i, base in enumerate(result["bases"], 1):
        print(f"Round {i}: {base}")


if __name__ == "__main__":
    main()
