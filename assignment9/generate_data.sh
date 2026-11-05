
#!/bin/bash

mkdir -p generated_data

# Generate 1 MB using Linux kernel RNG
dd if=/dev/urandom of=generated_data/linux_urandom.bin bs=1M count=1 status=progress

# Generate 1 MB using OpenSSL
openssl rand -out generated_data/openssl_rand.bin 1048576

echo "Random datasets generated successfully."
