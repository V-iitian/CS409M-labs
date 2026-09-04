import string
from collections import Counter
import numpy as np

ALPHABET = string.ascii_lowercase

def load_ciphertext(filename="ciphertext.txt"):
    with open(filename, "r") as f:
        return f.read()


def show_frequency(ciphertext):
    ascii_range = np.arange(97,123,1)
    frequency_analy = Counter(char for char in ciphertext if ord(char) in ascii_range)
    print(frequency_analy)

    
def show_mapping(mapping):
    print("\nCurrent mapping:")
    print("----------------")

    for c in ALPHABET:
        print(f"{c} -> {mapping[c]}")


def decrypt(ciphertext, mapping):
    plain_text = ""
    for ch in ciphertext:
        if ch in ALPHABET:
            plain_text+=(mapping[ch])
        else:
            plain_text+=(ch)
    return plain_text
    

def set_mapping(mapping, cipher_char, plain_char):
    """
    Map one ciphertext character to one plaintext character.
    """
    cipher_char = cipher_char.lower()
    plain_char = plain_char.lower()

    if cipher_char not in ALPHABET:
        print("Invalid ciphertext character.")
        return

    if plain_char not in ALPHABET:
        print("Invalid plaintext character.")
        return

    mapping[cipher_char] = plain_char


def reset_mapping():
    return {letter: letter for letter in ALPHABET}


def main():
    ciphertext = load_ciphertext()
    mapping = reset_mapping()
    ciphertext = ciphertext.lower()
    # print(ciphertext)
    # show_frequency(ciphertext)
    print("\nInitial plaintext:")
    print("------------------")
    # print(decrypt(ciphertext, mapping))

    while True:
        print("\nOptions:")
        print("  1. Show plaintext")
        print("  2. Show frequency")
        print("  3. Show mapping")
        print("  4. Set mapping")
        print("  5. Reset Mapping")
        print("  6. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            print("\nCurrent plaintext:")
            print("------------------")
            with open("output.txt", "w") as file:
                file.write(decrypt(ciphertext,mapping))

        elif choice == "2":

            show_frequency(ciphertext)

        elif choice == "3":

            show_mapping(mapping)

        elif choice == "4":
            ## b
            cipher_char = input(
                "Ciphertext character: "
            ).strip()

            plain_char = input(
                "Plaintext character: "
            ).strip()

            set_mapping(mapping, cipher_char, plain_char)
        elif choice=="5":
            mapping=reset_mapping()
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


