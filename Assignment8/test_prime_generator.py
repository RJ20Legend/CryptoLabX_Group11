
import unittest
from sympy import isprime

from prime_generator import generate_candidate, miller_rabin, generate_prime


class TestPrimeGenerator(unittest.TestCase):

    def test_candidate_bit_length(self):
        candidate = generate_candidate(512)
        self.assertEqual(candidate.bit_length(), 512)
        self.assertEqual(candidate % 2, 1)

    def test_known_primes(self):
        primes = [2, 3, 5, 7, 11, 97, 101, 997]

        for number in primes:
            result, _ = miller_rabin(number)
            self.assertTrue(result)

    def test_composite_numbers(self):
        composites = [4, 9, 15, 21, 25, 100, 561, 1105]

        for number in composites:
            result, _ = miller_rabin(number)
            self.assertFalse(result)

    def test_generated_prime(self):
        result = generate_prime(512, 40)
        prime = result["prime"]

        self.assertEqual(prime.bit_length(), 512)
        self.assertEqual(prime % 2, 1)
        self.assertTrue(miller_rabin(prime, 40)[0])
        self.assertTrue(isprime(prime))

    def test_invalid_input(self):
        result, _ = miller_rabin(-7)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
