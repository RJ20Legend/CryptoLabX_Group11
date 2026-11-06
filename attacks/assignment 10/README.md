
# Assignment 10: MT19937 Stream Cipher and Predictable Token Attack

## Objective
To understand why MT19937 is unsuitable for cryptographic applications by implementing a stream cipher, recovering a weak seed, and predicting timestamp-based reset tokens.

## Part A: MT19937 Stream Cipher

MT19937 is a pseudorandom number generator that produces a sequence of numbers using the Mersenne Twister algorithm.

It has a period of 2^19937 - 1 and provides good statistical randomness, but it is not cryptographically secure.

### Encryption and Decryption
- A keystream byte is generated for every plaintext byte.
- Encryption is performed using XOR between plaintext and keystream.
- Decryption uses the same XOR operation with the same seed.

### Known Plaintext Attack
If plaintext is known, the attacker can calculate the keystream:

Keystream = Ciphertext XOR Plaintext

The attacker tries all possible 16-bit seeds.

Search space = 2^16 = 65,536 seeds.

The correct seed is identified when the decrypted plaintext contains 14 consecutive A characters.

## Part B: Predictable Reset Token Attack

In this experiment, MT19937 is seeded using the current Unix timestamp.

A 16-byte reset token is generated using 16 consecutive 8-bit outputs.

### Attack
An attacker who knows the approximate token generation time can test timestamps within a specified interval.

For an interval of T-300 to T+300:

Total candidates = 601.

Each candidate timestamp is used to generate a token. The generated token is compared with the observed token.

If both match, the timestamp has been recovered.

## Why MT19937 Is Not Cryptographically Secure

1. Its internal state can be reconstructed from sufficient output.
2. Its output is deterministic for a given seed.
3. It is vulnerable to prediction attacks.
4. It is not designed to resist attackers.

## Why Timestamp Seeding Is Vulnerable

Unix timestamps are predictable and have a limited search space when the generation time is approximately known. An attacker can test possible timestamps and reproduce the token.

## Pseudocode

### Seed Recovery

1. Read ciphertext.
2. Set known plaintext to 14 consecutive A characters.
3. For every seed from 0 to 65535:
   - Generate the keystream.
   - XOR it with ciphertext.
   - Check whether the known sequence exists.
4. Return the matching seed.
5. Decrypt the complete ciphertext and verify.

### Token Prediction

1. Observe the reset token.
2. Obtain the approximate generation time T.
3. Set search interval to T-300 through T+300.
4. Generate a candidate token for every timestamp.
5. Compare candidate token with observed token.
6. Report the matching timestamp.
7. Regenerate the token to verify.

## Conclusion

MT19937 is suitable for statistical simulations but not for security-sensitive applications. Weak seeds and predictable initialization allow attackers to recover encryption seeds and predict reset tokens. Cryptographic applications should use a CSPRNG instead.

