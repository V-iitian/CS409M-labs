from Crypto.Util.strxor import strxor
import string
ALPHABET = string.ascii_lowercase + "1234567890_"
def load_ciphertext(filename):
    with open(filename, "rb") as f:
        # hex_string = f.read()
        # actual_bytes = bytes.fromhex(hex_string)
        return f.read()


if __name__=="__main__":
    c1 = load_ciphertext("ciphertext1.enc")
    c2 = load_ciphertext("ciphertext2.enc")
    # print(c1)
    # print(c2)
    cipher_xor = strxor(c1,c2)
    print("length of the cipher text",len(cipher_xor))
    print("english text till now is ",strxor(b"cs409m{decryption_of_encrypted_data_reveal_information}",cipher_xor[0:55]))
    print(strxor(b"}",cipher_xor[54:55]))
    print("flag text till now is ",strxor(b"one_time_pad_is_perfectly_secure_only_theoretically_",cipher_xor[0:52]))
    i= int(input("give chracter pos"))
    if i==-1:
         j=int(input("give chracter pos for all alphabets check"))
         for char in ALPHABET:
                bits = bytes(char,encoding='utf-8')
                ans = strxor(bits,cipher_xor[j:j+1])
                print(char," used and its flag text is ",ans)
    else:
        print("Now working with",i," th chracter")
        char = input("chracter you wanna try:")
        bits = bytes(char,encoding='utf-8')
        j=i+1
        print(char,"is used for english text and flag is",strxor(bits,cipher_xor[i:j]))
