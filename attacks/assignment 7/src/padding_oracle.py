# Assignment 7: Padding Oracle Attack

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES block size is 16 bytes
BLOCK_SIZE = 16


# Function to encrypt the original message
def encrypt_message(message, key, iv):

    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_message = pad(message, BLOCK_SIZE)

    ciphertext = cipher.encrypt(padded_message)

    return ciphertext


# Function to create the padding oracle
def create_padding_oracle(secret_key):

    def oracle(previous_block, target_block):

        cipher = AES.new(
            secret_key,
            AES.MODE_CBC,
            previous_block
        )

        try:
            decrypted = cipher.decrypt(target_block)

            unpad(decrypted, BLOCK_SIZE)

            return True

        except ValueError:
            return False

    return oracle
# Function to perform Padding Oracle Attack

def padding_oracle_attack(iv, ciphertext, oracle):

    block_size = 16
    total_queries = 0

    # Divide ciphertext into 16-byte blocks
    blocks = [
        ciphertext[i:i + block_size]
        for i in range(0, len(ciphertext), block_size)
    ]

    recovered_plaintext = b""

    # Process each ciphertext block
    for block_index, target_block in enumerate(blocks):

        # Previous ciphertext block or IV
        if block_index == 0:
            previous_block = iv
        else:
            previous_block = blocks[block_index - 1]

        intermediate = bytearray(block_size)
        plaintext_block = bytearray(block_size)

        # Recover bytes from right to left
        for position in range(block_size - 1, -1, -1):

            padding_value = block_size - position

            crafted_block = bytearray(block_size)

            # Set already recovered bytes
            for j in range(position + 1, block_size):
                crafted_block[j] = (
                    intermediate[j] ^ padding_value
                )

            found = False

            # Try all possible byte values
            for guess in range(256):

                crafted_block[position] = guess

                total_queries += 1

                # Ask the padding oracle
                if oracle(bytes(crafted_block), target_block):

                    # Confirm valid padding candidates
                    if position > 0:

                        check_block = bytearray(crafted_block)
                        check_block[position - 1] ^= 1

                        total_queries += 1

                        if not oracle(
                            bytes(check_block),
                            target_block
                        ):
                            continue

                    # Calculate intermediate byte
                    intermediate[position] = (
                        guess ^ padding_value
                    )

                    # Recover original plaintext byte
                    plaintext_block[position] = (
                        intermediate[position]
                        ^ previous_block[position]
                    )

                    found = True
                    break

            if not found:
                raise Exception(
                    "Unable to recover byte at position "
                    + str(position)
                )

        recovered_plaintext += bytes(plaintext_block)

        print(
            "Recovered block",
            block_index + 1,
            ":",
            bytes(plaintext_block)
        )

    # Remove PKCS#7 padding
    recovered_plaintext = unpad(
        recovered_plaintext,
        block_size
    )

    return recovered_plaintext, total_queries
# Main function

def main():

    print("====================================")
    print("       PADDING ORACLE ATTACK")
    print("====================================")

    # Generate a random AES key and IV
    key = os.urandom(16)
    iv = os.urandom(16)

    # Original plaintext
    message = b"Padding Oracle Attack recovers plaintext without knowing the AES key."

    # Encrypt the message
    ciphertext = encrypt_message(message, key, iv)

    print("\nOriginal Plaintext:")
    print(message.decode())

    print("\nCiphertext:")
    print(ciphertext.hex())

    # Create padding oracle
    oracle = create_padding_oracle(key)

    print("\nStarting Padding Oracle Attack...\n")

    # Perform attack without passing the key
    recovered, queries = padding_oracle_attack(
        iv,
        ciphertext,
        oracle
    )

    print("\n====================================")
    print("           ATTACK RESULTS")
    print("====================================")

    print("\nRecovered Plaintext:")
    print(recovered.decode())

    print("\nTotal Oracle Queries:")
    print(queries)

    print("\nAttack Successful:",
          recovered == message)


# Program execution
if __name__ == "__main__":
    main()
