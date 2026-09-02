from typing import List
from Crypto.Util.strxor import strxor

A = 0x243f6a8885a308d313198a2e03707345
C = 0xb7e151628aed2a6abf7158809cf4f3c7
M = 2 ** 128

def load_ciphertexts(filename="ciphertexts.hex") -> List[bytes]:
    _ciphertexts = []
    with open(filename, "r") as f:
        for _line in f.readlines():
            _ciphertexts.append(bytes.fromhex(_line))

    return _ciphertexts

def mod_inv(_x: int, _M: int) -> int:
    """
    Modular Inverse of _x mod _M
    _x⁻¹ (mod _M)
    """

    return pow(_x, -1, _M)


ciphertexts: List[bytes] = load_ciphertexts()

if __name__=='__main__':
    flag = ""
    messages = []
    keys = []
    for i,ciphers in enumerate(ciphertexts):
        print(f"decrypting {i}-th chracter")
        for j in range(0,255,1):
            message_first = "The next char: "
            message_first_byte = bytes(message_first,encoding='utf-8')
            last_bit = j.to_bytes(1)
            mixed_first = message_first_byte+last_bit
            true_pseudo_gen_key = strxor(mixed_first,ciphers)
            state = int.from_bytes(true_pseudo_gen_key, "big")
            A_inverse = mod_inv(A,M)
            if (A_inverse*(state-C))%M<=2**64:
                k = (A_inverse*(state-C))%M
                # print("possible key for",i,"th chracter is ",k)
                messages.append(mixed_first.decode('utf-8')[-1])
                keys.append(k)
    result = "".join(messages)
    print("The Flage is ",result)
    print('the key for each cipher is ',keys)
# Find and output the flag!