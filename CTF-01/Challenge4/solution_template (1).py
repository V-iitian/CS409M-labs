from typing import List

def decrypt(ciphers: List[bytes]) -> str:
    # write decryption logic
    message = []
    for i in range(len(ciphers[0])):
        k = 0 
        for j in range(len(ciphers)):
            k = k|ciphers[j][i]
        message.append(k)
    

    message_bytes = bytes(message)

    return message_bytes.decode('utf-8')

def decrypt_wrapper(filename: str = "ciphers.dat") -> str:
    with open(filename, "r") as f:
        ciphers = [bytes.fromhex(line.strip()) for line in f if line.strip()]

    return decrypt(ciphers)

if __name__ == "__main__":
    print(decrypt_wrapper()) # output the flag
