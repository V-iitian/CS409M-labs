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
    loop_around = True
    flag = "cs409m{"
    english_text = strxor(cipher_xor[:7],bytes(flag,encoding='utf-8')).decode('utf-8')
    print("current_flag_is :-  ",flag)
    print("current_english_text_is :-  ",english_text)
    print("\n\n\n")
    curr_index = 8
    while loop_around:
        print("Choose among the following operations")
        print("1. Guess the english message")
        print("2. Guess the flag")
        print("3. print the flag decrypted till now")
        print("4. print the english message decrypted till now")
        print("5. exit the program")
        i = int(input("give the operation you wanna go with"))
        if i==5:
            loop_around = False

        elif i==2:
            cha = input("choose the chracter")
            char_bytes = bytes(cha,encoding='utf-8')
            flag = flag+cha
            print(flag)
            english_text = strxor(cipher_xor[:curr_index],bytes(flag,encoding='utf-8')).decode('utf-8')
            print("current_flag_is :-  ",flag)
            print("current_english_text_is :-  ",english_text)
            curr_index+=1
        elif i==1:
            cha = input("choose the chracter")
            char_bytes = bytes(cha,encoding='utf-8')
            english_text=english_text+cha
            flag = strxor(cipher_xor[:curr_index],bytes(english_text,encoding='utf-8')).decode('utf-8')
            print("current_flag_is :-  ",flag)
            print("current_english_text_is :-  ",english_text)
            curr_index+=1
        elif i==3:
            print("current_flag_is :-  ",flag)
        elif i==4:
            print("current_english_text_is :-  ",english_text)

    print("Final_flag_is",flag)