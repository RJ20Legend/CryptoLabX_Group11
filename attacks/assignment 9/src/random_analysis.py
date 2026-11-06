import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

files = {
    "Linux urandom": "attacks/assignment 9/outputs/linux_urandom.bin",
    "OpenSSL": "attacks/assignment 9/outputs/openssl_random.bin",
    "Windows CNG": "attacks/assignment 9/outputs/windows_cng.bin"
}

for name, path in files.items():

    try:
        data = np.fromfile(path, dtype=np.uint8)
    except FileNotFoundError:
        print(f"\n{name}: File not found. Skipping.")
        continue

    print("\n==========", name, "==========")

    # Byte frequency
    frequency = np.bincount(data, minlength=256)

    print("Total bytes:", len(data))
    print("Minimum frequency:", frequency.min())
    print("Maximum frequency:", frequency.max())

    # Chi-square test for uniform byte distribution
    expected = np.full(256, len(data) / 256)
    chi, p_value = chisquare(frequency, expected)

    print("Chi-square:", chi)
    print("P-value:", p_value)

    # Bit distribution
    bits = np.unpackbits(data)

    zeros = np.sum(bits == 0)
    ones = np.sum(bits == 1)

    print("Number of zeros:", zeros)
    print("Number of ones:", ones)
    print("Bit proportion of ones:", ones / len(bits))

    # Repeated consecutive byte pairs
    repeated_pairs = np.sum(data[:-1] == data[1:])

    print("Repeated consecutive bytes:", repeated_pairs)

    # Serial correlation
    correlation = np.corrcoef(data[:-1], data[1:])[0, 1]

    print("Serial correlation:", correlation)

    # Byte frequency graph
    plt.figure(figsize=(10, 4))
    plt.bar(range(256), frequency)
    plt.title(name + " - Byte Frequency Distribution")
    plt.xlabel("Byte Value")
    plt.ylabel("Frequency")
    plt.savefig(
        "attacks/assignment 9/reports/" +
        name.replace(" ", "_") + "_frequency.png"
    )
    plt.close()

print("\nAnalysis completed!")
