
import os
import numpy as np
from scipy.stats import chisquare, norm
DATASETS = {
    "Linux /dev/urandom": "generated_data/linux_urandom.bin",
    "OpenSSL rand": "generated_data/openssl_rand.bin",
    ".NET RandomNumberGenerator": "generated_data/dotnet_rng.bin"
}


def analyze_file(name, filepath):
    with open(filepath, "rb") as file:
        data = file.read()

    values = np.frombuffer(data, dtype=np.uint8)

    # 1. Byte frequency distribution
    frequencies = np.bincount(values, minlength=256)

    # 2. Bit distribution
    bits = np.unpackbits(values)
    zero_bits = np.count_nonzero(bits == 0)
    one_bits = np.count_nonzero(bits == 1)

    # 3. Repeated adjacent bytes
    adjacent_repeats = np.count_nonzero(
        values[:-1] == values[1:]
    )

    # 4. Repeated non-overlapping 4-byte blocks
    blocks = [
        data[i:i + 4]
        for i in range(0, len(data) - 3, 4)
    ]

    repeated_blocks = len(blocks) - len(set(blocks))

    # 5. Serial correlation between consecutive bytes
    correlation = np.corrcoef(
        values[:-1], values[1:]
    )[0, 1]

    print("\n" + "=" * 55)
    print(f"ANALYSIS: {name}")
    print("=" * 55)

    print(f"File size: {len(data)} bytes")
    print(f"Distinct byte values: {np.count_nonzero(frequencies)}")

    print("\nBYTE FREQUENCY")
    print(f"Minimum frequency: {frequencies.min()}")
    print(f"Maximum frequency: {frequencies.max()}")
    print(f"Expected average frequency: {len(data) / 256:.2f}")

    print("\nBIT DISTRIBUTION")
    print(f"Zero bits: {zero_bits}")
    print(f"One bits: {one_bits}")
    print(f"Zero percentage: {zero_bits / len(bits) * 100:.4f}%")
    print(f"One percentage: {one_bits / len(bits) * 100:.4f}%")

    print("\nREPEATED PATTERNS")
    print(f"Adjacent repeated bytes: {adjacent_repeats}")
    print(f"Repeated 4-byte blocks: {repeated_blocks}")

    print("\nSERIAL CORRELATION")
    print(f"Correlation coefficient: {correlation:.6f}")


def formal_tests(name, data):
    values = np.frombuffer(data, dtype=np.uint8)

    print("\nFORMAL STATISTICAL TESTS")

    # 1. Chi-square byte frequency test
    frequencies = np.bincount(values, minlength=256)
    expected = np.full(256, len(values) / 256)

    chi_stat, chi_p = chisquare(frequencies, expected)

    print("\nChi-square test:")
    print(f"Statistic: {chi_stat:.4f}")
    print(f"P-value: {chi_p:.6f}")
    print("Result:", "PASS" if chi_p >= 0.01 else "FAIL")

    # Convert bytes into individual bits
    bits = np.unpackbits(values)
    n = len(bits)

    # 2. Monobit frequency test
    ones = np.count_nonzero(bits)
    proportion = ones / n

    s_obs = abs(2 * ones - n) / np.sqrt(n)
    monobit_p = 2 * norm.sf(s_obs)

    print("\nMonobit frequency test:")
    print(f"Proportion of ones: {proportion:.6f}")
    print(f"P-value: {monobit_p:.6f}")
    print("Result:", "PASS" if monobit_p >= 0.01 else "FAIL")

    # 3. Runs test
    runs = 1 + np.count_nonzero(bits[1:] != bits[:-1])

    pi = proportion
    if abs(pi - 0.5) >= 2 / np.sqrt(n):
        runs_p = 0.0
    else:
        expected_runs = 2 * n * pi * (1 - pi) + 1
        variance = (
            2 * n * pi * (1 - pi)
            * (2 * n * pi * (1 - pi) - 1)
            / (n - 1)
        )

        z = abs(runs - expected_runs) / np.sqrt(variance)
        runs_p = 2 * norm.sf(z)

    print("\nRuns test:")
    print(f"Observed runs: {runs}")
    print(f"P-value: {runs_p:.6f}")
    print("Result:", "PASS" if runs_p >= 0.01 else "FAIL")


if __name__ == "__main__":
    for name, filepath in DATASETS.items():
        if os.path.exists(filepath):
            with open(filepath, "rb") as file:
                data = file.read()

                analyze_file(name, filepath)
                formal_tests(name, data)
        else:
            print(f"Missing dataset: {filepath}")
