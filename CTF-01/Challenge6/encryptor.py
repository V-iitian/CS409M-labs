"""
Vigenere cipher over the 95-character printable-ASCII alphabet.

Alphabet: the 95 characters from 0x20 (space) to 0x7E (~), inclusive.
Each character c is assigned the integer ord(c) - 0x20, i.e. an integer
in [0, 94]. Encryption is
    c_i = ( p_i + k_{i mod L} ) mod 95
where p_i, k_i, c_i are the integer encodings of the plaintext, key,
and ciphertext characters respectively, and L is the length of the key.

Any character in the input plaintext that falls outside the printable
ASCII range (for example, newlines or tabs) is silently dropped before
encryption -- the ciphertext is a continuous string of printable-ASCII
characters. The ciphertext is written out wrapped at 80 characters per
line purely for the reader's convenience; the line breaks are not part
of the ciphertext and should be removed before decryption.
"""

ALPHABET_START = 0x20
ALPHABET_SIZE  = 95   # 0x20 .. 0x7E inclusive


def is_in_alphabet(c: str) -> bool:
    return ALPHABET_START <= ord(c) < ALPHABET_START + ALPHABET_SIZE


def to_int(c: str) -> int:
    return ord(c) - ALPHABET_START


def to_char(x: int) -> str:
    return chr((x % ALPHABET_SIZE) + ALPHABET_START)


def encrypt(plaintext: str, key: str) -> str:
    assert all(is_in_alphabet(c) for c in key), \
        "Key must consist only of printable-ASCII characters (0x20..0x7E)."
    filtered = [c for c in plaintext if is_in_alphabet(c)]
    L = len(key)
    out = []
    for i, p in enumerate(filtered):
        c_int = (to_int(p) + to_int(key[i % L])) % ALPHABET_SIZE
        out.append(to_char(c_int))
    return "".join(out)


def wrap(s: str, width: int = 80) -> str:
    return "\n".join(s[i:i + width] for i in range(0, len(s), width))


if __name__ == "__main__":
    with open("plaintext.txt", "r") as f:
        plaintext = f.read()

    # The key is a passphrase drawn from the same 95-character alphabet
    # as the plaintext. Its length is revealed to the student.
    key = "REDACTED"

    ciphertext = encrypt(plaintext, key)

    with open("ciphertext.txt", "w") as f:
        f.write(wrap(ciphertext) + "\n")

    print(f"Encrypted {len(ciphertext)} characters "
          f"with a key of length {len(key)}.")
