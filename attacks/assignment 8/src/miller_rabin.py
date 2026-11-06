
import secrets
import time
from sympy import isprime

BIT_LENGTH = 512
ROUNDS = 40


# Miller-Rabin test using random bases
def miller_rabin(n, rounds):

    if n < 2:
        return False, []

    if n == 2 or n == 3:
        return True, []

    if n % 2 == 0:
        return False, []

    # Express n-1 as 2^s * d
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


# Verify using the same Miller-Rabin bases
def miller_rabin_with_bases(n, bases):

    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


# Generate an odd candidate of exactly the required bit length
def generate_candidate(bits):

    n = secrets.randbits(bits)

    n |= (1 << (bits - 1))
    n |= 1

    return n


# Generate a probable prime
def generate_prime(bits, rounds):

    candidates_tested = 0
    total_rounds = 0

    start_time = time.perf_counter()

    while True:

        candidate = generate_candidate(bits)
        candidates_tested += 1

        probable_prime, bases = miller_rabin(
            candidate, rounds
        )

        total_rounds += len(bases)

        if probable_prime and len(bases) == rounds:

            # Independent verification using SymPy
            if isprime(candidate):

                elapsed = time.perf_counter() - start_time

                return (
                    candidate,
                    candidates_tested,
                    bases,
                    elapsed,
                    total_rounds
                )


# Main program
if __name__ == "__main__":

    print("=" * 55)
    print("CRYPTOGRAPHIC PRIME GENERATION - MILLER RABIN")
    print("=" * 55)

    prime, count, bases, elapsed, total_rounds = generate_prime(
        BIT_LENGTH, ROUNDS
    )

    print("\n========== EXPERIMENTAL RESULTS ==========")

    print("Assigned bit length:", BIT_LENGTH)

    print("\nGenerated prime candidate:")
    print(prime)

    print("\nActual bit length:", prime.bit_length())

    print("Number of candidates tested:", count)

    print("Miller-Rabin rounds per candidate:", ROUNDS)

    print("Total Miller-Rabin rounds executed:", total_rounds)

    print("Total execution time: {:.6f} seconds".format(elapsed))

    print("\n========== VERIFICATION ==========")

    print("Exact bit length verified:",
          prime.bit_length() == BIT_LENGTH)

    print("Odd number verified:", prime % 2 == 1)

    print("Miller-Rabin verification:",
          miller_rabin_with_bases(prime, bases))

    print("Independent SymPy verification:", isprime(prime))

    print("\nBases used in final successful test:")

    for i, base in enumerate(bases, 1):
        print("Round", i, ":", base)

    print("\nPrime generation completed successfully!")

