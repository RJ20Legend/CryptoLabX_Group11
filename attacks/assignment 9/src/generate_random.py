import os
import subprocess

SIZE = 1024 * 1024

output_dir = "attacks/assignment 9/outputs"

os.makedirs(output_dir, exist_ok=True)

# 1. Generate random data using /dev/urandom
with open("/dev/urandom", "rb") as source:
    data = source.read(SIZE)

with open(output_dir + "/linux_urandom.bin", "wb") as file:
    file.write(data)

print("[+] Generated 1 MB using /dev/urandom")

# 2. Generate random data using OpenSSL
subprocess.run([
    "openssl", "rand",
    "-out", output_dir + "/openssl_random.bin",
    str(SIZE)
], check=True)

print("[+] Generated 1 MB using OpenSSL")

print("[+] Random data generation completed!")
