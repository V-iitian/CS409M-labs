from typing import List
from Crypto.Util.strxor import strxor
import secrets

A = 0x243f6a8885a308d313198a2e03707345
C = 0xb7e151628aed2a6abf7158809cf4f3c7
M = 2 ** 128


def prg(seed: bytes) -> bytes:
    state = int.from_bytes(seed, "big")
    output = (A * state + C) % M
    return output.to_bytes(16, "big")


def encrypt(key: bytes, message: bytes) -> bytes:
    return strxor(prg(key), message)

def send_flag(flag: str):
    ciphertexts: List[str] = []

    for char in flag:
        message_string = "The next char: " + char
        message_bytes = message_string.encode()

        # 8 random bytes
        key: bytes = secrets.token_bytes(8)

        ciphertext = encrypt(key, message_bytes)

        ciphertexts.append(ciphertext.hex())

    with open("ciphertexts.hex", 'w') as f:
        f.write('\n'.join(ciphertexts))


send_flag("REDACTED")