# Assignment 9: OS Random Number Generation Analysis

## Objective
Evaluate operating-system random-number generation mechanisms
and investigate their suitability for cryptographic applications.

## Technologies Used
- Python
- Linux /dev/urandom
- OpenSSL RAND
- Windows CNG / .NET
- NumPy
- Pandas
- SciPy
- Matplotlib
- Jupyter Notebook

## Tasks
1. Generate 1 MB random data.
2. Analyze byte-frequency distributions.
3. Analyze bit distributions.
4. Detect repeated patterns.
5. Calculate serial correlations.
6. Perform statistical tests.
7. Investigate Linux and Windows RNG mechanisms.
8. Compare cryptographic security.

## Execution

Generate random data:
python src/generate_random.py

Run analysis:
python src/random_analysis.py

Open notebook:
jupyter notebook

## Conclusion
Statistical randomness is important but does not
independently guarantee cryptographic security.
