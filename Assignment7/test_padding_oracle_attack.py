import unittest

from Crypto.Random import get_random_bytes

from padding_oracle_attack import (
    encrypt_message,
    make_padding_oracle,
    padding_oracle_attack,
)


class PaddingOracleAttackTests(unittest.TestCase):
    def test_recovers_various_plaintexts(self):
        messages = [
            b"",
            b"Hello, world!",
            b"A" * 16,
            b"Padding oracle attacks need no key.",
            bytes(range(64)),
        ]

        for plaintext in messages:
            with self.subTest(plaintext_length=len(plaintext)):
                key = get_random_bytes(16)
                iv = get_random_bytes(16)
                ciphertext = encrypt_message(plaintext, key, iv)
                oracle = make_padding_oracle(key)

                recovered, query_count = padding_oracle_attack(
                    iv, ciphertext, oracle
                )

                self.assertEqual(recovered, plaintext)
                self.assertGreater(query_count, 0)


if __name__ == "__main__":
    unittest.main()
