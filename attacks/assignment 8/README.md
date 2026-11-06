
# Assignment 8: Cryptographic Prime Generation Using Miller-Rabin

## Objective
Generate a probable prime of 512-bit length using the Miller-Rabin primality test.

## Implementation
1. Generate random 512-bit odd candidate integers.
2. Apply the Miller-Rabin primality test.
3. Use 40 random bases for the final successful candidate.
4. Reject composite candidates and generate new ones.
5. Verify the generated prime independently using SymPy.

## Experimental Results

| Parameter | Value |
|---|---|
| Assigned bit length | 512 |
| Actual bit length | 512 |
| Number of candidates tested | 21 |
| Miller-Rabin rounds | 40 |
| Total rounds executed | 60 |
| Execution time | 0.053574 seconds |

## Generated Prime

12821859789702768861454175314504545406529886378210943026485330678514634537475407606334878939168468772337045457223424600645781782837541335873385302549849551

## Verification

- Exact bit length: True
- Odd number: True
- Miller-Rabin verification: True
- Independent SymPy verification: True

## Requirements
- Python 3
- SymPy 1.14.0

## Execution

pip install sympy
python "src/miller_rabin.py"

