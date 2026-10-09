# Assignment 8: AES-CBC Padding Oracle Attack

## Objective
Recover plaintext from AES-CBC ciphertext without giving the attack function the AES key, using only a Boolean oracle that reports whether PKCS#7 padding is valid.

## Files
- `padding_oracle_attack.py`: padding helpers, demonstration encryption, oracle, attack, and query counter.
- `test_padding_oracle_attack.py`: regression tests for multiple plaintext lengths and contents.

## Setup and execution
From the repository root in PowerShell:

```powershell
python -m pip install pycryptodome
python Assignment8\padding_oracle_attack.py
python -m unittest discover -s Assignment8 -p "test_*.py" -v
```

## How it works
CBC decryption is:

`P_i = D_K(C_i) XOR C_(i-1)`

The attack modifies the preceding ciphertext block (or IV), guesses bytes from right to left, and queries the padding oracle. Once the intermediate byte `D_K(C_i)` is inferred, XOR with the original preceding block recovers the plaintext byte. The script repeats this for every block, removes PKCS#7 padding, and reports the total oracle query count.

## Query count
The exact count varies by run because each byte is recovered by trying candidate values and stopping when the oracle confirms valid padding. The counter includes confirmation queries used to reject an accidental longer-padding match.

## Security recommendations
- Prefer authenticated encryption such as AES-GCM with correct nonce handling.
- For legacy CBC, authenticate ciphertext before decrypting or checking padding.
- Avoid distinguishable error messages and timing differences.
- Use established cryptographic libraries and secure protocol designs.

## Important note
This is a local educational demonstration. Its key is used only by the encryption setup and the oracle. `padding_oracle_attack()` receives no key. For a course-provided ciphertext, use the supplied IV and ciphertext with the actual oracle, then record the recovered plaintext and query count for that specific input.
