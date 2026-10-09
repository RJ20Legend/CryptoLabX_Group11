"""
Assignment 8: AES-CBC Padding Oracle Attack demonstration.

Install dependency:
    python -m pip install pycryptodome

Run:
    python Assignment8/padding_oracle_attack.py

The attack function receives only the IV, ciphertext, and a Boolean oracle.
It never receives the AES key. The key is used only by the local demonstration
encryption setup and the oracle closure.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = AES.block_size  # AES block size is 16 bytes.


def pkcs7_pad(data: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len


def pkcs7_unpad(data: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    if not data or len(data) % block_size:
        raise ValueError("Invalid padded data length")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > block_size:
        raise ValueError("Invalid PKCS#7 padding")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid PKCS#7 padding")
    return data[:-pad_len]


def encrypt_message(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return cipher.encrypt(pkcs7_pad(plaintext))


def make_padding_oracle(key: bytes):
    """Create an oracle that returns only whether decrypted PKCS#7 padding is valid."""
    def padding_oracle(iv: bytes, ciphertext: bytes) -> bool:
        if len(iv) != BLOCK_SIZE or not ciphertext or len(ciphertext) % BLOCK_SIZE:
            return False
        try:
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            plaintext_with_padding = cipher.decrypt(ciphertext)
            pkcs7_unpad(plaintext_with_padding)
            return True
        except (ValueError, TypeError):
            return False

    return padding_oracle


def padding_oracle_attack(iv: bytes, ciphertext: bytes, oracle):
    """
    Recover plaintext without the key.

    Returns:
        (plaintext_bytes, oracle_query_count)
    """
    if len(iv) != BLOCK_SIZE:
        raise ValueError("IV must be exactly 16 bytes")
    if not ciphertext or len(ciphertext) % BLOCK_SIZE:
        raise ValueError("Ciphertext must contain complete AES blocks")

    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]
    recovered = bytearray()
    query_count = 0
    previous = iv

    for target_block in blocks:
        # intermediate = AES_decrypt(target_block), recovered one byte at a time.
        intermediate = bytearray(BLOCK_SIZE)
        crafted_previous = bytearray(previous)

        for position in range(BLOCK_SIZE - 1, -1, -1):
            desired_padding = BLOCK_SIZE - position

            # Make every already-recovered suffix byte equal desired_padding.
            for j in range(position + 1, BLOCK_SIZE):
                crafted_previous[j] = intermediate[j] ^ desired_padding

            found = False
            for guess in range(256):
                crafted_previous[position] = guess
                query_count += 1

                if not oracle(bytes(crafted_previous), target_block):
                    continue

                # At the final byte, reject accidental longer valid paddings.
                if position == BLOCK_SIZE - 1:
                    confirmation = bytearray(crafted_previous)
                    confirmation[position - 1] ^= 1
                    query_count += 1
                    if not oracle(bytes(confirmation), target_block):
                        continue

                intermediate[position] = guess ^ desired_padding
                found = True
                break

            if not found:
                raise RuntimeError(
                    f"Unable to recover byte at position {position}. "
                    "Check that the oracle reliably reports PKCS#7 validity."
                )

        # CBC: P_i = AES_decrypt(C_i) XOR original C_(i-1).
        recovered_block = bytes(
            intermediate[i] ^ previous[i] for i in range(BLOCK_SIZE)
        )
        recovered.extend(recovered_block)
        previous = target_block

    return pkcs7_unpad(bytes(recovered)), query_count


def main():
    # Demonstration setup only. The attack below is not passed the key.
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)
    plaintext = (
        b"Padding oracle attacks exploit error messages. "
        b"Never reveal whether CBC padding was valid."
    )

    ciphertext = encrypt_message(plaintext, key, iv)
    oracle = make_padding_oracle(key)

    print("=== AES-CBC Padding Oracle Attack ===")
    print(f"IV (hex):         {iv.hex()}")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print("The attack uses only the IV, ciphertext, and Boolean oracle.")

    recovered, queries = padding_oracle_attack(iv, ciphertext, oracle)

    print(f"Recovered plaintext: {recovered.decode('utf-8', errors='replace')}")
    print(f"Oracle queries:      {queries}")
    print(f"Recovery successful: {recovered == plaintext}")


if __name__ == "__main__":
    main()
